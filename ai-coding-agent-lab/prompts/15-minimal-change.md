---
name: "작게 수정하고 검증하기" 프롬프트
source: pi_based_ai_coding_agent_prompt_pack.md - Prompt 15
usage: Pi, Claude Code, Codex CLI, Cursor, Cline, Aider 등에서 사용 가능
---

이제 승인된 계획에 따라 최소 변경만 수행해 주세요.

규칙:
1. 한 번에 큰 리팩토링을 하지 않습니다.
2. public API 변경은 사전에 명시합니다.
3. 기존 테스트가 깨지지 않게 합니다.
4. 변경 후 실행해야 할 테스트 명령을 제안합니다.
5. 수정한 파일과 이유를 요약합니다.
6. 다음 개선은 별도 단계로 분리합니다.

출력 형식:
## 수행한 변경
## 수정 파일
## 변경 이유
## 실행할 테스트
## 예상 리스크
## 다음 단계
