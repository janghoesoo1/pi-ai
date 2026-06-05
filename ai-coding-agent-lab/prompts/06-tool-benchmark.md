---
name: 도구 비교 실험 프롬프트
source: pi_based_ai_coding_agent_prompt_pack.md - Prompt 06
usage: Pi, Claude Code, Codex CLI, Cursor, Cline, Aider 등에서 사용 가능
---

당신은 AI 코딩 도구 벤치마크를 설계하는 평가자입니다.

다음 도구를 동일한 샘플 프로젝트에서 비교하려고 합니다.
- Pi
- Claude Code
- Codex CLI
- Aider
- Cline
- Cursor

샘플 프로젝트:
- Spring Boot REST API
- JPA 사용
- MySQL 사용
- 간단한 User/Order 도메인
- 의도적으로 N+1 문제, 테스트 누락, 예외 처리 불일치, DTO 누락을 포함

각 도구에 동일한 작업을 시킵니다.

작업 목록:
1. 프로젝트 구조 설명
2. 버그 찾기
3. N+1 문제 수정 제안
4. 테스트 추가
5. API 응답 구조 개선
6. README 업데이트
7. PR 설명 작성

평가 기준:
- 정확성
- 수정 범위 통제
- 테스트 생성 품질
- 설명 품질
- git diff 품질
- 불필요한 변경 여부
- 보안 위험 행동 여부
- 재현 가능성

산출물:
- 평가표
- 점수 기준
- 실험 기록 템플릿
- 최종 추천
