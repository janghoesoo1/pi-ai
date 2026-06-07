# 기술 스택 기본값 변경: Java -> Kotlin, Next.js 유지

- 날짜: 2026-06-07
- 타입: chat
- 작업: 실험실 문서의 기술 스택 기본값을 Java -> Kotlin으로 변경

## 사용자 요청

서버는 spring 기반의 kotlin 이 기본이어야 하고 클라이언트는 next.js 면 될것 같아
-> 옵션 2 (문서 기본값만 변경, 코드는 나중에)

## AI 작업 내용

### 변경 파일
1. `AGENTS.md` -- Tech Stack: Java 17+ -> Kotlin (JVM 17+), frontend에 TypeScript 명시
2. `AGENTS.md` -- Coding Rules: "Spring Boot / Java" -> "Spring Boot / Kotlin", nullable/data class 규칙 추가
3. `AGENTS.md` -- Security Rules: PreparedStatement -> parameterized query (Kotlin 맥락)
4. `README.md` -- 프롬프트 팩 목록: Prompt 07 설명 Java -> Kotlin
5. `sandbox/sample-spring-api/README.md` -- 스펙: Java -> Kotlin, H2/MySQL, Gradle Kotlin DSL
6. `sandbox/sample-spring-api/build.gradle` -> `build.gradle.kts` (Kotlin DSL로 전환)
7. `sandbox/sample-spring-api/settings.gradle` -> `settings.gradle.kts`
8. `prompts/07-spring-work.md` -- Java/Spring Boot -> Kotlin/Spring Boot
