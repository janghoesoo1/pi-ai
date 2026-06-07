# 실험: 하네스 엔지니어링 Q&A 갭 분석 → lab 자산 보강

- 실험일: 2026-06-07
- 상태: **완료** (분석 + 신규 스킬 6개 추가)
- 대상: ai-coding-agent-lab 자체 (메타 작업)
- 입력 자료: `~/Downloads/harness_engineering_qa_original_and_summary.md` (황민호 수석 x AI Frenz "하네스 엔지니어링 60분 스팀팩" Q&A 정리 + 발표자료 §2.4 검증패턴)
- 참고: 발표 슬라이드 원본은 비공개(구글 인증)로 직접 접근 불가. Downloads 문서의 §2.4 요약을 근거로 사용.

## 1. 목적
황수석 Q&A/발표자료의 하네스 엔지니어링 원칙을 현재 lab과 비교(갭 분석)하고, 빠진 동적 메커니즘을 prompts/ 스킬로 보강한다.

## 2. 갭 분석 결과

### 이미 정렬된 것
| 황수석 자료 | lab 현황 |
|---|---|
| 가드레일은 코드/설정에 (프롬프트는 보안경계 아님) | ✅ `deny-guard.py` PreToolUse hook |
| CLAUDE.md = 프로젝트 주제 + 하네스 히스토리 | ◐ `context/lab-overview.md`가 대체 |
| 자율성 레벨 / 6단계 하네스 | ✅ AGENTS.md 명문화 |
| eval = 자산, 매주 6지표 | ✅ OPERATING-GUIDE (수집은 수동) |
| 무성 절단 금지 | ✅ lessons "exit code 맹신 금지" |

### 발견한 갭 → 보강
| # | 갭 | 보강 |
|---|---|------|
| 1 | "하네스 깎기" 3법 중 1법(직접편집)만 존재 | `17-agent-1on1.md`(1:1 포스트모템), `18-meta-tune.md`(메타 교정) |
| 2 | 교차검증이 정책엔 있으나 실행 메커니즘 없음 | `19-cross-verify.md` (codex 둘 다 설치 확인) |
| 3 | 발표자료 7검증패턴 미코드화, 심사패널(A/B/C) 없음 | `20-judge-panel.md`, `22-verification-patterns.md` |
| 4 | 오케스트레이터를 스킬로 (황수석 핵심) | `21-orchestrator.md` |
| 5 | 모델 티어링 정책 부재 | AGENTS.md에 "## 모델 티어링" 절 추가 |
| 6 | 자가 개선 루프(AutoResearch) 미구현 | **후속** — OMC `autoresearch` 연결 (이번 범위 외) |

## 3. 산출물 (결정론적)
| 항목 | 값 |
|------|-----|
| 신규 prompts 파일 | 6개 (17,18,19,20,21,22) |
| 수정 파일 | AGENTS.md(모델 티어링), lab-overview.md(마일스톤), decisions.md |
| 빌드/테스트 영향 | 없음 (md 문서만) |

## 3.5 실제 revfactory 구현과 대조 (유튜브 강의 자료 반영)

유튜브 라이브 페이지 본문/자막은 WebFetch로 접근 불가(JS 렌더링, 제목만 확인). 대신 강의가 가리키는
공개 레포 `revfactory/harness`·`revfactory/skills`의 **README·디렉토리 요약을 WebFetch로** 가져와 초안과 대조함.
> 주의(신뢰도): 파일 단위 git checkout이 아니라 페이지 요약 기반이다 — 신뢰도 "보도됨" 수준.
> 정밀 검증하려면 레포를 clone해 커밋 해시·읽은 파일 경로를 기록해야 한다. (codex 교차검증이 지적한 항목, §4.5)

| 항목 | 초안(내 추정) | 실제 revfactory | 반영 |
|------|---------------|------------------|------|
| agent-1on1 | experiments 데이터 포스트모템 | **에이전트로 1인칭 몰입(roleplay) 대화** + 기존 내용 보존(추가·강화 우선, 삭제는 명시 요청 시만) | 17에 1인칭 대화 절 + 보존 원칙 추가 |
| 교차검증 | 막연한 `codex exec` | `codex-cli` 스킬: `--sandbox read-only`, `codex review`, `--output-schema`, `--ask-for-approval` 안티패턴, "second opinion"=결론+원본동봉 | 19에 안전 패턴·신뢰도등급(확인/반증/미확인/상충) 반영 |
| 오케스트레이션 | lab 6단계만 | harness는 6 아키텍처 패턴(Pipeline/Fan-out·in/Expert Pool/Producer-Reviewer/Supervisor/Hierarchical) + Agent Teams vs Subagents | 21에 패턴 참조 추가 |

