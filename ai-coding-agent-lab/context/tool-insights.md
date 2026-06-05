# Tool Insights

도구별 학습 사항. 실험 후 누적 기록한다.

## Pi
- (실험 후 기록)

## Claude Code
- (2026-06-05) 백그라운드 task의 exit code를 신뢰하지 말 것 — `| tail` 등 파이프 때문에 BUILD FAILED여도 exit 0으로 보고됨. 실제 출력으로 검증.
- (2026-06-05) 멀티서비스 빌드 복구처럼 "한 겹 고치면 다음 겹이 드러나는" 작업에 강함. 단 매 단계 실제 실패 메시지 추적이 필수.
- (2026-06-05) AGENTS.md를 먼저 코드에서 역도출 → 이후 작업 품질·일관성 상승. lab→주력 프로젝트 이식의 핵심 자산.

## Codex CLI
- (실험 후 기록)

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
