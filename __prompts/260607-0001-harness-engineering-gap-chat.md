# 260607-0001 하네스 엔지니어링 Q&A 갭 분석 → lab 스킬 보강

## 사용자 요청
황민호 수석 x AI Frenz "하네스 엔지니어링 60분 스팀팩" 발표자료(구글 슬라이드)와
`~/Downloads/harness_engineering_qa_original_and_summary.md` Q&A 정리를 분석해서,
이 프로젝트의 pi-ai agent(ai-coding-agent-lab)를 다듬을 방법이 있는지 찾아달라.
→ 이어서 "네 모두 진행" (갭 기록 + 신규 프롬프트 작성).
→ 추가: 유튜브 라이브(https://www.youtube.com/live/_20mengjS78)에 강의 자료가 있다는 제보.

## AI 응답 요약

### 1. 분석
- 발표 슬라이드 원본은 비공개(구글 인증)라 직접 열지 못함 → Downloads 문서 §2.4(슬라이드 검증패턴 요약)를 근거로 사용.
- lab은 황수석 자료의 "하네스=업무 운영 구조"를 이미 ~80% 구현(6단계 하네스, 자율성 L1~L4, eval 6지표, deny-guard.py 강제점).
- 빠진 것 = 황수석이 강조한 **동적 메커니즘**("하네스를 깎는다").

### 2. 발견한 갭 → 보강
| # | 갭 | 보강 |
|---|---|------|
| 1 | "깎기" 3법 중 직접편집만 존재 | 17-agent-1on1, 18-meta-tune |
| 2 | 교차검증 정책만 있고 실행 없음 | 19-cross-verify |
| 3 | 7검증패턴·심사패널 미코드화 | 20-judge-panel, 22-verification-patterns |
| 4 | 오케스트레이터가 산문뿐 | 21-orchestrator |
| 5 | 모델 티어링 정책 부재 | AGENTS.md 절 추가 |
| 6 | 자가 개선 루프 없음 | 후속(OMC autoresearch 연결) |

### 3. 산출물
- 신규 prompts 6개: 17~22
- 수정: AGENTS.md(모델 티어링), context/lab-overview.md(상태·마일스톤), context/decisions.md
- 기록: experiments/2026-06-07-harness-engineering-gap.md

### 4. 핵심 인사이트
- 황수석 하네스의 차별점은 "완성형"이 아니라 **계속 깎는 메타 하네스**.
- lab도 정적 산출(프롬프트팩) → 동적 운영(깎기 루프)으로 무게중심 이동.
- 발표자료 "무성 절단 금지" = lab의 "exit code 맹신 금지" 교훈과 같은 정신(좋은 하네스의 수렴점).

## 민감정보
없음 (문서 작업만).
