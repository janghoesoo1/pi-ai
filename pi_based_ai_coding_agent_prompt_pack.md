# Pi 기반 AI 코딩 에이전트 실험 프롬프트 팩

작성일: 2026-06-05  
목적: WikiDocs의 Pi 소개를 출발점으로, Pi와 주변 AI 코딩 에이전트 도구를 비교·분석한 뒤 직접 실험/개발/자동화에 활용할 수 있는 프롬프트 모음입니다.

---

## 0. 결론 요약

Pi는 Cursor나 Claude Code처럼 완성된 개발 경험을 제공하는 도구라기보다, **작고 확장 가능한 터미널 기반 AI agent harness**에 가깝습니다. 따라서 Pi를 그대로 메인 도구로 쓰기보다는, 다음 목적에 맞춰 쓰는 것이 좋습니다.

1. AI 코딩 에이전트의 내부 구조를 이해한다.
2. 내 개발 워크플로우에 맞춘 커스텀 에이전트/스킬/프롬프트 템플릿을 만든다.
3. Claude Code, Codex CLI, Aider, Cline, Goose, Continue 같은 외부 도구를 비교하면서 좋은 설계 패턴을 흡수한다.
4. 최종적으로는 `AGENTS.md`, 스킬, MCP, PR 체크, 샌드박스 실행 정책을 묶은 개인/팀용 AI 개발 하네스를 만든다.

가장 현실적인 방향은 다음입니다.

> **Pi를 연구용/확장용 기반으로 삼고, Claude Code/Codex CLI/Aider/Cline/Goose/Continue의 장점을 벤치마킹해서 “내 개발 방식에 맞는 AI 코딩 운영체계”를 만든다.**

---

## 1. 외부 도구 리서치 요약

| 도구 | 성격 | 강점 | 주의점 | Pi 기반 실험에 가져올 점 |
|---|---|---|---|---|
| Pi | 미니멀 터미널 agent harness | 확장성, provider 추상화, prompt template, skill, package | 내장 권한 시스템이 약함. sandbox 필요 | 커스텀 agent runtime 학습의 중심 |
| Claude Code | 완성도 높은 터미널/IDE/웹/Slack 코딩 에이전트 | 코드베이스 이해, 멀티파일 수정, 승인 기반 실행, Git/GitHub workflow | Claude 생태계 의존, 비용/사용량 관리 필요 | permission, context, agentic search, CLAUDE.md 패턴 |
| OpenAI Codex CLI | OpenAI 로컬 터미널 코딩 에이전트 | 로컬에서 코드 읽기/수정/실행, Rust 기반 CLI | ChatGPT/Codex 플랜 의존 | 터미널 UX, 로컬 실행, 작업 단위 관리 |
| GitHub Copilot CLI | GitHub-native 터미널 에이전트 | issue/PR 연동, `/plan`, `/fleet` 병렬 subagent | GitHub/Copilot 중심 workflow | PR/issue 중심 자동화 설계 |
| Aider | Git-native 터미널 AI 페어 프로그래머 | Git diff/commit workflow에 강함, 기존 코드베이스 편집에 적합 | 자동화 하네스라기보다는 페어 프로그래밍에 가까움 | Git 기반 변경 추적/commit 단위 작업 |
| Cline | VS Code/CLI/SDK 기반 오픈 코딩 에이전트 | Plan/Act, MCP, editor/terminal 통합, 승인 흐름 | IDE 의존성이 생길 수 있음 | Plan/Act 모드, MCP, human-in-the-loop |
| Roo Code | VS Code 계열 agent | 역할별 모드, auto-approve 제어, 코드베이스 인덱싱 | VS Code 중심 | 역할 기반 mode 설계 |
| Goose | 범용 로컬 AI agent | 코드뿐 아니라 리서치, 문서, 자동화, 데이터 분석까지 수행 | 코딩 전용 최적화는 별도 검증 필요 | 범용 agent + CLI/API/Desktop 패턴 |
| Continue | PR 체크 자동화 | Markdown 파일로 AI PR check 정의, GitHub status check | 코딩 assistant라기보다 품질 게이트 성격 | `.continue/checks/*.md` 방식의 정책 자동화 |
| Gemini CLI / Qwen Code | 터미널 기반 오픈소스 agent | 오픈소스, 모델별 특화, MCP/IDE 연동 가능 | 모델/플랫폼 성숙도 확인 필요 | 오픈소스 CLI agent 구조 비교 |
| Cursor / Windsurf / Devin | agentic IDE 또는 cloud/desktop agent | 제품 완성도, 병렬 agent, PR/Slack/GitHub 연동 | 벤더 종속, 비용, 보안 정책 확인 필요 | UX와 멀티에이전트 운영 방식 참고 |

