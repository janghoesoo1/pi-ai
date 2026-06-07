---
name: Pi 기반 실험실 설계 프롬프트
source: pi_based_ai_coding_agent_prompt_pack.md - Prompt 02
usage: Pi, Claude Code, Codex CLI, Cursor, Cline, Aider 등에서 사용 가능
---

관련 프롬프트: [13-product-design.md](13-product-design.md) (실험실을 제품으로 발전시키는 기획)

당신은 AI Coding Agent Lab을 설계하는 소프트웨어 아키텍트입니다.

나는 Pi를 기반으로 AI 코딩 에이전트 실험실을 만들고 싶습니다.
목표는 단순히 Pi를 설치하는 것이 아니라, 여러 AI 코딩 도구의 장점을 분석해서 나만의 개발 워크플로우를 만드는 것입니다.

요구사항:
1. Mac 환경을 기준으로 합니다.
2. Java/Spring Boot 프로젝트를 주요 대상으로 합니다.
3. Cursor, Claude Code, Codex CLI, Aider와 함께 비교 실험할 수 있어야 합니다.
4. 실제 회사 코드가 아니라 샘플 프로젝트에서 먼저 실험합니다.
5. 파일 수정, bash 실행, 네트워크 접근, secret 접근에 대한 안전 정책이 있어야 합니다.
6. 실험 결과를 markdown으로 남길 수 있어야 합니다.
7. 나중에는 MCP, GitHub PR 체크, 자동 문서화까지 확장하고 싶습니다.

산출물:
- 디렉터리 구조
- README.md 초안
- AGENTS.md 초안
- allowed command / denied command 정책
- 첫 번째 실험 시나리오 5개
- 성공/실패 평가 기준
- 2주 PoC 일정

제약:
- 회사 코드나 민감 정보는 사용하지 않습니다.
- destructive command는 기본 금지합니다.
- 모든 자동 수정은 git diff로 검토 가능해야 합니다.