주의(혼동 방지): revfactory **harness의 6단계**(Domain Analysis→Team Arch→Agent Gen→Skill Gen→Integration→Validation)는
"하네스를 **만드는**" 메타 단계이고, 이 lab의 **6단계**(Preflight~Log)는 "작업을 **실행하는**" 단계다. 층위가 다르므로 합치지 않는다.

## 4. 교훈
- 황수석 하네스의 차별점은 "완성형"이 아니라 **계속 깎는 메타 하네스**라는 점. lab도 정적 산출(프롬프트팩)에서 동적 운영(깎기 루프)로 무게중심을 옮겨야 한다.
- 7번 검증패턴 "무성 절단 금지"(검토 범위 축소를 공개하는 원칙)는 lab의 "exit code 맹신 금지"(빌드 출력 검증 원칙)와 **상호 보완**된다. 같은 원칙은 아니지만 '겉보기 완료에 속지 말라'는 방향이 일치한다. (codex가 "같은 정신"은 과장이라 지적 → 표현 완화)

## 4.5 codex 교차검증 결과 (19-cross-verify dogfooding)

`19-cross-verify`를 codex(codex-cli 0.130)로 **실제 1회 실행**해 second opinion을 받음.
→ **결함을 실제로 잡아냄 = 스킬이 작동한다는 증명** (1번 "실전 검증"의 핵심 성과).

수정 반영(High):
- `codex review --sandbox`는 실제 CLI에 없는 옵션(오기) → `codex exec`만 `--sandbox` 유지하도록 19 수정. 로컬 `--help`로 확인.
- 21-orchestrator가 L1을 "승인 후 실행" 가능하게 읽힘 → "L1은 사람 전용, AI Execute 금지"로 수정.
- 21이 bf/pact 라우팅 전제 → AGENTS.md 정본(cross-folder 금지)과 정합화. path-guard hook이 강제.
- revfactory 대조 근거 부족 → §3.5에 "WebFetch 요약 기반, 신뢰도 보도됨" 명시.

다음 깎기 백로그(Med/Low — 이번엔 미반영, 무성 절단 금지로 공개):
- `20-judge-panel`: 원문은 "각 안 독립 구현·시뮬레이션 후 선택"인데 설계 비교까지만 → 구현/시뮬레이션 단계 추가 검토.
- 업무형 하네스 미신설: 원본 §2.5의 레거시 분석/아키텍처 의사결정/검증 리포트/장애 분석 하네스 → 별도 프롬프트로 자산화.
- `17-agent-1on1`: 롤플레이 답변을 experiments 증거와 분리 라벨링하는 규칙 추가.
- `18-meta-tune`: "최신 패턴 흡수"에 출처 검증·공식문서 우선·날짜 기록 규칙 추가.

교훈: **WebFetch 요약을 1차 출처로 신뢰하면 사실 오류가 하네스에 주입된다.** 외부 CLI 패턴은 반드시 로컬 `--help`로 검증. 그리고 교차검증(다른 모델)은 자기검토가 놓치는 결함을 실제로 잡는다 — 19는 유지할 가치가 있는 스킬로 1차 검증됨.

## 5. 다음에 반영할 것
- 신규 스킬(17~22)을 실제 작업에 1회 이상 적용해 eval(experiments) 누적 → 스킬이 작동하는지 검증.
- 갭 #6(자가 개선 루프): 수용률<70% 트리거 자동화. OMC autoresearch 연결 PoC.
- `21-orchestrator.md`를 다음 pact-conference 작업의 실제 진입점으로 사용해 6단계 구동 검증.

## 6. 결론
lab은 하네스의 "구조"(L1~L4, 6단계, 가드레일 hook)는 갖췄으나 "깎기 메커니즘"이 약했다. 이번에 1:1 포스트모템·메타 교정·교차 검증·심사 패널·검증 패턴 카탈로그·오케스트레이터 스킬을 추가해 황수석 자료의 동적 운영 모델에 정렬했다.