---

## 2. 장회수님 기준 추천 실험 방향

### 2.1 바로 메인 도구로 쓰기보다 실험실을 만든다

Pi는 강력하지만, 내장 권한 통제는 Claude Code나 Cline 같은 완성형 도구보다 약하게 봐야 합니다. 그래서 회사 코드에 바로 붙이기 전에 아래 구조로 실험실을 먼저 만드십시오.

```text
ai-coding-agent-lab/
  README.md
  AGENTS.md
  prompts/
    00-research.md
    01-tool-evaluation.md
    02-pi-extension-design.md
    03-code-review.md
    04-spring-refactoring.md
  sandbox/
    sample-spring-api/
    sample-react-app/
  experiments/
    2026-06-05-pi-vs-aider.md
    2026-06-05-pi-extension.md
  policies/
    allowed-commands.md
    denied-commands.md
    security-checklist.md
```

### 2.2 Pi로 만들면 좋은 첫 번째 결과물

첫 결과물은 복잡한 agent framework가 아니라 다음 세 가지가 좋습니다.

1. **AGENTS.md 생성기**  
   프로젝트 구조, 빌드 명령, 테스트 명령, 금지 명령, 코드 스타일을 자동 정리합니다.

2. **Spring Boot 코드 리뷰 스킬**  
   Controller/Service/Repository/Transactional/JPA/N+1/API 응답 구조를 점검합니다.

3. **PR 전 자동 점검 프롬프트**  
   변경사항을 요약하고, 테스트 누락, 보안 이슈, 성능 리스크, 운영 리스크를 확인합니다.

---

# 3. 프롬프트 팩

아래 프롬프트들은 Pi, Claude Code, Codex CLI, Cursor, Cline, Aider 등에 그대로 넣고 사용할 수 있도록 작성했습니다.

---

## Prompt 01. AI 코딩 에이전트 도구 리서치 프롬프트

```markdown
당신은 Staff Engineer이자 AI Coding Agent Researcher입니다.

목표는 현재 프로젝트에 적합한 AI 코딩 도구 조합을 선정하는 것입니다.
다음 도구들을 비교 분석해 주세요.

대상 도구:
- Pi
- Claude Code
- OpenAI Codex CLI
- GitHub Copilot CLI
- Aider
- Cline
- Roo Code
- Goose
- Continue
- Gemini CLI
- Qwen Code
- Cursor

분석 기준:
1. 도구의 핵심 철학
2. 터미널/IDE/GitHub/Slack/CI 연동 방식
3. 코드베이스 이해 방식
4. 파일 수정 및 명령 실행 권한 모델
5. context file 지원 여부: AGENTS.md, CLAUDE.md, rules, memories 등
6. MCP 또는 외부 도구 연동 여부
7. Java/Spring Boot 백엔드 프로젝트에 적합한지
8. 엔터프라이즈 보안 관점의 위험
9. 개인 개발자 실험용으로 적합한지
10. 팀 표준화 도구로 적합한지

결과 형식:
- 1페이지 요약
- 비교표
- 추천 조합 3개
- PoC 계획
- 도입하지 말아야 할 경우
- 다음 액션 아이템

중요:
- 추측하지 말고 확인된 정보와 추론을 구분해 주세요.
- 보안/비용/벤더 종속성은 별도 섹션으로 분리해 주세요.
```

---

## Prompt 02. Pi 기반 실험실 설계 프롬프트

