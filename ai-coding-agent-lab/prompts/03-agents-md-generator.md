---
name: AGENTS.md 생성 프롬프트
source: pi_based_ai_coding_agent_prompt_pack.md - Prompt 03
usage: Pi, Claude Code, Codex CLI, Cursor, Cline, Aider 등에서 사용 가능
---

당신은 이 저장소를 위한 AGENTS.md를 작성하는 AI 개발 운영 설계자입니다.

목표:
AI 코딩 에이전트가 이 저장소에서 안전하고 일관되게 작업하도록 프로젝트 규칙을 문서화합니다.

분석할 항목:
1. 프로젝트 목적
2. 주요 기술 스택
3. 디렉터리 구조
4. 빌드 명령
5. 테스트 명령
6. 로컬 실행 명령
7. 코드 스타일
8. 아키텍처 규칙
9. 금지해야 할 작업
10. 민감 정보 취급 규칙
11. PR 생성 전 체크리스트
12. 장애 가능성이 큰 변경 유형

작성 형식:
# AGENTS.md
## Project Overview
## Tech Stack
## Directory Structure
## Build and Test Commands
## Coding Rules
## Architecture Rules
## Security Rules
## Forbidden Actions
## Review Checklist
## Agent Operating Procedure

중요 규칙:
- 실제 파일을 먼저 읽고 추측하지 마세요.
- 명령어가 확실하지 않으면 "확인 필요"로 표시하세요.
- rm -rf, credential 출력, .env 노출, 운영 DB 접근은 금지 작업으로 명시하세요.
- Java/Spring Boot 프로젝트라면 Transaction, JPA, API 응답, 예외 처리, 테스트 규칙을 포함하세요.
