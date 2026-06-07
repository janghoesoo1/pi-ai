---
name: AI 코딩 에이전트 도구 리서치 프롬프트
source: pi_based_ai_coding_agent_prompt_pack.md - Prompt 01
usage: Pi, Claude Code, Codex CLI, Cursor, Cline, Aider 등에서 사용 가능
---

관련 프롬프트: [06-tool-benchmark.md](06-tool-benchmark.md) (동일 도구 벤치마크 실험), [00-research.md](00-research.md) (도구 비교 참고표)

당신은 Staff Engineer이자 AI Coding Agent Researcher입니다.

목표는 현재 프로젝트에 적합한 AI 코딩 도구 조합을 선정하는 것입니다.
다음 도구들을 비교 분석해 주세요.

대상 도구:
- Pi
- Claude Code
- OpenAI Codex CLI
- GitHub Copilot CLI
- Aider
- Cline
- Roo Code
- Goose
- Continue
- Gemini CLI
- Qwen Code
- Cursor

분석 기준:
1. 도구의 핵심 철학
2. 터미널/IDE/GitHub/Slack/CI 연동 방식
3. 코드베이스 이해 방식
4. 파일 수정 및 명령 실행 권한 모델
5. context file 지원 여부: AGENTS.md, CLAUDE.md, rules, memories 등
6. MCP 또는 외부 도구 연동 여부
7. Java/Spring Boot 백엔드 프로젝트에 적합한지
8. 엔터프라이즈 보안 관점의 위험
9. 개인 개발자 실험용으로 적합한지
10. 팀 표준화 도구로 적합한지

결과 형식:
- 1페이지 요약
- 비교표
- 추천 조합 3개
- PoC 계획
- 도입하지 말아야 할 경우
- 다음 액션 아이템

중요:
- 추측하지 말고 확인된 정보와 추론을 구분해 주세요.
- 보안/비용/벤더 종속성은 별도 섹션으로 분리해 주세요.
