# AI Coding Agent Lab

## 목적

Pi를 연구용/확장용 기반으로 삼고, Claude Code/Codex CLI/Aider/Cline/Goose/Continue의 장점을 벤치마킹해서 "내 개발 방식에 맞는 AI 코딩 운영체계"를 만든다.

Pi는 Cursor나 Claude Code처럼 완성된 개발 경험을 제공하는 도구가 아니라, 작고 확장 가능한 터미널 기반 AI agent harness에 가깝다. 따라서 다음 세 가지 목적으로 사용한다.

1. AI 코딩 에이전트의 내부 구조를 이해한다.
2. 내 개발 워크플로우에 맞춘 커스텀 에이전트/스킬/프롬프트 템플릿을 만든다.
3. 외부 도구의 좋은 설계 패턴을 흡수하고, 최종적으로 `AGENTS.md + Prompt Pack + Security Policy + PR Check + Pi Skill` 조합을 만든다.

---

## 디렉토리 구조

```text
ai-coding-agent-lab/
  README.md
  AGENTS.md
  OPERATING-GUIDE.md
  prompts/
    00-research.md
    01-tool-evaluation.md
    02-pi-extension-design.md
    03-code-review.md
    04-spring-refactoring.md
  context/
    lab-overview.md
    tool-insights.md
    decisions.md
    lessons.md
  sandbox/
    sample-spring-api/
    sample-react-app/
  experiments/
    2026-06-05-pi-vs-aider.md
    2026-06-05-pi-extension.md
  policies/
    allowed-commands.md
    denied-commands.md
    security-checklist.md
```

| 디렉토리 | 역할 |
|----------|------|
| `prompts/` | 실험에 사용하는 프롬프트 템플릿 모음 |
| `sandbox/` | 실험용 샘플 프로젝트. 회사 코드 절대 금지 |
| `experiments/` | 실험 결과 기록. 날짜-도구-작업 형태로 저장 |
| `policies/` | 허용/금지 명령, 보안 정책 문서 |
| `context/` | 운영 기억 -- 실험실 상태, 도구 인사이트, 결정 로그, 교훈 |
| `OPERATING-GUIDE.md` | AI-네이티브 프레임워크 기반 운영 가이드 |

---

## 운영 프레임워크

이 실험실은 AI-네이티브 스타트업 프레임워크(6단계)를 적용한다. 상세 내용은 `OPERATING-GUIDE.md` 참조.

| 단계 | 실험실 적용 |
|------|------------|
| 1. 업무 매핑 | 반복 업무를 자율성 레벨(L1~L4)로 분류 |
| 2. 컨텍스트 시스템 | `AGENTS.md` + `context/` + `policies/` |
| 3. 자동화 선택 | 스크립트, AI 보조, 워크플로, 에이전트 중 가장 가벼운 도구 |
| 4. 스킬 + eval | `prompts/` = 스킬, `experiments/` = eval |
| 5. 팀 AI-네이티브 | 온보딩은 산출물로 종료. 판단을 지침으로 인코딩 |
| 6. 피드백 루프 | 매주 리뷰 -> 컨텍스트 갱신 -> 스킬 개선 -> 반복 |

핵심 원칙:
- 모델은 교체 가능하지만 컨텍스트와 eval은 회사만의 자산
- 가드레일은 코드와 설정에 (프롬프트 지시는 보안 경계가 아님)
- 자동 머지 금지, 프로덕션 쓰기 금지

---

## 빠른 시작

### Day 1: 도구 설치와 샘플 프로젝트 준비

1. Pi 설치
2. Claude Code 또는 Codex CLI 중 하나 설치
3. Aider 설치
4. 샘플 Spring Boot 프로젝트 생성
5. git 초기화
6. 실험 기록 폴더 생성

### Day 2: AGENTS.md 만들기

1. `prompts/03-code-review.md` 기반 프롬프트 실행 (Prompt 03)
2. Context Engineering 프롬프트 실행 (Prompt 11)
3. 사람이 AGENTS.md 검토
4. 금지 명령 추가
5. 첫 실험 기록 작성

### Day 3~4: 같은 작업을 여러 도구에 시켜보기

1. N+1 문제 찾기
2. 테스트 추가
3. 예외 처리 개선
4. README 업데이트
5. diff 비교

### Day 5: 보안 정책 정리

1. 안전한 실행 정책 설계 프롬프트 실행 (Prompt 05)
2. `policies/allowed-commands.md` 및 `policies/denied-commands.md` 문서 작성
3. sandbox 실행 방식 검토

### Week 2: Pi 기반 확장 개발