```markdown
당신은 AI Coding Agent Lab을 설계하는 소프트웨어 아키텍트입니다.

나는 Pi를 기반으로 AI 코딩 에이전트 실험실을 만들고 싶습니다.
목표는 단순히 Pi를 설치하는 것이 아니라, 여러 AI 코딩 도구의 장점을 분석해서 나만의 개발 워크플로우를 만드는 것입니다.

요구사항:
1. Mac 환경을 기준으로 합니다.
2. Java/Spring Boot 프로젝트를 주요 대상으로 합니다.
3. Cursor, Claude Code, Codex CLI, Aider와 함께 비교 실험할 수 있어야 합니다.
4. 실제 회사 코드가 아니라 샘플 프로젝트에서 먼저 실험합니다.
5. 파일 수정, bash 실행, 네트워크 접근, secret 접근에 대한 안전 정책이 있어야 합니다.
6. 실험 결과를 markdown으로 남길 수 있어야 합니다.
7. 나중에는 MCP, GitHub PR 체크, 자동 문서화까지 확장하고 싶습니다.

산출물:
- 디렉터리 구조
- README.md 초안
- AGENTS.md 초안
- allowed command / denied command 정책
- 첫 번째 실험 시나리오 5개
- 성공/실패 평가 기준
- 2주 PoC 일정

제약:
- 회사 코드나 민감 정보는 사용하지 않습니다.
- destructive command는 기본 금지합니다.
- 모든 자동 수정은 git diff로 검토 가능해야 합니다.
```

---

## Prompt 03. AGENTS.md 생성 프롬프트

```markdown
당신은 이 저장소를 위한 AGENTS.md를 작성하는 AI 개발 운영 설계자입니다.

목표:
AI 코딩 에이전트가 이 저장소에서 안전하고 일관되게 작업하도록 프로젝트 규칙을 문서화합니다.

분석할 항목:
1. 프로젝트 목적
2. 주요 기술 스택
3. 디렉터리 구조
4. 빌드 명령
5. 테스트 명령
6. 로컬 실행 명령
7. 코드 스타일
8. 아키텍처 규칙
9. 금지해야 할 작업
10. 민감 정보 취급 규칙
11. PR 생성 전 체크리스트
12. 장애 가능성이 큰 변경 유형

작성 형식:
# AGENTS.md
## Project Overview
## Tech Stack
## Directory Structure
## Build and Test Commands
## Coding Rules
## Architecture Rules
## Security Rules
## Forbidden Actions
## Review Checklist
## Agent Operating Procedure

중요 규칙:
- 실제 파일을 먼저 읽고 추측하지 마세요.
- 명령어가 확실하지 않으면 “확인 필요”로 표시하세요.
- rm -rf, credential 출력, .env 노출, 운영 DB 접근은 금지 작업으로 명시하세요.
- Java/Spring Boot 프로젝트라면 Transaction, JPA, API 응답, 예외 처리, 테스트 규칙을 포함하세요.
```

---

## Prompt 04. Pi Extension / Skill 설계 프롬프트

```markdown
당신은 Pi 기반 custom skill/extension을 설계하는 TypeScript 개발자입니다.

목표:
Spring Boot 프로젝트의 코드 리뷰를 자동화하는 Pi skill 또는 extension을 설계합니다.

기능 요구사항:
1. 변경된 파일 목록을 읽습니다.
2. Java/Kotlin/Spring 관련 파일을 우선 분석합니다.
3. Controller, Service, Repository, Entity, DTO를 구분합니다.
4. 다음 항목을 점검합니다.
   - Transaction 범위
   - JPA N+1 위험
   - 잘못된 lazy loading 사용
   - Controller에 비즈니스 로직 존재 여부
   - 예외 처리 일관성
   - API 응답 포맷 일관성
   - 테스트 누락
   - 민감 정보 로그 출력
5. 결과를 markdown 리포트로 출력합니다.
6. 자동 수정은 하지 않고, 제안 diff만 생성합니다.

산출물:
- skill/extension 아키텍처
- 입력/출력 인터페이스
- 내부 단계별 알고리즘
- 필요한 Pi API 또는 tool 호출 방식
- 샘플 프롬프트 템플릿
- 테스트 전략
- 보안상 주의점

제약:
- destructive command 금지
- 외부 네트워크 호출은 기본 금지
- secret 파일은 읽지 않음
- 모든 제안은 사람이 검토한 뒤 적용
```

---

## Prompt 05. 안전한 실행 정책 설계 프롬프트

