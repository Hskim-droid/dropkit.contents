# 2026-09-21 generic surface probe

- 목표: GitHub에서 받은 harness가 메뉴 경로와 화면 DOM을 모르는 상태에서도
  브라우저 접근성 표면을 관찰하고, 읽기 전용 추출만 안전하게 수행할 수 있는
  범용성 경계를 설계·검증한다.
- 승인된 범위: 외부 사례·공식 문서 조사, semantic browser probe 구현, 공통
  `UiObservation`/`ActionReceipt`/`SurfaceAdapter` 계약 추가, synthetic QMS
  변형 fixture 검증, 공개 `main` 푸시. Native UIA/AX/AT-SPI 실제 어댑터와
  ERP·메일 연결은 이번 단계에 추가하지 않는다.
- 기준 파일: `agent-harness/surface_adapter.py`, `agent-harness/browser_probe.py`,
  `fixtures/qms_task.json`, `fixtures/qms_variant_*.html`,
  `tests/test_browser_probe.py`, `tests/test_surface_adapter.py`,
  `agent-harness/README.md`.
- 완료 근거: 18개 unittest 통과, `py_compile`, `git diff --check`, variant 3
  CLI 실행 확인. 검증 범위는 메뉴 깊이·언어·컬럼 순서·DOM 변화, 미공개 라벨,
  동일 스키마 완료 테이블, 필드 충돌, 금지 메뉴, 중복 ID·산출물 기존 검사를
  포함한다.
- 공개 커밋: `d757efe` (`Require explicit browser probe safety terms`), 이전
  generic probe 커밋 `4cc5c3f` 포함. 원격: `Hskim-droid/dropkit.contents`.
- 남은 제한: 접근성 이름/라벨이 없는 화면은 이 어댑터가 중단한다. Native
  macOS/Windows/Linux 접근성 백엔드, OCR/비전 fallback, 실제 인증·ERP·메일
  adapter와 스케줄/큐 발송은 별도 작업이다.
- 사용자 미커밋 파일: `src/pages/sitemap.xml.ts`, `src/pages/work/index.astro`,
  `public/examples/`, `src/pages/work/scan-recovery.astro`는 건드리거나 푸시하지
  않았다.
