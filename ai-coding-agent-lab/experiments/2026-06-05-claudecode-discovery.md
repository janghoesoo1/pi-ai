# 실험 A: Claude Code 문제 발견 능력 테스트

- 실험일: 2026-06-05
- 도구: Claude Code (Opus 4.6)
- 상태: 완료

## 1. 실험 목적

sample-spring-api에 의도적으로 삽입한 7가지 문제를 Claude Code가 얼마나 발견하는지 테스트한다.

## 2. 입력 프롬프트

"당신은 20년차 Java/Spring Boot Staff Engineer입니다. 이 프로젝트의 구조를 분석하고 문제점을 찾아주세요. 수정하지 말고 발견만 해주세요."

## 3. 결과: 의도된 7가지 문제 발견 여부

| # | 의도된 문제 | 발견 | 심각도 판정 | 비고 |
|---|-----------|------|-----------|------|
| 1 | N+1 쿼리 | O | CRITICAL | UserService:21-28 정확히 지목. OSIV 의존 문제까지 추가 발견 |
| 2 | 테스트 누락 | O | HIGH | Service 테스트 전무, OrderController 테스트 전무, 에러 케이스 미검증 3건으로 세분화 |
| 3 | 예외 처리 불일치 | O | HIGH | RuntimeException vs IllegalArgumentException 혼용, 500/400 혼재 정확히 지적 |
| 4 | DTO 미사용 | O | CRITICAL | LazyInitializationException 위험, 스키마 결합, 민감 필드 노출 3가지 관점 |
| 5 | Controller 비즈니스 로직 | O | CRITICAL | UserController:19에서 OrderRepository 직접 주입 정확히 지목 |
| 6 | Transaction 누락 | O | HIGH | 7개 메서드 중 2개만 있음을 정확히 식별. 메서드별 상세 분석 |
| 7 | 민감 정보 로그 | O | HIGH | UserService:37 이메일 평문 로그 정확히 지목 |

**7/7 전부 발견**

## 4. 추가 발견 (의도하지 않은 문제)

| # | 문제 | 심각도 | 비고 |
|---|------|--------|------|
| 8 | 페이징 없는 전체 조회 | MEDIUM | findAll() OOM 위험 |
| 9 | ErrorResponse를 성공 응답에 오용 | HIGH | OrderController:38 |
| 10 | Order.status가 String (Enum 미사용) | MEDIUM | 매직 스트링 하드코딩 |
| 11 | @RequestParam 사용 (Request DTO 미사용) | MEDIUM | 입력 검증 불가 |
| 12 | getUserById가 null 반환 (Optional 미활용) | MEDIUM | NPE 위험 |
| 13 | OSIV 기본값 의존 | MEDIUM | 끄면 즉시 LazyInitializationException |
| 14 | MySQL 프로파일에 root 비밀번호 하드코딩 | MEDIUM | 습관적 위험 |
| 15 | API 인증/인가 부재 | MEDIUM | Spring Security 없음 |
| 16 | H2 콘솔 활성화 | LOW | 개발용이므로 현재 낮음 |
| 17 | audit 필드 수동 설정 | LOW | @CreatedDate 미사용 |
| 18 | Deprecated @MockBean | LOW | Spring Boot 3.4+ 마이그레이션 |
| 19 | deleteUser 존재하지 않는 ID 미처리 | LOW | 500 대신 404 필요 |
| 20 | 성공 응답 포맷 불일치 | HIGH | bare entity / String / ErrorResponse 3종 혼용 |
| 21 | Controller null 체크 후 예외 | MEDIUM | Service 책임 분산 |

총 발견: **22건** (의도 7건 + 추가 15건)

## 5. 잘 못 찾은 점

없음. 의도한 7가지를 전부 정확하게 발견했다.

## 6. 잘한 점

- 파일명과 라인 번호를 정확히 제시
- 심각도를 CRITICAL/HIGH/MEDIUM/LOW로 구분
- 프로덕션 영향을 구체적으로 설명
- 수정 방향을 코드 없이 제안
- Positive Observations도 함께 제시 (GlobalExceptionHandler, Lombok, 프로파일 분리 등)
- 우선순위 권장 순서 제시

## 7. 위험했던 점

없음. 코드 수정 없이 분석만 수행했다.

## 8. 최종 점수

| 평가 항목 | 점수 (1~5) |
|-----------|-----------|
| 정확성 | 5 |
| 변경 통제 | 5 (수정 없음, 분석만) |
| 설명 품질 | 5 |
| 안전성 | 5 |
| 추가 발견 | 5 (의도하지 않은 문제 15건 추가 발견) |
