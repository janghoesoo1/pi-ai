# Tool Insights

도구별 학습 사항. 실험 후 누적 기록한다.

## Pi
- (실험 후 기록)

## Claude Code
- (2026-06-05) 백그라운드 task의 exit code를 신뢰하지 말 것 — `| tail` 등 파이프 때문에 BUILD FAILED여도 exit 0으로 보고됨. 실제 출력으로 검증.
- (2026-06-05) 멀티서비스 빌드 복구처럼 "한 겹 고치면 다음 겹이 드러나는" 작업에 강함. 단 매 단계 실제 실패 메시지 추적이 필수.
- (2026-06-05) AGENTS.md를 먼저 코드에서 역도출 → 이후 작업 품질·일관성 상승. lab→주력 프로젝트 이식의 핵심 자산.

## Codex CLI
- (2026-06-07) **codex-cli 0.130.0 설치·실동작 확인.** `codex exec --sandbox read-only "<prompt>"`로 비대화형 second opinion 가능. lab 산출물(prompts 17~22)을 적대적 교차검증시켜 실제 결함 4건(High) 발견 — 19-cross-verify의 첫 dogfooding 성공.
- **옵션 사실 정정**: `codex exec`에는 `-s/--sandbox`가 있으나 **`codex review`에는 `--sandbox`가 없다**(git 기반·읽기 위주). WebFetch 요약을 믿고 `codex review --sandbox`로 썼다가 codex 자기검증에 걸림 → 로컬 `--help`로 확인 후 정정.
- 강점: 다른 모델 관점이라 Claude 자기검토가 놓친 결함(L1 실행 위험, 가드레일 충돌, 근거 부족)을 잡음. 교차검증 자산으로 유지 가치 1차 확인.
- 주의: codex 실행 시 sandbox에서 `git`/`xcrun` temp 접근 경고 다수 출력(기능엔 무해). verbose 로그가 커서(1MB+) 결과는 tail로 회수.

## Aider
- (실험 후 기록)

## Cline
- (실험 후 기록)

## Cursor
- (실험 후 기록)

## harness.sh (pact-conference 자체 스캐폴딩 CLI)
- (2026-06-05) `new-service`가 5개 횡단 관심사(gradle·gateway·k8s·prometheus·기동스크립트)를 단일 명령으로 일관 배선. dry-run이 실제와 정확히 일치 → 승인 게이트로 적합. L4 수준 신뢰.
- 한계: 산출 store가 untyped Map + TODO, 테스트 미생성, `.bak` 잔여. "동작하는 골격"이지 완성품 아님.
- 개선 후보: 기본 테스트 생성, `.bak` 자동정리, `--jpa` 플래그(kotlin-jpa+exclude 해제 자동).
- (2026-06-05) gateway `@Value` 이스케이프 버그 **근본 수정 완료**(PR #6 머지): sed→python literal. 향후 스캐폴드는 gateway 컴파일 정상.

## 공통 패턴
- (2026-06-05) **AGENTS.md는 코드에서 역도출하라.** 스캐폴딩 CLI/빌드설정에 컨벤션이 이미 인코딩돼 있으면 그게 1차 출처.
- (2026-06-05) **빌드 가능 여부가 모든 작업의 선결 조건.** 코드 품질 평가 이전에 red→green부터.
