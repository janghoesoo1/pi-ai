# Decision Log

결정 로그. 한 줄에 하나씩 append-only로 유지한다.
추론이 결론과 함께 따라가게 한다.

| 날짜 | 결정 | 이유 | 영향 |
|------|------|------|------|
| 2026-06-05 | 실험실 구조를 pi_based_ai_coding_agent_prompt_pack.md 기반으로 생성 | 원본 문서가 체계적인 프롬프트 팩과 실험 시나리오를 이미 포함 | 프롬프트 16개, policies 3개, experiments 2개 생성 |
| 2026-06-05 | sample-spring-api에 의도적 문제 7가지 삽입 | 도구 비교 벤치마크 시 발견 능력, 수정 범위, 테스트 품질 측정 목적 | N+1, 테스트 누락, 예외 불일치, DTO 미사용, Controller 로직, Tx 누락, PII 로그 |
| 2026-06-05 | AI-네이티브 스타트업 프레임워크를 OPERATING-GUIDE.md로 반영 | 실험실 운영에 체계적 피드백 루프와 eval 시스템 필요 | 6단계 프레임워크, 자율성 레벨, 주간 리뷰 체크리스트 도입 |
| 2026-06-05 | **lab의 역할을 "독립 샌드박스 실험실" → "주력 프로젝트의 AI 개발 컨트롤 플레인"으로 재정의** | 자동화의 회수 가치는 샌드박스가 아니라 실제 주력 프로젝트(pact-conference, bf/workspace)에 있음. 샌드박스에서만 검증하면 회수 시간 0 | 방법론·eval·규율은 lab에 자산으로 남기고, AGENTS.md·프롬프트팩·가드레일은 각 주력 프로젝트로 이식. 샌드박스는 "프로덕션 적용 전 스테이징"으로 강등 |
| 2026-06-05 | **첫 다리로 pact-conference-api-harness 선택** | 이름부터 harness로 lab 주제와 일치, 개인·저위험, gradlew 존재 | pact-conference 루트에 코드 기반 AGENTS.md 생성(검증 완료). bf/workspace는 다음 단계 |
| 2026-06-05 | **리스크 등급 분리: pact=개인(자유), bf/workspace=운영/회사(보수)** | bf는 프로덕션·Jenkins/CI 자산 | bf에는 읽기·제안만, 자동 머지·프로덕션 쓰기 금지. pact는 자율성 레벨 상향 가능 |
| 2026-06-05 | pact 빌드 복구를 PR로 분리(#4), room-service를 PR로 분리(#5) | 개인 repo가 PR 워크플로 사용 | pact는 푸시·PR 완료. bf는 보수적으로 브랜치 커밋만(미푸시) |
| 2026-06-05 | bf AGENTS.md는 작성하되 회사 리모트에 푸시하지 않음 | 운영/회사 코드 가드레일(읽기·제안만) | `docs/agents-md` 로컬 브랜치 커밋, 푸시·머지는 사람이 결정 |
| 2026-06-05 | pact PR #4·#5·#6 머지 완료, harness 근본 버그(#6) 수정 | 검증된 개인 repo 변경 | main이 빌드복구+room+harness수정 반영. pact는 안정 상태 |
| 2026-06-05 | bf 푸시 시도 → 사내 GitLab pre-receive 훅 500 거부 → 우회 안 함 | 회사 인프라 정책 존중 | bf AGENTS.md는 로컬 커밋 유지, 사람이 정식 프로세스로 푸시 |
| 2026-06-07 | **가드레일 강제화: PreToolUse hook(`.claude/hooks/deny-guard.py`) 도입** | "가드레일은 코드·설정에, 프롬프트는 보안 경계가 아니다" 원칙을 산문→실제 강제점으로 전환(감사 H1) | Bash 명령을 런타임에 정규식 검사해 denied-commands 위반 시 exit 2로 차단. PoC(완전 샌드박싱 아님), 패턴은 policies/denied-commands.md와 동기화. 5개 차단/허용 케이스 테스트 통과 |
| 2026-06-07 | **정밀 감사(병렬 4분야) 후 문서 정합성·정책·프롬프트 일괄 정정** | README stale 파일명, MySQL/H2 오기, denied-commands 누락(공급망·sudo 등), frontmatter 불일치 등 발견 | README/AGENTS/lab-overview 정정 + denied-commands 3개 섹션 추가 + 프롬프트 frontmatter 표준화. eval 무결성은 양호 확인 |
