# 프롬프트 팩 추출 - 독립 파일 생성

## 사용자 요청

`pi_based_ai_coding_agent_prompt_pack.md` 원본 문서에서 6개 프롬프트를 독립 실행 가능한 파일로 추출해 달라는 요청.

생성 대상:
- `ai-coding-agent-lab/prompts/00-research.md` - 외부 도구 비교표 (참고 문서)
- `ai-coding-agent-lab/prompts/01-tool-evaluation.md` - Prompt 01: 도구 리서치
- `ai-coding-agent-lab/prompts/02-pi-lab-design.md` - Prompt 02: 실험실 설계
- `ai-coding-agent-lab/prompts/03-agents-md-generator.md` - Prompt 03: AGENTS.md 생성
- `ai-coding-agent-lab/prompts/04-spring-review-skill.md` - Prompt 04: Pi Skill 설계
- `ai-coding-agent-lab/prompts/05-security-policy.md` - Prompt 05: 보안 정책 설계

## AI 응답 요약

원본 문서를 읽고 각 섹션의 코드블록 안 내용을 그대로 추출하여 파일별 frontmatter를 붙여 저장.

파일 형식:
```
---
name: {프롬프트 이름}
source: pi_based_ai_coding_agent_prompt_pack.md - Prompt {번호}
usage: Pi, Claude Code, Codex CLI, Cursor, Cline, Aider 등에서 사용 가능
---

{프롬프트 본문}
```

`00-research.md`는 프롬프트가 아닌 참고 문서이므로 usage를 "프롬프트가 아닌 참고 문서"로 표기.

## 생성된 파일 목록

| 파일 | 원본 섹션 |
|------|----------|
| `00-research.md` | 섹션 1 비교표 |
| `01-tool-evaluation.md` | Prompt 01 |
| `02-pi-lab-design.md` | Prompt 02 |
| `03-agents-md-generator.md` | Prompt 03 |
| `04-spring-review-skill.md` | Prompt 04 |
| `05-security-policy.md` | Prompt 05 |
