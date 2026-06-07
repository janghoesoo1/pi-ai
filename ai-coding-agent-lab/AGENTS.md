# AGENTS.md

AI 코딩 에이전트가 이 저장소에서 작업할 때 따라야 할 규칙.
실제 파일을 먼저 읽고, 추측하지 않으며, 최소 변경만 수행한다.

---

## Project Overview

AI 코딩 에이전트 실험실. Pi를 기반으로 여러 AI 코딩 도구를 비교하고, 커스텀 개발 워크플로우를 만드는 프로젝트.

목적:
- AI 코딩 에이전트의 내부 구조를 이해한다.
- 내 개발 워크플로우에 맞춘 커스텀 에이전트/스킬/프롬프트 템플릿을 만든다.
- Claude Code, Codex CLI, Aider, Cline, Goose, Continue 같은 외부 도구를 비교하면서 좋은 설계 패턴을 흡수한다.

중요: 이 실험실은 회사 코드가 아닌 샘플 프로젝트를 대상으로 한다.

---

## Tech Stack

실험 대상 (backend):
- Kotlin (JVM 17+)
- Spring Boot 3.x
- JPA / Hibernate
- H2 (기본 인메모리 프로파일, `spring.profiles.active: h2`) / MySQL (선택 프로파일)

실험 대상 (frontend):
- Next.js (React 18+)
- TypeScript

AI 도구:
- Pi
- Claude Code
- OpenAI Codex CLI
- Aider
- Cline
- Cursor

---

## Directory Structure

| 경로 | 역할 |
|------|------|
| `prompts/` | 실험에 사용하는 프롬프트 템플릿 모음 |
| `sandbox/` | 실험용 샘플 프로젝트. 회사 코드 절대 금지 |
| `sandbox/sample-spring-api/` | Spring Boot REST API 샘플 프로젝트 |
| `sandbox/sample-react-app/` | React 프론트엔드 샘플 프로젝트 |
| `experiments/` | 실험 결과 기록. 형식: `YYYY-MM-DD-tool-task.md` |
| `policies/` | 허용/금지 명령, 보안 정책 문서 |

---

## Build and Test Commands

> ⚠️ 현재 `sandbox/sample-spring-api`에는 gradle wrapper(`gradlew`/`gradle/wrapper/*.jar`)가 포함돼 있지 않다.
> 아래 명령 실행 전 `gradle wrapper`로 래퍼를 먼저 생성해야 한다(시스템 gradle 필요). `mvnw`도 없음.

```bash
# (최초 1회) gradle wrapper 생성
gradle wrapper

# 빌드 (sandbox/sample-spring-api/)
./gradlew build

# 테스트
./gradlew test

# 실행
./gradlew bootRun

# React (sandbox/sample-react-app/)
npm install
npm run dev
```

---

## Coding Rules

### 공통
- 변경 전 관련 파일을 반드시 읽는다. 추측으로 코드를 작성하지 않는다.
- 변경 범위를 최소화한다. 필요하지 않은 리팩토링을 같이 하지 않는다.
- 모든 자동 수정은 git diff로 검토 가능해야 한다.

### Spring Boot / Kotlin
- Controller에 비즈니스 로직을 두지 않는다.
- Entity를 API 응답으로 직접 노출하지 않는다. DTO(data class)를 사용한다.
- Service는 transaction boundary를 명확히 한다.
- Repository query는 N+1 가능성을 검토한다.
- 예외는 일관된 ErrorResponse로 변환한다.
- 단위 테스트와 통합 테스트를 구분한다.
- 민감 정보를 로그에 출력하지 않는다.
- nullable 타입을 명시적으로 관리한다. `!!` 남용 금지.
- data class를 적극 활용한다 (DTO, 값 객체).

---

## Architecture Rules

### 계층 분리
```
Controller -> Service -> Repository
```
- Controller: 요청 수신, 입력 검증, 응답 변환만 담당
- Service: 비즈니스 로직, transaction 경계 관리
- Repository: 데이터 접근만 담당

### DTO 패턴
- Request DTO: 입력 검증 포함
- Response DTO: Entity 직접 노출 금지
- 계층 간 데이터 전달에 DTO 사용

### API 응답 구조 일관성
- 성공/실패 모두 동일한 응답 포맷 사용
- 에러는 일관된 ErrorResponse 구조로 반환

---

## Security Rules