1. Pi Extension / Skill 설계 프롬프트로 skill 설계 (Prompt 04)
2. 작은 markdown report 기능부터 구현
3. PR check prompt 작성
4. MCP 연동 후보 정리

---

## 추천 첫 실험 시나리오

| 실험 | 목표 | 사용 프롬프트 |
|------|------|--------------|
| 실험 1: Pi로 AGENTS.md 만들기 | 샘플 Spring Boot 프로젝트를 분석해서 AGENTS.md를 생성한다. 빌드/테스트 명령, forbidden action, Spring Boot/JPA 규칙 포함 여부 검증 | Prompt 03, 11 |
| 실험 2: Pi vs Aider 변경 품질 비교 | 같은 N+1 문제를 Pi와 Aider에게 각각 수정시켜 diff 품질을 비교한다. 변경 파일 수, 테스트 추가 여부, 불필요한 스타일 변경 기준 평가 | Prompt 06, 07, 12 |
| 실험 3: Claude Code/Codex CLI와 UX 비교 | Pi가 부족한 점과 강한 점을 체감한다. 계획 수립, 파일 탐색, 명령 승인 UX, diff 리뷰, context 유지 능력 비교 | Prompt 01, 06 |
| 실험 4: Continue 스타일 PR Check 만들기 | AI 코딩 결과를 사람이 병합하기 전에 자동 점검하는 markdown check를 만든다 | Prompt 08, 09 |
| 실험 5: Pi Skill 또는 Extension 설계 | Spring Boot 코드 리뷰 스킬을 설계하고 작은 기능부터 구현한다 | Prompt 04, 05 |

---

## 프롬프트 팩 목록

| 파일 | 설명 |
|------|------|
| `00-research.md` | 외부 도구 리서치 요약 (참고 문서) |
| `01-tool-evaluation.md` | Prompt 01: AI 코딩 에이전트 도구 비교 분석 |
| `02-pi-lab-design.md` | Prompt 02: Pi 기반 실험실 설계 |
| `03-agents-md-generator.md` | Prompt 03: AGENTS.md 생성 |
| `04-spring-review-skill.md` | Prompt 04: Pi Extension/Skill 설계 |
| `05-security-policy.md` | Prompt 05: 안전한 실행 정책 설계 |
| `06-tool-benchmark.md` | Prompt 06: 도구 비교 실험 |
| `07-spring-work.md` | Prompt 07: Java/Spring Boot 실무 작업 |
| `08-pr-review.md` | Prompt 08: PR 리뷰 자동화 |
| `09-pr-check.md` | Prompt 09: Continue 스타일 PR Check |
| `10-mcp-design.md` | Prompt 10: MCP 연동 설계 |
| `11-context-engineering.md` | Prompt 11: Context Engineering |
| `12-experiment-template.md` | Prompt 12: 실험 기록 템플릿 |
| `13-product-design.md` | Prompt 13: 나만의 AI 개발 에이전트 제품화 |
| `14-plan-only.md` | Prompt 14: 코드 수정 전 계획만 세우기 |
| `15-minimal-change.md` | Prompt 15: 작게 수정하고 검증하기 |
| `16-ai-native-startup-playbook.md` | AI-네이티브 스타트업 프레임워크 (참고) |

---

## 참고 링크

### 도구

- Pi 공식 사이트: https://pi.dev/
- Pi GitHub: https://github.com/earendil-works/pi
- Claude Code 공식 페이지: https://claude.com/product/claude-code
- Claude Code GitHub: https://github.com/anthropics/claude-code
- OpenAI Codex CLI: https://developers.openai.com/codex/cli
- GitHub Copilot CLI: https://github.com/features/copilot/cli
- Aider: https://aider.chat/
- Cline: https://cline.bot/
- Goose: https://goose-docs.ai/
- Continue Docs: https://docs.continue.dev/
- OpenCode GitHub: https://github.com/opencode-ai/opencode
- Gemini CLI: https://developers.google.com/gemini-code-assist/docs/gemini-cli
- Qwen Code: https://qwen.ai/qwencode
- Cursor: https://cursor.com/
- Devin: https://devin.ai/

### 연구 논문

- AIDev: Studying AI Coding Agents on GitHub: https://arxiv.org/abs/2602.09185
- Configuring Agentic AI Coding Tools: https://arxiv.org/abs/2602.14690
- Building Effective AI Coding Agents for the Terminal: https://arxiv.org/abs/2603.05344
- Dive into Claude Code: https://arxiv.org/abs/2604.14228
- On the Use of Agentic Coding: https://arxiv.org/abs/2509.14745
