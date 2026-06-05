# 프로젝트 발전 방향 — lab을 주력 프로젝트의 컨트롤 플레인으로 전환

- 날짜: 2026-06-05
- 순번: 0005
- 타입: chat

---

## 사용자
이제 이 프로젝트를 어떻게 활용해서 발전시켜야 하는가?

## AI (요약)
ai-coding-agent-lab 구조를 분석한 결과 **"골격은 완성, 알맹이는 0"**으로 진단.
- 완성: 디렉토리 구조, AGENTS.md, OPERATING-GUIDE, 프롬프트 16개, 샌드박스 2개, 정책, 컨텍스트 골격
- 비어있음: 실험 0건, tool-insights/decisions/lessons 전부 플레이스홀더

핵심: lab의 자기 원칙("eval 멈추면 복리 성장도 멈춘다")인데 아직 시작조차 안 함.
지금 필요한 건 프롬프트를 더 만드는 게 아니라 **한 번이라도 실제로 돌려 데이터를 채우는 것**(병목 = 실행).
3단계 로드맵(첫 실험 1건 완주 → 컨텍스트 자산 채우기 → 루프) 제시 후 우선순위·목표 질문.

## 사용자 (선택)
- 우선 진행: 첫 실험 실제 실행
- 최종 목표: 내 개발 워크플로우 자동화

## AI (요약)
실험 전제 검증 중 현실 점검:
- `claude`·`codex`만 설치, `pi`·`aider` 미설치 → "Pi vs Aider" 실험 불가
- 샌드박스: gradlew 래퍼 없음 + JDK 미등록 → 빌드 실패

## 사용자
실제 프로젝트 두 개가 주력이다:
- `~/work/pact-conference-api-harness`
- `~/bf/workspace`

## AI (요약)
**핵심 재정의**: lab은 독립 장난감 실험실이 아니라 **두 주력 프로젝트의 AI 개발을 운영하는 컨트롤 플레인**이 되어야 한다. lab의 "회사 코드 금지(sandbox만)" 제약이 가치(주력 프로젝트)와 모순됨을 지적. 샌드박스는 폐기가 아니라 "프로덕션 적용 전 스테이징"으로 강등.

두 프로젝트 파악:
- pact-conference: Kotlin/SpringBoot3 멀티서비스(common·session·attendee·cfp·gateway) + Pact CDC + 자체 스캐폴딩 CLI `harness.sh`. 개인·저위험.
- bf/workspace: 풀스택 모노레포 + Jenkins/GitLab CI + 운영. 회사·고위험.

## 사용자 (선택)
- 먼저 연결: pact-conference
- 리스크: pact=개인(자유), bf=운영/회사(보수)

## AI (수행 결과)
1. **pact-conference에 코드 기반 AGENTS.md 생성** — 실제 컨벤션(ApiResponse 엔벨로프, DTO 패턴, GlobalExceptionHandler의 RFC7807 ProblemDetail, Store/StoreInterface, gateway ProxyController 라우팅, Pact consumer/provider, common 공유 JWT/RBAC, 포트 매핑) 근거로 작성. `harness.sh validate`/`list`로 라우팅·포트·모듈을 실측 검증.
2. **빌드 실패 3중 원인 발견·문서화**: (1)gradle-wrapper.jar 누락 (2)Java toolchain 미고정 → JVM 타깃 21 vs 24 충돌 (3)등록된 JDK 21 부재. AGENTS.md 빌드 섹션에 정확한 복구법 명시.
3. **lab 모순 해소**: lab-overview의 "회사 코드 금지"를 "주력 프로젝트 연결(pact=개인 자유, bf=운영 보수)"로 갱신, decisions.md·lessons.md에 방향 전환과 교훈 기록.

핵심 교훈: 실험 도구 전제부터 확인 / 코드 고치기 전 빌드 가능 여부가 선결 / exit code 맹신 금지(실제 출력으로 검증).

## 사용자
다음단계 (= pact 빌드 복구 진행)

## AI (수행 결과 — 빌드 복구, 4겹 버그)
pact-conference 빌드를 살리는 과정에서 4개의 독립 버그가 순차로 드러남(양파 까기). 각 수정→검증→다음 겹 발견:
1. `gradle-wrapper.jar` 누락 → `gradle wrapper`로 재생성 (`./gradlew` 복구)
2. JVM 타깃 21 vs 24 충돌 → 루트 build.gradle.kts에 Java toolchain(21) + settings.gradle.kts에 Foojay resolver(JDK 21 자동 프로비저닝)
3. `jpa` 프로파일에서 `spring.autoconfigure.exclude` 미해제 → `application-jpa.yml`에 `exclude: []` 오버라이드
4. `@Entity` no-arg 생성자 없음 → session-service에 `kotlin("plugin.jpa")` 적용

결과: **전체 `./gradlew build` 통과**(37 태스크, session-service Testcontainers 통합테스트 5개 포함 전부 그린).
AGENTS.md 빌드 섹션을 "수정 완료 + 향후 새 JPA 서비스 추가 시 주의사항"으로 갱신. lab의 lessons/decisions/lab-overview에 첫 실제 실험 데이터로 기록.

변경 파일(pact-conference, 미커밋): `build.gradle.kts`, `settings.gradle.kts`, `session-service/build.gradle.kts`, `session-service/src/main/resources/application-jpa.yml`, `AGENTS.md`(신규).

## 사용자
1,2,3 계속 해

## AI (수행 결과 — 세 작업 연속)
**1. pact 빌드 복구 커밋**: `fix/build-recovery` 브랜치에서 3개 의미 단위 커밋(빌드인프라 / JPA활성화 / 문서). `.gitignore`의 `!gradle-wrapper.jar` 부정 규칙이 `*.jar`보다 앞에 있어 무효화된 버그도 수정(뒤로 이동). gradlew.bat 줄바꿈 노이즈 되돌림.

**2. AGENTS.md 기반 첫 실제 작업 + eval**: `experiment/scaffold-room-service` 브랜치에서 AGENTS.md 절차(Plan→dry-run→Execute→Verify)대로 `harness.sh new-service`로 room-service 스캐폴딩. 17파일 +284, 빌드 9초 그린, validate 전항목 정상. lab `experiments/2026-06-05-claudecode-scaffold-room.md`에 첫 eval 기록(정확성5·변경통제4·테스트1·설명5·안전성4). 한계: untyped Map store·테스트 미생성. `tool-insights.md`도 실데이터로 첫 작성.

**3. bf/workspace 파악 + 보수적 가드레일**: read-only 파악 — Kotlin DDD 멀티모듈(api/common/domain-ai·employee·mail·timesheet) + React/Vite 프론트, Jenkins/GitLab CI, 운영 HR SaaS(제품이 Claude 사용). `.env` 미추적 확인(보안 위생 양호). 운영 코드라 파일 미수정, lab `proposals/bf-workspace-AGENTS-draft.md`에 보수적 AGENTS.md 초안 제시(자동머지·프로덕션쓰기·CI/DB/시크릿 접근 금지, 기본 L2).

핵심: lab이 "빈 골격"에서 처음으로 실제 자산(AGENTS.md·eval·tool-insights·proposals)으로 채워짐. pact는 그린+커밋, bf는 보수적 진입 준비.