```markdown
당신은 AI 코딩 에이전트 보안 아키텍트입니다.

Pi 또는 기타 CLI 기반 AI 코딩 에이전트를 사용할 때 필요한 실행 정책을 설계해 주세요.

상황:
- 에이전트는 파일을 읽고 쓸 수 있습니다.
- bash 명령을 실행할 수 있습니다.
- git 명령을 사용할 수 있습니다.
- 테스트 명령을 실행할 수 있습니다.
- 실수로 credential, .env, SSH key, 운영 DB 접속정보에 접근하면 안 됩니다.

작성할 문서:
1. Risk Model
2. Allowed Commands
3. Denied Commands
4. File Access Policy
5. Network Access Policy
6. Secret Handling Policy
7. Git Safety Policy
8. Review-before-apply Policy
9. Sandbox/Docker 실행 패턴
10. 사고 발생 시 복구 절차

반드시 포함할 금지 예시:
- rm -rf /
- rm -rf .git
- git push --force
- cat ~/.ssh/*
- cat .env
- printenv
- aws secretsmanager get-secret-value
- kubectl delete
- terraform destroy
- 운영 DB에 직접 write하는 명령

결과는 `policies/security-checklist.md`로 저장할 수 있는 형태로 작성해 주세요.
```

---

## Prompt 06. 도구 비교 실험 프롬프트

```markdown
당신은 AI 코딩 도구 벤치마크를 설계하는 평가자입니다.

다음 도구를 동일한 샘플 프로젝트에서 비교하려고 합니다.
- Pi
- Claude Code
- Codex CLI
- Aider
- Cline
- Cursor

샘플 프로젝트:
- Spring Boot REST API
- JPA 사용
- MySQL 사용
- 간단한 User/Order 도메인
- 의도적으로 N+1 문제, 테스트 누락, 예외 처리 불일치, DTO 누락을 포함

각 도구에 동일한 작업을 시킵니다.

작업 목록:
1. 프로젝트 구조 설명
2. 버그 찾기
3. N+1 문제 수정 제안
4. 테스트 추가
5. API 응답 구조 개선
6. README 업데이트
7. PR 설명 작성

평가 기준:
- 정확성
- 수정 범위 통제
- 테스트 생성 품질
- 설명 품질
- git diff 품질
- 불필요한 변경 여부
- 보안 위험 행동 여부
- 재현 가능성

산출물:
- 평가표
- 점수 기준
- 실험 기록 템플릿
- 최종 추천
```

---

## Prompt 07. Java/Spring Boot 실무 작업 프롬프트

```markdown
당신은 20년차 Java/Spring Boot Staff Engineer처럼 행동해 주세요.

작업 목표:
현재 Spring Boot 프로젝트의 특정 기능을 안전하게 개선합니다.

진행 방식:
1. 먼저 관련 파일을 읽고 구조를 설명합니다.
2. 변경 계획을 제안합니다.
3. 변경 범위를 작게 유지합니다.
4. public API 변경 여부를 명시합니다.
5. DB schema 변경이 필요한 경우 migration 전략을 제안합니다.
6. 테스트를 먼저 확인하고, 없으면 테스트를 추가합니다.
7. 변경 후 실행해야 할 명령을 제안합니다.
8. 마지막에 git diff 기준으로 리뷰 포인트를 요약합니다.

코딩 기준:
- Controller에는 비즈니스 로직을 두지 않습니다.
- Service는 transaction boundary를 명확히 합니다.
- Entity를 API 응답으로 직접 노출하지 않습니다.
- Repository query는 N+1 가능성을 검토합니다.
- 예외는 일관된 ErrorResponse로 변환합니다.
- 테스트는 단위 테스트와 통합 테스트를 구분합니다.

출력 형식:
## 구조 분석
## 변경 계획
## 수정 대상 파일
## 구현 내용
## 테스트 계획
## 위험 요소
## 리뷰 체크리스트
```

---

## Prompt 08. PR 리뷰 자동화 프롬프트

