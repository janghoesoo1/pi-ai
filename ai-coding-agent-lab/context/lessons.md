# Lessons Learned

실패와 교훈. append-only로 유지한다.

| 날짜 | 교훈 | 출처 |
|------|------|------|
| 2026-06-05 | **실험 도구 전제부터 확인하라.** lab은 "Pi vs Aider"를 가정했지만 이 머신엔 `pi`·`aider` 미설치, `claude`·`codex`만 존재. 프롬프트 팩이 가정한 도구가 실제로 없으면 실험 자체가 불가능 | 도구 가용성 점검 |
| 2026-06-05 | **샌드박스/주력 모두 빌드 환경이 전제다.** sample-spring-api는 gradlew 래퍼 없음 + JDK 미등록으로 toolchain 빌드 실패. pact-conference는 (1)`gradle-wrapper.jar` 누락 (2)Java toolchain 미고정으로 JVM 타깃 21 vs 24 충돌 (3)등록된 JDK 21 부재 → 셋 다 빌드 실패. "코드를 고치기 전에 빌드가 되는지"가 모든 실험의 선결 조건 | pact/sandbox 빌드 검증 |
| 2026-06-05 | **에이전트의 exit code를 맹신하지 말 것.** 백그라운드 `./gradlew` 가 exit 0으로 보고됐으나 실제로는 "Unable to access jarfile"로 실패. 검증은 종료코드가 아니라 실제 출력으로 한다 | 빌드 검증 |
| 2026-06-05 | **lab 자기 모순 발견.** lab-overview는 "회사 코드 금지(sandbox만)"인데 정작 가치는 주력 프로젝트에 있음. 안전 규칙(가드레일)과 가치 회수 대상을 분리해야 함 — 회사 코드엔 보수적 가드레일, 개인 코드엔 자율성 | 방향 재정의 |
| 2026-06-05 | **"빌드 복구"는 한 번에 안 끝난다 — 양파 까기다.** pact-conference 빌드를 살리는 과정에서 4겹의 독립 버그가 순차로 드러남: (1)wrapper jar 누락 (2)Java toolchain 미고정→JVM타깃 21/24 충돌 (3)jpa 프로파일에서 `spring.autoconfigure.exclude` 미해제→JPA빈 누락 (4)`kotlin("plugin.jpa")` 미적용→엔티티 no-arg 생성자 없음. 각 수정이 다음 겹을 드러냄. **교훈: 한 번 통과를 성공으로 보지 말고, 매번 실제 실패 메시지의 근본원인까지 추적할 것** | pact 빌드 복구 (lab 첫 실제 실험) |
| 2026-06-05 | **Kotlin+JPA 표준 셋업 체크리스트 도출**: `kotlin("plugin.jpa")`(no-arg) 필수, 엔티티는 var+nullable 기본값, 프로파일별 autoconfigure exclude 충돌 주의. 이건 향후 pact/유사 Kotlin 프로젝트 AGENTS.md·프롬프트팩에 재사용할 자산 | 동상 |
