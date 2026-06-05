---
name: 실험 기록 템플릿 생성 프롬프트
source: pi_based_ai_coding_agent_prompt_pack.md - Prompt 12
usage: Pi, Claude Code, Codex CLI, Cursor, Cline, Aider 등에서 사용 가능
---

당신은 AI 코딩 도구 실험 기록을 남기는 연구원입니다.

다음 실험을 markdown으로 기록할 템플릿을 만들어 주세요.

실험 대상 도구:
[도구명]

작업:
[예: Spring Boot N+1 문제 수정]

기록할 항목:
1. 실험 목적
2. 입력 프롬프트
3. 사용 모델
4. 실행 환경
5. 에이전트가 읽은 주요 파일
6. 에이전트가 수정한 파일
7. 생성된 diff 요약
8. 테스트 실행 결과
9. 잘한 점
10. 위험했던 점
11. 사람이 개입한 부분
12. 다음 실험에서 바꿀 점
13. 최종 점수

점수 기준:
- 정확성: 1~5
- 변경 통제: 1~5
- 테스트 품질: 1~5
- 설명 품질: 1~5
- 안전성: 1~5

결과는 `experiments/YYYY-MM-DD-tool-task.md`로 저장할 수 있게 작성해 주세요.
