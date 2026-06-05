# 260605-0001 - 프롬프트 팩 파일 추출 (chat)

## 요청

원본 문서 `pi_based_ai_coding_agent_prompt_pack.md`에서 Prompt 11~15를 독립 실행 가능한 프롬프트 파일로 추출해 달라는 요청.

생성 대상:
- `ai-coding-agent-lab/prompts/11-context-engineering.md` (Prompt 11)
- `ai-coding-agent-lab/prompts/12-experiment-template.md` (Prompt 12)
- `ai-coding-agent-lab/prompts/13-product-design.md` (Prompt 13)
- `ai-coding-agent-lab/prompts/14-plan-only.md` (Prompt 14)
- `ai-coding-agent-lab/prompts/15-minimal-change.md` (Prompt 15)

파일 형식: frontmatter(name, source, usage) + 원문 프롬프트 본문

## 응답

원본 문서를 읽고 해당 프롬프트 코드블록 내용을 그대로 추출하여 5개 파일을 병렬 생성했습니다.
각 파일 상단에 `name`, `source`, `usage` frontmatter를 추가했으며, 프롬프트 본문은 원문 그대로 유지했습니다.

## 생성된 파일

- `/Users/janghoesu/work/pi-ai/ai-coding-agent-lab/prompts/11-context-engineering.md`
- `/Users/janghoesu/work/pi-ai/ai-coding-agent-lab/prompts/12-experiment-template.md`
- `/Users/janghoesu/work/pi-ai/ai-coding-agent-lab/prompts/13-product-design.md`
- `/Users/janghoesu/work/pi-ai/ai-coding-agent-lab/prompts/14-plan-only.md`
- `/Users/janghoesu/work/pi-ai/ai-coding-agent-lab/prompts/15-minimal-change.md`
