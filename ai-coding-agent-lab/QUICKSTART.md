# AI Coding Agent Lab 활용 가이드

이 실험실을 실제로 어떻게 쓰는지에 대한 가이드.

---

## 현재 상태

- 실험실 구조, 프롬프트 17개, 샘플 프로젝트 2개, 정책 3개, 운영 가이드 -- 모두 준비 완료
- **다음 할 일: 실험 실행**

---

## 활용법 1: 프롬프트를 AI 도구에 복붙해서 쓴다

가장 기본적인 활용법. `prompts/` 파일을 열어 내용을 복사한 뒤, 사용하는 AI 도구에 붙여넣는다.

### 바로 쓸 수 있는 프롬프트 (도구 무관)

| 상황 | 프롬프트 | 사용법 |
|------|---------|--------|
| Spring Boot 코드를 개선하고 싶다 | `07-spring-work.md` | 프롬프트를 복사해서 Claude Code/Cursor/Aider에 입력. 대상 프로젝트 경로 지정 |
| PR 올리기 전 리뷰 받고 싶다 | `08-pr-review.md` | `git diff`와 함께 프롬프트 입력. 변경사항 리뷰 받기 |
| 코드 수정 전 계획만 세우고 싶다 | `14-plan-only.md` | 프롬프트에 작업 목표를 채워 입력. 코드 수정 없이 계획만 받기 |
| 최소한만 고치고 싶다 | `15-minimal-change.md` | 14번으로 계획 받은 뒤, 15번으로 실행 |
| 프로젝트에 AGENTS.md를 만들고 싶다 | `03-agents-md-generator.md` | 자기 프로젝트 루트에서 프롬프트 입력 |
| 보안 정책을 정리하고 싶다 | `05-security-policy.md` | 프롬프트 입력하면 policies/ 형태의 문서 생성 |

### 사용 예시

```bash
# Claude Code에서 사용하는 경우
cd sandbox/sample-spring-api
# 프롬프트 파일을 @로 참조
@prompts/07-spring-work.md

# 또는 직접 복사해서 입력
cat prompts/07-spring-work.md | pbcopy
# -> AI 도구에 붙여넣기
```

```bash
# Aider에서 사용하는 경우
cd sandbox/sample-spring-api
aider --message-file ../prompts/07-spring-work.md
```

```bash
# Cursor에서 사용하는 경우
# prompts/ 파일을 열어 내용 복사 -> Composer에 붙여넣기
```

---

## 활용법 2: sandbox 프로젝트로 도구를 비교한다

`sandbox/sample-spring-api`에는 의도적으로 7가지 문제가 들어있다.
같은 문제를 여러 AI 도구에게 시켜보고 결과를 비교한다.

### 실험 순서

#### 1단계: 문제 발견 실험

각 도구에게 `prompts/07-spring-work.md` 프롬프트를 주고 "이 프로젝트의 문제를 찾아줘"라고 요청한다.

비교 기준:
- 7가지 문제 중 몇 개를 발견하는가
- 잘못된 문제를 지적하지는 않는가
- 우선순위를 올바르게 매기는가

| # | 의도된 문제 | 찾았는가 |
|---|-----------|---------|
| 1 | N+1 쿼리 (UserService.getAllUsersWithOrders) | |
| 2 | 테스트 누락 (Service 테스트 없음) | |
| 3 | 예외 처리 불일치 (RuntimeException vs ErrorResponse 혼용) | |
| 4 | DTO 미사용 (Entity 직접 API 노출) | |
| 5 | Controller 비즈니스 로직 (UserController.deleteUser) | |
| 6 | Transaction 누락 (일부 메서드만 @Transactional) | |
| 7 | 민감 정보 로그 (이메일 INFO 출력) | |

#### 2단계: 수정 실험

각 도구에게 "N+1 문제를 수정해줘"라고 요청한다.

비교 기준:
- 수정이 정확한가
- 변경 파일 수가 최소인가
- 테스트를 함께 추가하는가
- 불필요한 리팩토링을 하지 않는가

#### 3단계: 기록

`experiments/` 디렉토리에 결과를 기록한다. 템플릿은 `prompts/12-experiment-template.md` 참조.

```bash
# 파일명 형식
experiments/2026-06-05-claudecode-n1-fix.md
experiments/2026-06-05-aider-n1-fix.md
experiments/2026-06-05-cursor-n1-fix.md
```

---

## 활용법 3: 자기 프로젝트에 적용한다

실험실에서 검증된 프롬프트를 실제 프로젝트에 사용한다.

### 적용 순서

