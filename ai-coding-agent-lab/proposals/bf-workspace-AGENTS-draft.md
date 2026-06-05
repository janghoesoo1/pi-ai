# [DRAFT] bf/workspace AGENTS.md 제안

> 이 문서는 **lab 안의 제안 초안**이다. bf/workspace는 운영/회사 코드이므로 lab은 파일을 직접 쓰지 않는다.
> 검토 후 적절하다고 판단되면 사람이 `~/bf/workspace/AGENTS.md`로 복사·수정해 적용한다.
> 작성 근거: 2026-06-05 read-only 구조 파악(코드 미수정).

---

## 운영 코드 가드레일 (최상단 — 가장 중요)

이 저장소는 **운영 중인 HR/워크스페이스 SaaS**다. AI 에이전트는 다음을 절대 위반하지 않는다.

- **자동 머지 금지. 프로덕션 쓰기 금지.** 모든 변경은 사람 승인 + PR 리뷰를 거친다.
- **시크릿 접근 금지**: `.env`, `APP_JWT_SECRET`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_CHAT_SERVICE_ACCOUNT`, `ANTHROPIC_API_KEY`, DB 자격증명을 읽거나 출력하지 않는다. (`.env`는 gitignore됨 — 그대로 둔다)
- **CI/배포 파일은 사람 전용(L1)**: `Jenkinsfile`, `.gitlab-ci.yml`, `docker-compose.prod.yml`, `infra/`, `ops/`는 에이전트가 수정하지 않는다.
- **DB 스키마/마이그레이션 변경은 L1**: 사람 설계 후에만. 운영 DB에 직접 접속하지 않는다.
- 기본 자율성: **L2(AI 준비 + 사람 승인)**. 읽기·분석·제안 위주. 코드 생성은 제안→승인 후 적용.

---

## Project Overview
사내 HR/워크스페이스 SaaS. 직원·근태·메일·AI 도메인을 가진 멀티모듈 백엔드 + 관리자 웹.
제품 자체가 Claude(Anthropic API)를 사용하는 AI 기능(`domain-ai`)을 포함한다.

## Tech Stack
| 구분 | 값 |
|------|-----|
| 백엔드 | Kotlin + Spring Boot (Gradle Kotlin DSL, `./gradlew`) |
| 백엔드 아키텍처 | DDD 멀티모듈 |
| 프론트 | React 18 + Vite + TypeScript, axios |
| 인증 | JWT (`common-auth`) |
| 통합 | Google OAuth / Google Chat, Sentry, Anthropic |
| CI/CD | Jenkins + GitLab CI |
| 데이터 | DB(`DB_URL`) + Redis |

## Directory Structure (확인된 범위)
```
backend/  (rootProject: bf-workspace)
  api/api-web            # 웹 계층 (컨트롤러/REST)
  common/common-auth     # JWT 인증
  common/common-core     # 공통 유틸/기반
  domain/domain-ai       # AI 기능 (Anthropic 연동)
  domain/domain-employee # 직원
  domain/domain-mail     # 메일
  domain/domain-timesheet# 근태
frontend/workspace-admin-web  # React/Vite 관리자 웹
infra/, ops/, Jenkinsfile, .gitlab-ci.yml  # ← 에이전트 수정 금지
```
> 확인 필요: 각 domain 모듈 내부 패키지 컨벤션, api-web의 응답 표준/예외 처리, 프론트 상태관리·라우팅 구조는 추가 파악 후 보강.

## Build and Test Commands
```bash
# 백엔드 (확인 필요: 정확한 태스크명)
cd backend && ./gradlew build
./gradlew :api:api-web:test     # 모듈 경로는 확인 필요

# 프론트
cd frontend/workspace-admin-web
npm install
npm run dev      # vite
npm run build    # tsc -b && vite build
```

## Coding Rules
- 변경 전 관련 파일을 반드시 읽는다. DDD 모듈 경계(api↔domain↔common)를 넘는 의존을 만들지 않는다.
- domain 모듈은 웹/인프라 관심사를 모르게 유지한다.
- 프론트: 컴포넌트/타입 안전(TS strict) 유지, axios 호출은 기존 API 클라이언트 패턴을 따른다.
- 변경 범위 최소화, 모든 변경은 git diff로 검토 가능.

## Security Rules
- 시크릿·PII(직원 개인정보) 로그 출력 금지. HR 도메인 특성상 개인정보 취급에 특히 주의.
- 입력 검증을 경계(api-web)에서 수행. 인증/인가는 `common-auth` 재사용.
- 외부 통합(Google/Anthropic) 호출 시 키는 환경변수로만, 코드에 하드코딩 금지.

## Forbidden Actions
```bash
cat .env / printenv          # 시크릿 노출
git push --force
# Jenkinsfile / .gitlab-ci.yml / docker-compose.prod.yml / infra / ops 수정
# 운영 DB 접속·마이그레이션
# 자동 머지 / 자동 배포
```

## Review Checklist
- [ ] 운영 가드레일 위반 없음(시크릿·CI·DB·자동머지)
- [ ] DDD 모듈 경계 준수
- [ ] 개인정보/시크릿 로그 노출 없음
- [ ] 변경 범위 최소, 테스트 존재
- [ ] 사람 승인 받음 (L2)

## Agent Operating Procedure
1. 관련 파일을 먼저 읽고 영향 범위(모듈 경계, 통합 지점)를 파악한다.
2. **변경 계획을 먼저 제시하고 사람 승인을 받는다.** (기본 L2)
3. 승인 후 최소 변경. CI/배포/DB/시크릿은 손대지 않는다.
4. 빌드/테스트로 검증. 사람이 PR 리뷰 후 머지.

---

## 다음 단계 제안 (bf 도입 순서)
1. 이 초안을 사람이 검토 → 빌드/테스트 정확한 명령, 모듈 컨벤션 보강
2. **읽기 전용 워크플로부터** 도입: 코드 분석·PR 리뷰 보조(L2). 쓰기 작업은 신뢰 쌓인 후.
3. domain별(employee/timesheet/mail/ai) 세부 컨벤션을 prompts/로 분리
