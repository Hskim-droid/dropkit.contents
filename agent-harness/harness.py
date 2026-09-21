#!/usr/bin/env python3
"""Cross-platform, draft-first queue for Codex-connected persona jobs.

The public repository only contains the control plane. UI extractors, document
renderers, and mail senders are local adapters configured outside git.
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


FORMATS = {"xlsx", "docx", "pptx"}
STATUSES = {"queued", "running", "drafted", "sent", "blocked", "failed"}


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def config_path(value: str | None) -> Path:
    return Path(value).expanduser() if value else repo_root() / "agent-harness" / "config.json"


def load_config(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(
            f"missing config: {path}. Copy agent-harness/config.example.json to {path}"
        )
    with path.open(encoding="utf-8") as handle:
        config = json.load(handle)
    if config.get("mode") not in {"draft_only", "live"}:
        raise ValueError("config.mode must be draft_only or live")
    return config


def path_from_config(config: dict[str, Any], key: str) -> Path:
    value = Path(str(config[key])).expanduser()
    return value if value.is_absolute() else repo_root() / value


def database_path(config: dict[str, Any]) -> Path:
    return path_from_config(config, "state_dir") / "queue.sqlite3"


def connect(config: dict[str, Any]) -> sqlite3.Connection:
    path = database_path(config)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA journal_mode=WAL")
    return connection


def init_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        CREATE TABLE IF NOT EXISTS jobs (
          id TEXT PRIMARY KEY,
          persona_id TEXT NOT NULL,
          source_system TEXT NOT NULL,
          request TEXT NOT NULL,
          output_format TEXT NOT NULL CHECK(output_format IN ('xlsx','docx','pptx')),
          recipients_json TEXT NOT NULL,
          trigger TEXT NOT NULL,
          priority INTEGER NOT NULL DEFAULT 0,
          status TEXT NOT NULL DEFAULT 'queued',
          attempts INTEGER NOT NULL DEFAULT 0,
          artifact_path TEXT,
          error TEXT,
          created_at TEXT NOT NULL,
          updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS events (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          job_id TEXT,
          event_type TEXT NOT NULL,
          detail_json TEXT NOT NULL,
          created_at TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS jobs_status_order
          ON jobs(status, priority DESC, created_at ASC);
        """
    )
    connection.commit()


def event(connection: sqlite3.Connection, job_id: str | None, event_type: str, detail: Any) -> None:
    connection.execute(
        "INSERT INTO events(job_id,event_type,detail_json,created_at) VALUES (?,?,?,?)",
        (job_id, event_type, json.dumps(detail, ensure_ascii=False), now()),
    )
    connection.commit()


def ensure_config(path: Path) -> None:
    if path.exists():
        return
    example = path.parent / "config.example.json"
    if not example.exists():
        raise FileNotFoundError(f"missing example config: {example}")
    path.write_text(example.read_text(encoding="utf-8"), encoding="utf-8")


def cmd_init(args: argparse.Namespace) -> int:
    path = config_path(args.config)
    path.parent.mkdir(parents=True, exist_ok=True)
    ensure_config(path)
    config = load_config(path)
    path_from_config(config, "state_dir").mkdir(parents=True, exist_ok=True)
    path_from_config(config, "artifact_dir").mkdir(parents=True, exist_ok=True)
    with connect(config) as connection:
        init_schema(connection)
        event(connection, None, "HARNESS_INITIALIZED", {"config": str(path)})
    print(json.dumps({"ok": True, "config": str(path), "database": str(database_path(config))}, ensure_ascii=False))
    return 0


def cmd_doctor(args: argparse.Namespace) -> int:
    path = config_path(args.config)
    checks: dict[str, Any] = {"python": sys.version.split()[0], "config": str(path)}
    if not path.exists():
        checks["config_exists"] = False
        print(json.dumps(checks, ensure_ascii=False, indent=2))
        return 1
    try:
        config = load_config(path)
        checks.update(
            {
                "config_exists": True,
                "mode": config["mode"],
                "draft_only": config["mode"] == "draft_only",
                "state_dir": str(path_from_config(config, "state_dir")),
                "artifact_dir": str(path_from_config(config, "artifact_dir")),
                "executor_configured": any(config.get("executor", {}).values()),
            }
        )
        with connect(config) as connection:
            init_schema(connection)
        checks["database_ready"] = True
        checks["ok"] = True
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        checks["ok"] = False
        checks["error"] = str(exc)
    print(json.dumps(checks, ensure_ascii=False, indent=2))
    return 0 if checks.get("ok") else 1


def cmd_session_start(args: argparse.Namespace) -> int:
    path = config_path(args.config)
    config = load_config(path)
    with connect(config) as connection:
        init_schema(connection)
        event(
            connection,
            None,
            "SESSION_ATTACHED",
            {"agent": args.agent, "host": os.environ.get("COMPUTERNAME") or os.environ.get("HOSTNAME")},
        )
    print(json.dumps({"ok": True, "agent": args.agent, "mode": config["mode"]}, ensure_ascii=False))
    return 0


