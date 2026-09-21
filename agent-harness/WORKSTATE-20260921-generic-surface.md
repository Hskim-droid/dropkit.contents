# 2026-09-21 generic surface probe

- 목표: GitHub에서 받은 harness가 메뉴 경로와 화면 DOM을 모르는 상태에서도
  브라우저·로컬 앱의 읽기 전용 표면을 관찰하고, 사용자별 환경을 매핑한 뒤
  로컬 번역과 한 가지 문서 산출물로 안전하게 연결되는 범용성 경계를
  설계·검증한다.
- 승인된 범위: 외부 사례·공식 문서·RPA 논문 근거 추적, semantic browser probe 구현, 공통
  `UiObservation`/`ActionReceipt`/`SurfaceAdapter` 계약 추가, 선택적 macOS
  AXUIElement·Windows UIA 어댑터와 capability report, 관찰 ID 고정 실행,
  synthetic QMS 변형 fixture 검증, 개인식별자 수집을 하지 않는 host bootstrap 계획,
  loopback-only local translation adapter와 fixture DOCX 연결, 공개 `main` 푸시.
  Linux AT-SPI 실제 어댑터와 ERP·메일 연결은 이번 단계에 추가하지 않는다.
- 기준 파일: `agent-harness/surface_adapter.py`, `agent-harness/browser_probe.py`,
  `fixtures/qms_task.json`, `fixtures/qms_variant_*.html`,
  `tests/test_browser_probe.py`, `tests/test_surface_adapter.py`,
  `tests/test_native_adapters.py`, `agent-harness/bootstrap.py`,
  `agent-harness/translation_pipeline.py`, `agent-harness/fixture_demo.py`,
  `agent-harness/README.md`, `agent-harness/RPA_REFERENCE_LINEAGE.md`.
- 완료 근거: 53개 unittest 통과, `py_compile`, `git diff --check`, variant 3
  CLI 실행 확인. 검증 범위는 메뉴 깊이·언어·컬럼 순서·DOM 변화, 미공개 라벨,
  동일 스키마 완료 테이블, 필드 충돌, 금지 메뉴, 중복 ID·산출물 기존 검사를
  포함하며, bootstrap의 개인정보 비수집·허용 명령·명시적 네트워크 게이트,
  번역의 원문 보존·loopback endpoint·proxy/redirect/cloud guard(서버 재시작
  전제)·잘못된 JSON 중단·translated DOCX 검사를
  포함한다.
- 공개 커밋: `ea5e515` (`Add host bootstrap and local translation boundary`),
  기존 공개 기준은 `f1e8234` (`Document RPA lineage and pin UI actions`), 이전
  native adapter 커밋 `d0b496e`와 generic probe 커밋 `d757efe` 포함. 원격:
  `Hskim-droid/dropkit.contents`.
- 남은 제한: 실제 macOS/Windows 권한·창 연결 검증은 각 호스트가 필요하다.
  Linux AT-SPI 어댑터, 접근성 이름/라벨이 없는 화면의 OCR/비전 fallback,
  공통 native semantic planner·table extractor·postcondition evaluator,
  실제 인증·ERP·메일 adapter와 스케줄/큐 발송은 별도 작업이다. 실제 local-llm
  모델 weight 설치·RAM별 모델 검증과 XLSX/PPTX renderer도 별도 호스트/의존성
  검증이 필요하다. bootstrap은 엔진과 모델을 자동 설치하지 않는다.
- 사용자 미커밋 파일: `src/pages/sitemap.xml.ts`, `src/pages/work/index.astro`,
  `public/examples/`, `src/pages/work/scan-recovery.astro`는 건드리거나 푸시하지
  않았다.