```markdown
당신은 매우 엄격하지만 실용적인 Staff Engineer 코드 리뷰어입니다.

대상:
현재 브랜치의 변경사항 또는 제공된 diff를 리뷰합니다.

리뷰 기준:
1. 기능 요구사항 충족 여부
2. 변경 범위가 과도하지 않은지
3. 테스트 누락 여부
4. 예외 처리 일관성
5. 트랜잭션 경계 적절성
6. 성능 문제 가능성
7. 보안 문제 가능성
8. 운영 리스크
9. 로그 품질
10. 롤백 가능성

리뷰 스타일:
- 사소한 취향 문제는 낮은 우선순위로 둡니다.
- 장애를 만들 수 있는 문제는 강하게 지적합니다.
- 수정 방향을 구체적으로 제시합니다.
- “무조건 고쳐라”가 아니라 위험 수준을 표시합니다.

출력 형식:
## 요약
## 반드시 수정해야 할 사항
## 수정 권장 사항
## 질문 사항
## 테스트 보강 제안
## 운영 배포 전 체크리스트
## 승인 여부

승인 여부는 다음 중 하나로 표시합니다.
- APPROVE
- COMMENT
- REQUEST_CHANGES
```

---

## Prompt 09. Continue 스타일 PR Check 프롬프트

아래는 `.continue/checks/spring-security-review.md` 같은 파일로도 응용할 수 있는 형태입니다.

```markdown
---
name: Spring Security and Maintainability Review
summary: Spring Boot PR의 보안, 유지보수성, 트랜잭션, 테스트 누락을 점검합니다.
---

Review this pull request for Spring Boot backend risks.

Fail this check if any of the following are true:
- New API endpoint has no input validation.
- Controller contains business logic that should be in a service.
- Entity is directly returned as API response.
- SQL or JPQL is built through unsafe string concatenation.
- Sensitive data is logged.
- Transactional boundary is missing for write operations.
- N+1 query risk is introduced without mitigation.
- Error response format is inconsistent with the existing project style.
- Important behavior is changed without tests.

If issues are found:
1. Explain the issue.
2. Point to the relevant file and method.
3. Explain the production risk.
4. Suggest the smallest safe fix.

If no issues are found, pass the check and summarize why.
```

---

## Prompt 10. MCP 연동 설계 프롬프트

```markdown
당신은 MCP 기반 개발 자동화 아키텍트입니다.

목표:
Pi 또는 다른 AI 코딩 에이전트에서 MCP를 사용해 개발 업무를 확장하려고 합니다.

연동하고 싶은 도구:
- GitHub
- Jira 또는 Linear
- Confluence 또는 Notion
- Local filesystem
- Database read-only query
- Browser automation
- Internal API documentation

설계할 내용:
1. 어떤 MCP 서버가 필요한지
2. 각 MCP 서버의 권한 범위
3. read-only와 write 권한 분리
4. secret 관리 방식
5. audit log 방식
6. 에이전트가 해도 되는 일과 하면 안 되는 일
7. 실제 개발 workflow 예시
8. 장애 또는 오작동 시 차단 방법

결과 형식:
- MCP 아키텍처 다이어그램을 텍스트로 설명
- 권한 매트릭스
- 사용 시나리오 5개
- 보안 체크리스트
- PoC 순서
```

---

## Prompt 11. Context Engineering 프롬프트

```markdown
당신은 AI 코딩 에이전트를 위한 Context Engineering 전문가입니다.

목표:
에이전트가 코드베이스를 더 정확하게 이해하도록 context 전략을 설계합니다.

분석할 것:
1. 어떤 파일을 항상 읽어야 하는지
2. 어떤 파일은 필요할 때만 읽어야 하는지
3. 어떤 파일은 절대 읽으면 안 되는지
4. AGENTS.md에 넣을 내용과 넣지 않을 내용
5. README, ADR, API 문서, DB schema, 테스트 파일의 우선순위
6. context bloat를 줄이는 방법
7. 오래된 문서와 최신 코드가 충돌할 때 판단 기준
8. 작업별 context template

산출물:
- context map
- always-read files
- on-demand files
- forbidden files
- task-specific prompt template
- context refresh rule
```

---

## Prompt 12. 실험 기록 템플릿 생성 프롬프트

```markdown
당신은 AI 코딩 도구 실험 기록을 남기는 연구원입니다.

다음 실험을 markdown으로 기록할 템플릿을 만들어 주세요.

실험 대상 도구:
[도구명]

작업:
[예: Spring Boot N+1 문제 수정]

기록할 항목:
1. 실험 목적
2. 입력 프롬프트
3. 사용 모델
4. 실행 환경
5. 에이전트가 읽은 주요 파일
6. 에이전트가 수정한 파일
7. 생성된 diff 요약
8. 테스트 실행 결과
9. 잘한 점
10. 위험했던 점
11. 사람이 개입한 부분
12. 다음 실험에서 바꿀 점
13. 최종 점수

점수 기준:
- 정확성: 1~5
- 변경 통제: 1~5
- 테스트 품질: 1~5
- 설명 품질: 1~5
- 안전성: 1~5

결과는 `experiments/YYYY-MM-DD-tool-task.md`로 저장할 수 있게 작성해 주세요.
```

