---
name: 외부 도구 리서치 요약
source: pi_based_ai_coding_agent_prompt_pack.md - 섹션 1
usage: 프롬프트가 아닌 참고 문서. Pi 및 주변 AI 코딩 에이전트 도구 비교표.
---

| 도구 | 성격 | 강점 | 주의점 | Pi 기반 실험에 가져올 점 |
|---|---|---|---|---|
| Pi | 미니멀 터미널 agent harness | 확장성, provider 추상화, prompt template, skill, package | 내장 권한 시스템이 약함. sandbox 필요 | 커스텀 agent runtime 학습의 중심 |
| Claude Code | 완성도 높은 터미널/IDE/웹/Slack 코딩 에이전트 | 코드베이스 이해, 멀티파일 수정, 승인 기반 실행, Git/GitHub workflow | Claude 생태계 의존, 비용/사용량 관리 필요 | permission, context, agentic search, CLAUDE.md 패턴 |
| OpenAI Codex CLI | OpenAI 로컬 터미널 코딩 에이전트 | 로컬에서 코드 읽기/수정/실행, Rust 기반 CLI | ChatGPT/Codex 플랜 의존 | 터미널 UX, 로컬 실행, 작업 단위 관리 |
| GitHub Copilot CLI | GitHub-native 터미널 에이전트 | issue/PR 연동, `/plan`, `/fleet` 병렬 subagent | GitHub/Copilot 중심 workflow | PR/issue 중심 자동화 설계 |
| Aider | Git-native 터미널 AI 페어 프로그래머 | Git diff/commit workflow에 강함, 기존 코드베이스 편집에 적합 | 자동화 하네스라기보다는 페어 프로그래밍에 가까움 | Git 기반 변경 추적/commit 단위 작업 |
| Cline | VS Code/CLI/SDK 기반 오픈 코딩 에이전트 | Plan/Act, MCP, editor/terminal 통합, 승인 흐름 | IDE 의존성이 생길 수 있음 | Plan/Act 모드, MCP, human-in-the-loop |
| Roo Code | VS Code 계열 agent | 역할별 모드, auto-approve 제어, 코드베이스 인덱싱 | VS Code 중심 | 역할 기반 mode 설계 |
| Goose | 범용 로컬 AI agent | 코드뿐 아니라 리서치, 문서, 자동화, 데이터 분석까지 수행 | 코딩 전용 최적화는 별도 검증 필요 | 범용 agent + CLI/API/Desktop 패턴 |
| Continue | PR 체크 자동화 | Markdown 파일로 AI PR check 정의, GitHub status check | 코딩 assistant라기보다 품질 게이트 성격 | `.continue/checks/*.md` 방식의 정책 자동화 |
| Gemini CLI / Qwen Code | 터미널 기반 오픈소스 agent | 오픈소스, 모델별 특화, MCP/IDE 연동 가능 | 모델/플랫폼 성숙도 확인 필요 | 오픈소스 CLI agent 구조 비교 |
| Cursor / Windsurf / Devin | agentic IDE 또는 cloud/desktop agent | 제품 완성도, 병렬 agent, PR/Slack/GitHub 연동 | 벤더 종속, 비용, 보안 정책 확인 필요 | UX와 멀티에이전트 운영 방식 참고 |
