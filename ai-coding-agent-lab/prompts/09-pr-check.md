---
name: Spring Security and Maintainability Review
source: pi_based_ai_coding_agent_prompt_pack.md - Prompt 09
usage: Pi, Claude Code, Codex CLI, Cursor, Cline, Aider 등에서 사용 가능. .continue/checks/ 디렉토리를 직접 생성해 배치하면 Continue PR check로도 활용할 수 있다(현재 저장소에는 미포함).
---

관련 프롬프트: [08-pr-review.md](08-pr-review.md) (사람 중심의 포괄적 PR 리뷰)

Review this pull request for Spring Boot backend risks.

Fail this check if any of the following are true:
- New API endpoint has no input validation.
- Controller contains business logic that should be in a service.
- Entity is directly returned as API response.
- SQL or JPQL is built through unsafe string concatenation.
- Sensitive data is logged.
- Transactional boundary is missing for write operations.
- N+1 query risk is introduced without mitigation.
- Error response format is inconsistent with the existing project style.
- Important behavior is changed without tests.

If issues are found:
1. Explain the issue.
2. Point to the relevant file and method.
3. Explain the production risk.
4. Suggest the smallest safe fix.

If no issues are found, pass the check and summarize why.
