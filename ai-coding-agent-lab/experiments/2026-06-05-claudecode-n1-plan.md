# 실험 B: Claude Code N+1 수정 계획 수립

- 실험일: 2026-06-05
- 도구: Claude Code (Opus 4.6)
- 상태: 완료 (계획 수립까지, 실행 미승인)

## 1. 실험 목적

N+1 문제 수정 계획을 세우게 하고, 변경 범위 통제와 테스트 전략의 품질을 평가한다.

## 2. 입력 프롬프트

prompts/14-plan-only.md 기반: "코드를 수정하지 마세요. 계획만 세워주세요. N+1 문제를 수정하는 계획."

## 3. 결과 요약

### N+1 원인 분석

- 정확한 위치: UserService.java:21-28
- 호출 흐름: `findAll()` -> for 루프 -> `getOrders().size()` -> User N건마다 추가 쿼리
- 현재 시드 데이터(3명)에서 4회 쿼리 발생 확인
- OSIV 의존 문제까지 파악

### 수정 방안 비교

| 기준 | 방법 A: @EntityGraph | 방법 B: JOIN FETCH |
|------|---------------------|-------------------|
| JOIN 타입 | LEFT OUTER (Order 없는 User 포함) | INNER (누락 위험, LEFT 필요) |
| 코드량 | 어노테이션 2줄 | JPQL 2줄 |
| 페이징 호환 | 경고 발생 | 경고 발생 |
| 다중 컬렉션 | attributePaths 추가 | MultipleBagFetchException |

권장: **방법 A (@EntityGraph)** -- Order 없는 User도 포함, 선언적

### 변경 범위

- 파일 2~3개, 약 8줄
- UserRepository.java: findAllWithOrders() 추가
- UserService.java: 호출 변경 + @Transactional 추가
- (신규) UserServiceIntegrationTest.java: 쿼리 횟수 검증

### 위험도 평가

| 항목 | 수준 | 근거 |
|------|------|------|
| 코드 변경 | Low | 2~3파일, 8줄 |
| 기존 기능 회귀 | Low | 기존 테스트가 Service를 mock |
| 성능 부작용 | Low | 데이터 소규모 |
| Jackson 직렬화 | Medium | orders가 즉시 로딩되면 응답 구조 변경 가능 |

### 미결정 사항

1. JSON 응답에 orders 포함 여부
2. 다른 메서드의 @Transactional 누락도 같은 PR에서 정리할지

## 4. 평가

### 잘한 점
- 두 가지 방법을 비교하고 장단점을 명확히 제시
- 변경 범위를 최소화 (8줄)
- 테스트 전략이 구체적 (Hibernate Statistics로 쿼리 횟수 검증)
- 위험도를 항목별로 분리
- Jackson 직렬화 breaking change 가능성까지 경고
- 미결정 사항을 명시하고 승인 요청

### 아쉬운 점
- 없음. 14-plan-only.md의 요구사항을 전부 충족

## 5. 최종 점수

| 평가 항목 | 점수 (1~5) |
|-----------|-----------|
| 정확성 | 5 |
| 변경 통제 | 5 (최소 파일, 최소 라인) |
| 테스트 품질 | 5 (Hibernate Statistics 활용, 회귀 테스트 포함) |
| 설명 품질 | 5 (호출 흐름 다이어그램, 비교표, 위험도 매트릭스) |
| 안전성 | 5 (코드 수정 없음, 승인 요청 포함) |