---

## Prompt 13. “나만의 AI 개발 에이전트” 제품화 프롬프트

```markdown
당신은 AI 개발 도구 제품 기획자이자 소프트웨어 아키텍트입니다.

목표:
Pi를 기반으로 “나만의 AI 개발 에이전트”를 만들려고 합니다.

제품 컨셉:
- Java/Spring Boot 개발자를 위한 로컬 AI 코딩 에이전트
- 코드 리뷰, 테스트 생성, 리팩토링, 문서화, PR 설명 작성을 지원
- 회사 코드에 적용하기 전 로컬 샘플 프로젝트에서 검증
- 나중에는 팀 표준 도구로 확장 가능

기획해 주세요:
1. 제품명 후보 10개
2. 핵심 사용자 문제
3. MVP 기능
4. 제외할 기능
5. 사용자 흐름
6. 기술 아키텍처
7. Pi를 활용할 부분
8. 외부 도구와 비교한 차별점
9. 보안 정책
10. 4주 개발 로드맵
11. 성공 지표
12. 실패 가능성과 대응책

출력 형식:
# Product Brief
# MVP Scope
# Architecture
# Roadmap
# Risk
# Next Actions
```

---

## Prompt 14. 코드 수정 전 “계획만 세우기” 프롬프트

```markdown
지금은 코드를 수정하지 마세요.
먼저 계획만 세워 주세요.

작업 목표:
[여기에 목표 입력]

반드시 지켜야 할 규칙:
1. 파일을 수정하지 않습니다.
2. 명령을 실행하더라도 read-only 명령만 사용합니다.
3. 관련 파일을 조사합니다.
4. 변경해야 할 파일 후보를 나열합니다.
5. 위험도를 평가합니다.
6. 테스트 전략을 제시합니다.
7. 사람이 승인해야 다음 단계로 넘어갑니다.

출력 형식:
## 현재 구조 이해
## 변경 목표 재정의
## 수정 후보 파일
## 변경 계획
## 테스트 계획
## 위험도
## 승인 요청
```

---

## Prompt 15. “작게 수정하고 검증하기” 프롬프트

```markdown
이제 승인된 계획에 따라 최소 변경만 수행해 주세요.

규칙:
1. 한 번에 큰 리팩토링을 하지 않습니다.
2. public API 변경은 사전에 명시합니다.
3. 기존 테스트가 깨지지 않게 합니다.
4. 변경 후 실행해야 할 테스트 명령을 제안합니다.
5. 수정한 파일과 이유를 요약합니다.
6. 다음 개선은 별도 단계로 분리합니다.

출력 형식:
## 수행한 변경
## 수정 파일
## 변경 이유
## 실행할 테스트
## 예상 리스크
## 다음 단계
```

---

# 4. 추천 첫 실험 시나리오

## 실험 1. Pi로 AGENTS.md 만들기

목표: 샘플 Spring Boot 프로젝트를 분석해서 AGENTS.md를 생성합니다.

사용 프롬프트:
- Prompt 03
- Prompt 11

성공 기준:
- 빌드/테스트 명령이 정확하다.
- forbidden action이 명확하다.
- Spring Boot/JPA 규칙이 포함된다.
- 추측한 부분은 “확인 필요”로 표시한다.

---

## 실험 2. Pi vs Aider 변경 품질 비교

목표: 같은 N+1 문제를 Pi와 Aider에게 각각 수정시켜 diff 품질을 비교합니다.

사용 프롬프트:
- Prompt 06
- Prompt 07
- Prompt 12

성공 기준:
- 변경 파일 수가 최소화된다.
- 테스트가 추가된다.
- 설명이 명확하다.
- 불필요한 스타일 변경이 없다.

---

## 실험 3. Claude Code/Codex CLI와 UX 비교

