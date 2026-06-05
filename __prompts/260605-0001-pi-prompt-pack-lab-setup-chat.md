# Pi 기반 AI 코딩 에이전트 실험실 구조 생성

- 날짜: 2026-06-05
- 타입: chat
- 작업: pi_based_ai_coding_agent_prompt_pack.md를 기반으로 실험실 디렉토리 구조와 파일 생성

## 사용자 요청

`@pi_based_ai_coding_agent_prompt_pack.md` 이 프롬프트를 입력으로 만들어봐

## AI 작업 내용

1. 원본 프롬프트 팩 문서 분석
2. 문서 섹션 2.1의 디렉토리 구조를 기반으로 실험실 설계
3. 병렬 에이전트 6개를 디스패치하여 파일 생성

## 생성된 구조

```
ai-coding-agent-lab/
  README.md                          # 실험실 안내
  AGENTS.md                          # AI 에이전트 운영 규칙
  prompts/
    00-research.md                   # 외부 도구 리서치 요약 (참고)
    01-tool-evaluation.md            # Prompt 01: 도구 비교 분석
    02-pi-lab-design.md              # Prompt 02: 실험실 설계
    03-agents-md-generator.md        # Prompt 03: AGENTS.md 생성
    04-spring-review-skill.md        # Prompt 04: Pi Skill 설계
    05-security-policy.md            # Prompt 05: 보안 정책 설계
    06-tool-benchmark.md             # Prompt 06: 도구 벤치마크
    07-spring-work.md                # Prompt 07: Spring Boot 실무
    08-pr-review.md                  # Prompt 08: PR 리뷰 자동화
    09-pr-check.md                   # Prompt 09: Continue 스타일 PR Check
    10-mcp-design.md                 # Prompt 10: MCP 연동 설계
    11-context-engineering.md        # Prompt 11: Context Engineering
    12-experiment-template.md        # Prompt 12: 실험 기록 템플릿
    13-product-design.md             # Prompt 13: 제품화 기획
    14-plan-only.md                  # Prompt 14: 계획만 세우기
    15-minimal-change.md             # Prompt 15: 최소 변경
  sandbox/
    sample-spring-api/README.md      # Spring Boot 샘플 (미생성)
    sample-react-app/README.md       # React 샘플 (미생성)
  experiments/
    2026-06-05-pi-vs-aider.md        # 실험 2: Pi vs Aider 비교
    2026-06-05-pi-extension.md       # 실험 5: Pi Skill 설계
  policies/
    allowed-commands.md              # 허용 명령 목록
    denied-commands.md               # 금지 명령 목록
    security-checklist.md            # 보안 체크리스트
```

## 총 파일 수: 21개 (1차)

---

## 2차: sandbox 프로젝트 실제 코드 생성

사용자 요청: "계속해서 만들어줘"

### sample-spring-api (Spring Boot 3.x + Java 17 + JPA + H2/MySQL)

의도적으로 7가지 문제를 포함한 벤치마크용 프로젝트:

| # | 문제 | 위치 |
|---|------|------|
| 1 | N+1 쿼리 | UserService.getAllUsersWithOrders() + UserRepository (Fetch Join 없음) |
| 2 | 테스트 누락 | Service 테스트 없음, OrderController 테스트 없음 |
| 3 | 예외 처리 불일치 | UserController (RuntimeException), OrderController (String/ErrorResponse 혼용) |
| 4 | DTO 미사용 | Entity 직접 API 응답으로 반환 |
| 5 | Controller 비즈니스 로직 | UserController.deleteUser()에서 OrderRepository 직접 주입 |
| 6 | Transaction 누락 | UserService/OrderService 일부 메서드에만 @Transactional |
| 7 | 민감 정보 로그 | UserService.createUser()에서 이메일 INFO 로그 출력 |

생성 파일:
- build.gradle, settings.gradle
- src/main/resources/application.yml, data.sql
- src/main/java/com/example/lab/ (LabApplication, entity/User, entity/Order, repository/UserRepository, repository/OrderRepository, service/UserService, service/OrderService, controller/UserController, controller/OrderController, exception/ErrorResponse, exception/GlobalExceptionHandler)
- src/test/java/com/example/lab/ (LabApplicationTests, controller/UserControllerTest)

### sample-react-app (Next.js 14 + React 18 + TypeScript)

sample-spring-api와 연동하는 간단한 프론트엔드:
- package.json, tsconfig.json, next.config.js, .gitignore
- src/app/layout.tsx, src/app/page.tsx

## 총 파일 수: 48개 (21 + 15 Spring Boot + 6 React + 6 기존 README 등)
