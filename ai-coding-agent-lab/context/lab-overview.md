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

## 현재 상태
- 실험실 구조 생성 완료 (2026-06-05)
- 프롬프트 팩 16개 (00~15) + AI-네이티브 플레이북 (16) 준비 완료
- sandbox/sample-spring-api·sample-react-app 생성 완료 — 단, **빌드 환경 미비**(gradlew 래퍼·JDK 등록 문제)로 그대로는 빌드 불가
- 도구 가용성: `claude`·`codex` 설치됨 / `pi`·`aider` 미설치 → "Pi vs Aider" 실험은 현재 불가
- 첫 다리: pact-conference에 코드 기반 AGENTS.md 생성·검증 완료

## 핵심 제약
- destructive command 기본 금지
- 모든 자동 수정은 git diff로 검토 가능
- **회사/운영 코드(bf/workspace)**: 자동 머지 금지, 프로덕션 쓰기 금지, 사람 승인 필수
- **개인 코드(pact-conference)**: 자유롭게 실행하되 force push·시크릿 노출·harness 스키마 무단 변경 금지

## 다음 마일스톤
- pact-conference: ~~빌드 환경 복구~~(완료) → AGENTS.md 기반 첫 실제 작업 1건 실행 + eval 기록
- pact-conference용 프롬프트팩/가드레일 튜닝
- bf/workspace: 보수적 가드레일부터 수립 후 읽기·제안 워크플로 도입
- context/tool-insights.md 채우기, eval 기준 정립
