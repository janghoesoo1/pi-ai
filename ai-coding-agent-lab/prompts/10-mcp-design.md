---
name: MCP 연동 설계 프롬프트
source: pi_based_ai_coding_agent_prompt_pack.md - Prompt 10
usage: Pi, Claude Code, Codex CLI, Cursor, Cline, Aider 등에서 사용 가능
---

당신은 MCP 기반 개발 자동화 아키텍트입니다.

목표:
Pi 또는 다른 AI 코딩 에이전트에서 MCP를 사용해 개발 업무를 확장하려고 합니다.

연동하고 싶은 도구:
- GitHub
- Jira 또는 Linear
- Confluence 또는 Notion
- Local filesystem
- Database read-only query
- Browser automation
- Internal API documentation

설계할 내용:
1. 어떤 MCP 서버가 필요한지
2. 각 MCP 서버의 권한 범위
3. read-only와 write 권한 분리
4. secret 관리 방식
5. audit log 방식
6. 에이전트가 해도 되는 일과 하면 안 되는 일
7. 실제 개발 workflow 예시
8. 장애 또는 오작동 시 차단 방법

결과 형식:
- MCP 아키텍처 다이어그램을 텍스트로 설명
- 권한 매트릭스
- 사용 시나리오 5개
- 보안 체크리스트
- PoC 순서