- credential, .env, SSH key, 운영 DB 접속정보에 접근하지 않는다.
- 민감 정보를 로그에 출력하지 않는다.
- SQL 문자열 연결(concatenation)이나 string template으로 쿼리를 만들지 않는다. JPA 또는 parameterized query를 사용한다.
- 새 API endpoint에는 반드시 입력 검증을 추가한다.
- 실험 대상은 sandbox/ 내 샘플 프로젝트로 한정한다. 회사 코드/운영 환경에 접근하지 않는다.

---

## Forbidden Actions

> 전체·최신 금지 목록은 `policies/denied-commands.md`가 정본(canonical). 아래는 핵심 요약.

다음 명령은 기본 금지다. 사람의 명시적 승인 없이 실행하지 않는다.

```bash
# 파일 시스템 파괴
rm -rf /
rm -rf .git

# Git 히스토리 재작성
git push --force

# 민감 정보 노출
cat ~/.ssh/*
cat .env
printenv

# 클라우드 인프라 파괴
aws secretsmanager get-secret-value
kubectl delete
terraform destroy

# 운영 DB 직접 write
# (운영 DB 접속 자체를 금지)
```

추가로 다음 패턴도 금지한다:
- 운영 환경 변수를 읽는 모든 명령
- 외부 네트워크에 데이터를 전송하는 명령 (명시적 허용 제외)
- sandbox/ 외부 프로젝트 파일 수정

---

## Review Checklist

코드 변경 후 PR 또는 커밋 전 체크:

- [ ] 기능 요구사항을 충족하는가
- [ ] 변경 범위가 최소화되었는가 (불필요한 리팩토링 없음)
- [ ] 변경된 로직에 대한 테스트가 존재하는가
- [ ] 예외 처리가 기존 프로젝트 스타일과 일관되는가
- [ ] Transaction 경계가 적절한가
- [ ] 보안 이슈가 없는가 (민감 정보 노출, SQL injection 등)
- [ ] 운영 리스크가 없는가 (N+1, 메모리 누수, 무한 루프 등)
- [ ] 금지 명령이 포함되지 않았는가

---

## Autonomy Levels

작업별 자율성 레벨. 레벨이 낮을수록 사람 개입이 많다.

| 레벨 | 설명 | 예시 |
|------|------|------|
| L1 | 사람 전용 | 아키텍처 결정, MCP 설계, 보안 정책 수립 |
| L2 | AI 준비 + 사람 승인 | PR 리뷰, 보안 점검, 도구 비교 벤치마크 |
| L3 | AI 실행 + 사람 감독 | 코드 분석, 테스트 생성, N+1 탐지, 실험 기록 |
| L4 | 한계 안에서 자율 | 린트, 포맷팅, 빌드 검증 |

규칙:
- L2 이하 작업은 결과를 사람이 승인한 뒤에만 적용한다.
- L4 작업이라도 `policies/denied-commands.md`의 금지 명령은 실행하지 않는다.
- 자율성 레벨을 올리려면 수용률 70% 이상을 4주 연속 달성해야 한다.

---

## Agent Operating Procedure

1. **관련 파일을 먼저 읽는다.** 구조를 파악하지 않고 추측으로 코드를 작성하지 않는다.
2. **변경 계획을 먼저 제안한다.** 사람의 승인 후에 실행한다.
3. **최소 변경만 수행한다.** 요청 범위를 벗어난 수정을 하지 않는다.
4. **모든 자동 수정은 git diff로 검토 가능해야 한다.** 검토 불가능한 bulk 수정을 하지 않는다.
5. **destructive command는 기본 금지다.** Forbidden Actions 목록을 항상 확인한다.
6. **명령어가 확실하지 않으면 "확인 필요"로 표시한다.** 추측으로 명령을 실행하지 않는다.
7. **실험 결과는 `experiments/` 디렉토리에 기록한다.** 형식: `YYYY-MM-DD-tool-task.md`

### Harness 6단계

모든 작업은 다음 6단계를 거친다.

1. **Preflight** -- 토큰 쓰기 전 `AGENTS.md`와 `policies/` 로드. 금지 명령 확인.
2. **Plan** -- 변경 계획 수립. `prompts/14-plan-only.md` 참조.
3. **Approve** -- 사람이 계획 검토 후 승인. L1/L2 작업은 반드시 승인 필요.
4. **Execute** -- 최소 변경 실행. `prompts/15-minimal-change.md` 참조.
5. **Verify** -- 빌드/테스트 통과 확인. PR 리뷰 실행.
6. **Log** -- `experiments/`에 결과 기록. `context/decisions.md`에 결정 추가.
