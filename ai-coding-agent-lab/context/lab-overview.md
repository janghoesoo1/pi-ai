# Lab Overview

## 목적
Pi를 연구용/확장용 기반으로 삼고, Claude Code/Codex CLI/Aider/Cline/Goose/Continue의 장점을 벤치마킹해서 "내 개발 방식에 맞는 AI 코딩 운영체계"를 만든다.

## 역할 재정의 (2026-06-05)
lab은 "독립 샌드박스 실험실"이 아니라 **주력 프로젝트의 AI 개발을 운영하는 컨트롤 플레인**이다.
- 방법론·eval·규율 → lab에 자산으로 남는다
- AGENTS.md·프롬프트팩·가드레일 → 각 주력 프로젝트로 이식된다 (가치 회수)
- 샌드박스 → 위험한 워크플로를 주력에 적용하기 전 검증하는 스테이징

## 주력 프로젝트 (가치 회수 대상)
| 프로젝트 | 경로 | 성격 | 리스크/가드레일 | 상태 |
|----------|------|------|----------------|------|
| pact-conference-api-harness | `~/work/pact-conference-api-harness` | Kotlin/SpringBoot3 멀티서비스 + Pact + harness.sh | 개인·저위험 → 자율성 상향 가능 | **AGENTS.md 생성 + 빌드 복구(4겹 버그 수정, 전체 그린) 완료** |
| bf/workspace | `~/bf/workspace` | Kotlin DDD 백엔드(api/common/domain-ai·employee·mail·timesheet) + React/Vite 프론트 + Jenkins/GitLab CI, 운영 HR SaaS(제품이 Claude 사용) | 운영/회사 → 읽기·제안만, 자동머지·프로덕션 쓰기 금지 | **코드 기반 AGENTS.md 작성 → `docs/agents-md` 브랜치 커밋(미푸시, 사람 승인 대기)** |
| bf/ata-next-kotlin | `~/bf/ata-next-kotlin` | Next.js 프론트 + Kotlin 백엔드(WebFlux) 풀스택, Jenkins + 사내 GitLab(`bf.jang1/ata-next-kotlin`), 에어갭 사내 AI 플랫폼 | 운영/회사 → 읽기·제안만, 자동머지·프로덕션 쓰기 금지 | **AGENTS.md + frontend/CLAUDE.md 해당 폴더에 직접 생성 완료(2026-06-06, untracked — 사람 커밋 대기). cross-folder 금지 준수** |

## 현재 상태
- 실험실 구조 생성 완료 (2026-06-05)
- 프롬프트 팩 16개 (00~15) + AI-네이티브 플레이북 (16) 준비 완료
- **하네스 엔지니어링 Q&A(황민호 수석) 갭 분석 → 동적 운영 스킬 6개 추가 (2026-06-07): 17-agent-1on1·18-meta-tune·19-cross-verify·20-judge-panel·21-orchestrator·22-verification-patterns. AGENTS.md에 모델 티어링 절 추가. → `experiments/2026-06-07-harness-engineering-gap.md`**
- sandbox/sample-spring-api·sample-react-app 생성 완료 — 단, **`sandbox/sample-*`만 빌드 환경 미비**(gradle wrapper jar·JDK 등록 문제)로 그대로는 빌드 불가. (주력 pact-conference 빌드는 복구 완료·그린)
- 도구 가용성: `claude`·`codex` 설치됨 / `pi`·`aider` 미설치 → "Pi vs Aider" 실험은 현재 불가
- 첫 다리: pact-conference에 코드 기반 AGENTS.md 생성·검증 완료

## 핵심 제약
- destructive command 기본 금지
- 모든 자동 수정은 git diff로 검토 가능
- **회사/운영 코드(bf/workspace)**: 자동 머지 금지, 프로덕션 쓰기 금지, 사람 승인 필수
- **개인 코드(pact-conference)**: 자유롭게 실행하되 force push·시크릿 노출·harness 스키마 무단 변경 금지

## 다음 마일스톤
- pact-conference: ~~빌드 환경 복구~~(완료) → ~~AGENTS.md 기반 첫 실제 작업 + eval~~(완료: scaffold-room/room-typed 2건) → **3번째 eval**(scaffold-room/room-typed에서 약속한 store 단위테스트 / Pact consumer)
- pact-conference용 프롬프트팩/가드레일 튜닝
- bf/workspace: 보수적 가드레일부터 수립 후 읽기·제안 워크플로 도입. bf/ata-next-kotlin: 생성된 AGENTS.md 기반 첫 읽기·제안 워크플로
- ~~context/tool-insights.md 채우기~~(Claude Code/harness.sh 섹션 채움 완료; Codex CLI 섹션은 실험 후 보강), eval 기준 정립
- **가드레일 강제화(L1·설계 필요)**: 현재 정책은 산문뿐 — PreToolUse blocklist hook 등 실제 강제점 1개 이상 도입 또는 문서를 advisory로 명시
- **신규 스킬(17~22) 실전 검증**: 다음 pact-conference 작업을 `21-orchestrator.md`로 구동 + `19-cross-verify.md`로 codex 교차검증 1회 → eval 누적
- **자가 개선 루프(갭 #6)**: 수용률<70% 트리거 자동화. OMC `autoresearch` 연결 PoC (카파시 AutoResearch 스타일)
