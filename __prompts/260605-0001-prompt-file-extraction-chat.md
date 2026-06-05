# 260605-0001 - 프롬프트 팩 파일 추출

**날짜**: 2026-06-05
**타입**: chat

---

## 사용자 요청

원본 문서 `pi_based_ai_coding_agent_prompt_pack.md`에서 Prompt 06~10을 독립 실행 가능한 프롬프트 파일로 추출해 달라는 요청.

생성 대상:
- `06-tool-benchmark.md` - Prompt 06: 도구 비교 실험 프롬프트
- `07-spring-work.md` - Prompt 07: Java/Spring Boot 실무 작업 프롬프트
- `08-pr-review.md` - Prompt 08: PR 리뷰 자동화 프롬프트
- `09-pr-check.md` - Prompt 09: Continue 스타일 PR Check 프롬프트
- `10-mcp-design.md` - Prompt 10: MCP 연동 설계 프롬프트

파일 형식: frontmatter(name/source/usage) + 프롬프트 본문 원문 그대로.

---

## 처리 내용

1. 원본 문서 `/Users/janghoesu/work/pi-ai/pi_based_ai_coding_agent_prompt_pack.md` 전체 읽기
2. Prompt 06~10 본문 코드블록 내용 추출
3. 각 파일에 frontmatter 추가하여 `/Users/janghoesu/work/pi-ai/ai-coding-agent-lab/prompts/` 에 저장

---

## 생성된 파일

| 파일 | 용도 |
|------|------|
| `06-tool-benchmark.md` | Pi/Claude Code/Codex CLI/Aider/Cline/Cursor 동일 작업 벤치마크 설계 |
| `07-spring-work.md` | 20년차 Staff Engineer 페르소나로 Spring Boot 기능 개선 |
| `08-pr-review.md` | diff 기준 엄격한 Staff Engineer 코드 리뷰, APPROVE/COMMENT/REQUEST_CHANGES 판정 |
| `09-pr-check.md` | Continue `.continue/checks/` 방식 PR 자동 점검. frontmatter에 name/summary 포함 |
| `10-mcp-design.md` | GitHub/Jira/Confluence/DB 등 MCP 연동 아키텍처 설계 |

---

## 특이사항

- `09-pr-check.md`는 Continue PR check 파일 형태이므로 frontmatter에 `name`과 `summary` 필드를 포함함
- 프롬프트 본문은 원문 코드블록 내용 그대로 유지, 수정 없음