```
1. AGENTS.md 생성     <- prompts/03-agents-md-generator.md
2. 보안 정책 정리      <- prompts/05-security-policy.md
3. 코드 리뷰 자동화    <- prompts/08-pr-review.md + 09-pr-check.md
4. MCP 연동 설계      <- prompts/10-mcp-design.md
5. 커스텀 스킬 개발    <- prompts/04-spring-review-skill.md
```

### 예시: 자기 프로젝트에 AGENTS.md 만들기

```bash
cd ~/work/my-real-project

# Claude Code에서
# prompts/03-agents-md-generator.md 내용을 입력
# -> AI가 프로젝트를 분석해서 AGENTS.md 생성
# -> 사람이 검토 후 수정
```

### 예시: PR 리뷰 자동화

```bash
cd ~/work/my-real-project
git diff main...HEAD > /tmp/diff.txt

# prompts/08-pr-review.md + diff를 AI 도구에 입력
# -> 리뷰 결과 받기
# -> APPROVE / COMMENT / REQUEST_CHANGES 판단
```

---

## 활용법 4: 운영 체계를 만든다

프롬프트를 넘어, 팀/개인의 AI 코딩 운영 체계를 설계한다.

### 핵심 문서 3개

| 문서 | 역할 | 언제 읽는가 |
|------|------|------------|
| `AGENTS.md` | 에이전트 규칙 | 매 작업 시작 시 |
| `OPERATING-GUIDE.md` | 운영 프레임워크 | 주간 리뷰 시 |
| `policies/security-checklist.md` | 보안 가드레일 | 커밋/배포 전 |

### 주간 루프

매주 금요일, 15분 투자:

```
1. 이번 주 어떤 AI 도구로 어떤 작업을 했는가?
2. AI가 만든 결과를 그대로 쓴 비율은? (수용률)
3. 직접 고친 부분은 왜 고쳤는가?
4. context/ 파일에 새로 배운 것을 기록
5. 다음 주 실험 계획
```

이 루프가 쌓이면 "어떤 작업은 AI에게 맡기고, 어떤 작업은 직접 하는 것이 효율적인가"에 대한 자기만의 답이 만들어진다.

---

## 활용법 5: 제품으로 발전시킨다

`prompts/13-product-design.md`를 사용해 "나만의 AI 개발 에이전트"를 기획한다.

발전 경로:

```
실험실 (현재)
  -> 검증된 프롬프트 + 정책 모음
  -> Pi 기반 커스텀 Skill
  -> MCP 연동 자동화
  -> 팀 표준 도구
  -> 오픈소스 또는 내부 제품
```

---

## 지금 바로 해볼 것

### 옵션 A: 5분 체험

```bash
cd ai-coding-agent-lab/sandbox/sample-spring-api

# 사용 중인 AI 도구에 아래 프롬프트 입력:
#
# "당신은 20년차 Java/Spring Boot Staff Engineer입니다.
#  이 프로젝트의 구조를 분석하고 문제점을 찾아주세요.
#  수정하지 말고 발견만 해주세요."
#
# -> 7가지 의도된 문제 중 몇 개를 찾는지 확인
```

### 옵션 B: 30분 실험

1. `prompts/07-spring-work.md`를 Claude Code에 입력
2. "N+1 문제를 수정해줘"라고 추가 요청
3. `git diff`로 변경 내용 확인
4. `experiments/` 에 결과 기록
5. 같은 작업을 Aider나 Cursor에서 반복
6. 점수를 매기고 비교

### 옵션 C: 실무 적용

1. 자기 프로젝트에서 `prompts/03-agents-md-generator.md` 실행
2. 생성된 AGENTS.md 검토 및 수정
3. `prompts/08-pr-review.md`로 최근 PR 리뷰
4. 결과를 `context/tool-insights.md`에 기록

---

## 파일 안내 (전체 구조)

```
ai-coding-agent-lab/
  README.md                  <- 실험실 전체 안내
  AGENTS.md                  <- 에이전트 운영 규칙 + 자율성 레벨 + 하네스
  OPERATING-GUIDE.md         <- AI-네이티브 6단계 운영 프레임워크
  QUICKSTART.md              <- 이 문서 (활용 가이드)

  prompts/                   <- 17개 프롬프트 (AI 도구에 복붙해서 사용)
    00-research.md           <- 도구 비교표 (참고)
    01~15                    <- 실행 가능한 프롬프트
    16-ai-native-startup-playbook.md <- 프레임워크 참고

  sandbox/                   <- 실험용 코드 (의도적 문제 포함)
    sample-spring-api/       <- Spring Boot (7가지 문제)
    sample-react-app/        <- Next.js

  experiments/               <- 실험 결과 기록
  policies/                  <- 보안 정책
  context/                   <- 운영 기억 (학습 누적)
```