def cmd_enqueue(args: argparse.Namespace) -> int:
    if args.output_format not in FORMATS:
        raise ValueError(f"output format must be one of {sorted(FORMATS)}")
    path = config_path(args.config)
    config = load_config(path)
    recipients = [item.strip() for item in args.recipient if item.strip()]
    allowlist = set(config.get("recipient_allowlist", []))
    if allowlist and any(item not in allowlist for item in recipients):
        raise ValueError("recipient is outside config.recipient_allowlist")
    job_id = f"job-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{uuid.uuid4().hex[:8]}"
    created = now()
    with connect(config) as connection:
        init_schema(connection)
        connection.execute(
            """INSERT INTO jobs
            (id,persona_id,source_system,request,output_format,recipients_json,trigger,priority,status,created_at,updated_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (
                job_id,
                args.persona,
                args.source_system,
                args.request,
                args.output_format,
                json.dumps(recipients, ensure_ascii=False),
                args.trigger,
                args.priority,
                "queued",
                created,
                created,
            ),
        )
        event(connection, job_id, "JOB_QUEUED", {"request": args.request, "format": args.output_format})
    print(json.dumps({"ok": True, "job_id": job_id, "status": "queued"}, ensure_ascii=False))
    return 0


def row_json(row: sqlite3.Row) -> dict[str, Any]:
    value = dict(row)
    value["recipients"] = json.loads(value.pop("recipients_json"))
    return value


def cmd_status(args: argparse.Namespace) -> int:
    config = load_config(config_path(args.config))
    with connect(config) as connection:
        init_schema(connection)
        if args.job_id:
            row = connection.execute("SELECT * FROM jobs WHERE id=?", (args.job_id,)).fetchone()
            rows = [] if row is None else [row]
        else:
            rows = connection.execute(
                "SELECT * FROM jobs ORDER BY created_at DESC LIMIT ?", (args.limit,)
            ).fetchall()
    print(json.dumps([row_json(row) for row in rows], ensure_ascii=False, indent=2))
    return 0


def cmd_run_once(args: argparse.Namespace) -> int:
    config = load_config(config_path(args.config))
    with connect(config) as connection:
        init_schema(connection)
        row = connection.execute(
            "SELECT * FROM jobs WHERE status='queued' ORDER BY priority DESC, created_at ASC LIMIT 1"
        ).fetchone()
        if row is None:
            print(json.dumps({"ok": True, "message": "queue empty"}, ensure_ascii=False))
            return 0
        job = row_json(row)
        if args.dry_run:
            event(connection, job["id"], "DRY_RUN_PREVIEW", {"job": job})
            print(json.dumps({"ok": True, "dry_run": True, "job": job}, ensure_ascii=False, indent=2))
            return 0
        connection.execute(
            "UPDATE jobs SET status='running', attempts=attempts+1, updated_at=? WHERE id=?",
            (now(), job["id"]),
        )
        if not config.get("executor", {}).get("extract"):
            error = "no local UI extractor configured; job left blocked in draft-only control plane"
            connection.execute(
                "UPDATE jobs SET status='blocked', error=?, updated_at=? WHERE id=?",
                (error, now(), job["id"]),
            )
            event(connection, job["id"], "JOB_BLOCKED", {"reason": error})
            print(json.dumps({"ok": False, "job_id": job["id"], "status": "blocked", "error": error}, ensure_ascii=False))
            return 2
        event(connection, job["id"], "EXTRACTOR_HANDOFF_READY", {"executor": config["executor"]["extract"]})
        print(json.dumps({"ok": True, "job_id": job["id"], "status": "running", "next": "local extractor adapter"}, ensure_ascii=False))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Draft-first Codex persona job harness")
    parser.add_argument("--config", help="path to local config.json")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init", help="create local config/runtime state")
    sub.add_parser("doctor", help="check local runtime and safety defaults")

    session = sub.add_parser("session-start", help="record a Codex or local agent session")
    session.add_argument("--agent", default="codex")

    enqueue = sub.add_parser("enqueue", help="add one job to the FIFO/priority queue")
    enqueue.add_argument("--persona", default="han-gyeol")
    enqueue.add_argument("--source-system", required=True)
    enqueue.add_argument("--request", required=True)
    enqueue.add_argument("--output-format", choices=sorted(FORMATS), default="docx")
    enqueue.add_argument("--recipient", action="append", default=[])
    enqueue.add_argument("--trigger", choices=["scheduled", "email"], default="scheduled")
    enqueue.add_argument("--priority", type=int, default=0)

    status = sub.add_parser("status", help="show recent jobs")
    status.add_argument("--job-id")
    status.add_argument("--limit", type=int, default=20)

    run = sub.add_parser("run-once", help="take the next queued job")
    run.add_argument("--dry-run", action="store_true", help="preview without changing job state")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return {
            "init": cmd_init,
            "doctor": cmd_doctor,
            "session-start": cmd_session_start,
            "enqueue": cmd_enqueue,
            "status": cmd_status,
            "run-once": cmd_run_once,
        }[args.command](args)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
