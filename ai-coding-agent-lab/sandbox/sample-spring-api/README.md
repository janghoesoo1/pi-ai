# Sample Spring Boot API

AI 코딩 에이전트 실험용 Spring Boot REST API 샘플 프로젝트.

## 스펙
- Spring Boot 3.x
- Java 17+
- JPA (Hibernate)
- MySQL
- Gradle

## 도메인
- User
- Order

## 의도적으로 포함된 문제
- N+1 쿼리 문제
- 테스트 누락
- 예외 처리 불일치
- DTO 미사용 (Entity 직접 노출)

## 용도
prompts/06-tool-benchmark.md 기반 도구 비교 실험에서 사용.
각 AI 도구에게 동일한 작업을 시키고 결과를 비교한다.

## 상태
미생성 - Spring Initializr 또는 직접 생성 필요
