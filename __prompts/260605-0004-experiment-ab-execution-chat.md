# 실험 A/B 실행

- 날짜: 2026-06-05
- 타입: chat
- 작업: sample-spring-api에서 실험 A(문제 발견)와 B(N+1 수정 계획) 실행

## 사용자 요청

A, B

## AI 작업 내용

### 실험 A: 문제 발견 (code-reviewer, opus)
- 22건 발견 (의도한 7건 전부 + 추가 15건)
- experiments/2026-06-05-claudecode-discovery.md에 기록

### 실험 B: N+1 수정 계획 (architect, opus)
- @EntityGraph vs JOIN FETCH 비교 분석
- 변경 범위: 2~3파일, 8줄
- experiments/2026-06-05-claudecode-n1-plan.md에 기록