목표: Pi가 부족한 점과 강한 점을 체감합니다.

평가 항목:
- 계획 수립 능력
- 파일 탐색 방식
- 명령 실행 승인 UX
- diff 리뷰 UX
- 테스트 실패 후 회복 능력
- context 유지 능력

---

## 실험 4. Continue 스타일 PR Check 만들기

목표: AI 코딩 결과를 사람이 병합하기 전에 자동 점검하는 markdown check를 만듭니다.

사용 프롬프트:
- Prompt 09
- Prompt 08

---

## 실험 5. Pi Skill 또는 Extension 설계

목표: Spring Boot 코드 리뷰 스킬을 설계하고 작은 기능부터 구현합니다.

사용 프롬프트:
- Prompt 04
- Prompt 05

---

# 5. 권장 작업 순서

## Day 1: 도구 설치와 샘플 프로젝트 준비

1. Pi 설치
2. Claude Code 또는 Codex CLI 중 하나 설치
3. Aider 설치
4. 샘플 Spring Boot 프로젝트 생성
5. git 초기화
6. 실험 기록 폴더 생성

## Day 2: AGENTS.md 만들기

1. Prompt 03 실행
2. Prompt 11 실행
3. 사람이 AGENTS.md 검토
4. 금지 명령 추가
5. 첫 실험 기록 작성

## Day 3~4: 같은 작업을 여러 도구에 시켜보기

1. N+1 문제 찾기
2. 테스트 추가
3. 예외 처리 개선
4. README 업데이트
5. diff 비교

## Day 5: 보안 정책 정리

1. Prompt 05 실행
2. allowed/denied command 문서 작성
3. sandbox 실행 방식 검토

## Week 2: Pi 기반 확장 개발

1. Prompt 04로 skill 설계
2. 작은 markdown report 기능부터 구현
3. PR check prompt 작성
4. MCP 연동 후보 정리

---

# 6. 참고 링크

- Pi 공식 사이트: https://pi.dev/
- Pi GitHub: https://github.com/earendil-works/pi
- Claude Code 공식 페이지: https://claude.com/product/claude-code
- Claude Code GitHub: https://github.com/anthropics/claude-code
- OpenAI Codex CLI: https://developers.openai.com/codex/cli
- GitHub Copilot CLI: https://github.com/features/copilot/cli
- Aider: https://aider.chat/
- Cline: https://cline.bot/
- Goose: https://goose-docs.ai/
- Continue Docs: https://docs.continue.dev/
- OpenCode GitHub: https://github.com/opencode-ai/opencode
- Gemini CLI: https://developers.google.com/gemini-code-assist/docs/gemini-cli
- Qwen Code: https://qwen.ai/qwencode
- Cursor: https://cursor.com/
- Devin: https://devin.ai/

## 연구 참고

- AIDev: Studying AI Coding Agents on GitHub: https://arxiv.org/abs/2602.09185
- Configuring Agentic AI Coding Tools: https://arxiv.org/abs/2602.14690
- Building Effective AI Coding Agents for the Terminal: https://arxiv.org/abs/2603.05344
- Dive into Claude Code: https://arxiv.org/abs/2604.14228
- On the Use of Agentic Coding: https://arxiv.org/abs/2509.14745

---

# 7. 마지막 판단

Pi를 단순히 “또 하나의 AI 코딩 도구”로 보면 매력이 덜합니다. 하지만 **내가 직접 AI 개발 하네스를 만들기 위한 기반**으로 보면 꽤 흥미롭습니다.

장회수님께 가장 좋은 활용법은 다음입니다.

1. Cursor/Claude Code는 실무 생산성 도구로 계속 사용합니다.
2. Pi는 내부 구조 학습과 커스텀 자동화 실험에 사용합니다.
3. Aider는 Git 기반 편집 품질 비교 대상으로 둡니다.
4. Continue는 PR 품질 게이트 아이디어로 참고합니다.
5. Cline/Goose는 MCP와 범용 자동화 UX를 참고합니다.
6. 최종적으로는 `AGENTS.md + Prompt Pack + Security Policy + PR Check + Pi Skill` 조합을 만듭니다.

이 방향이면 단순히 도구를 소비하는 수준을 넘어, AI 개발 도구를 직접 설계하는 단계로 넘어갈 수 있습니다.
