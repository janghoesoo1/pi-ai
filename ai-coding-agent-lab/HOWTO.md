# HOWTO — 하네스 깎기 + 실사용 적용 가이드

이 lab을 (A) 어떻게 계속 "깎으며" 운영하는지, (B) 실제 프로젝트에 어떻게 적용하는지.
출처: 황민호 수석 "하네스 엔지니어링" Q&A 분석 + 실제 dogfooding(codex 교차검증) 결과.

> 한 줄 원칙: **하네스는 한 번 만들고 끝이 아니라, 약점 신호를 보고 그 부분만 계속 깎는 운영 자산이다.**

---

# A. pi-ai 하네스를 "깎는" 법

## 깎기 = 약점 자동탐지 → 그 스킬만 개정

핵심 루프 (주 1회, 또는 작업 끝날 때마다):

### ① 작업할 때 — 진입점은 `prompts/21-orchestrator.md`
6단계(Preflight→Plan→Approve→Execute→Verify→Log)를 따라간다. 끝나면 결과를
`experiments/YYYY-MM-DD-tool-task.md`에 점수(5축, 각 1~5)와 함께 기록한다.

### ② 약점 자동탐지 — 한 명령
```bash
python3 ai-coding-agent-lab/tools/eval-summary.py
# 또는 사이클 전체 점검:
bash ai-coding-agent-lab/tools/harness-cycle.sh
```
experiments 점수를 집계해 **임계(70% = 3.5/5) 미달 항목**을 찾아준다.
"어느 스킬을 깎아야 하는가"를 추측이 아니라 데이터로 알려준다.
(현재: 테스트 품질 2.5 → scaffold 계열 깎기 권고)

### ③ 지목된 스킬을 회고 — 깎기 도구 2종
- `prompts/17-agent-1on1.md` — 그 스킬과 1:1 대화(1인칭 몰입)로 실패·엣지케이스 발굴 → 개정 diff
- `prompts/18-meta-tune.md` — AI에게 "이 스킬 어떻게 더 좋게?" 물어 개정

> 깎기 = **전체 재작성이 아니라 지목된 스킬만 손본다.** 개정은 diff 제안 → 사람 적용.

### ④ 중요 산출물은 다른 모델로 교차검증 — `prompts/19-cross-verify.md`
```bash
codex exec --sandbox read-only \
  "Claude의 결론 + 원본 컨텍스트다. 적대적으로 검증해 틀린 곳·놓친 곳만 보고하라: <내용>"
```
자기검토가 못 잡는 결함을 잡는다. (실제로 이 프로젝트 보강의 High 결함 4개를 codex가 잡았다.)

### ⑤ 가드레일은 코드가 강제 (신경 안 써도 됨)
- `.claude/hooks/deny-guard.py` — 위험한 Bash 차단
- `.claude/hooks/path-guard.py` — lab 밖 파일 쓰기·`.env`·키 파일 차단
- `.claude/hooks/stop-eval.py` — 세션 종료 시 깎기 신호 자동 알림

### 안 고친 것은 반드시 공개 (무성 절단 금지)
한 번에 다 못 고치면 `experiments/*.md`의 "다음 깎기 백로그"에 남긴다.

---

# B. 실사용 프로젝트에 적용하는 법

## 철학: lab = 컨트롤 플레인, 코드 작업 = 그 프로젝트 폴더에서

lab은 방법·eval·규율의 보관소다. 실제 코드는 **그 프로젝트 폴더에서** 고친다.
lab 세션에서 외부 프로젝트를 고치면 `path-guard` hook이 차단한다(cross-folder 금지).

## 시나리오 예: "pact room-service에 store 단위테스트 추가"

왜 이 작업? — `eval-summary`가 **테스트 품질이 약하다**고 데이터로 지목했고,
lessons에도 "store 단위테스트 미작성"이 있다. **약점 신호 → 실제 작업**으로 이어진다.

```bash
# 실제 작업은 그 프로젝트에서 (lab이 아니라)
cd ~/work/pact-conference-api-harness && claude
```

세션 안에서 lab 스킬을 가져와 6단계로 구동:

| 단계 | lab 스킬 | 비고 |
|------|----------|------|
| Plan | `~/work/pi-ai/ai-coding-agent-lab/prompts/14-plan-only.md` | 코드 안 고치고 계획만 |
| Approve | 사람 승인 | pact는 개인·저위험 → L3 자율 가능 |
| Execute | `prompts/15-minimal-change.md` | store 단위테스트만 최소 추가 |
| Verify | `prompts/08-pr-review.md` + 전체 `./gradlew build` | exit code 말고 실제 출력 |
| Verify+ | `codex exec --sandbox read-only "이 테스트 diff 적대적 검증"` | 교차검증 |
| Log | 결과를 `~/work/pi-ai/.../experiments/`에 기록 | ← 가치를 lab으로 회수 |

## 프로젝트 등급별 가드레일
- **개인·저위험(pact-conference)**: 자율성 높게(L3~L4), PR까지 AI가. 자유롭게 실험.
- **회사·운영(bf/workspace, bf/ata-next-kotlin)**: 읽기·제안만. 자동머지·프로덕션 쓰기 금지.
  AGENTS.md 최상단에 보수적 가드레일. 푸시는 사람이.

## 새 프로젝트에 lab을 이식하는 3단계
1. 그 폴더에서 `prompts/03-agents-md-generator.md`로 **코드 기반 AGENTS.md** 생성
2. `policies/` 가드레일 + `.claude/hooks/`(deny-guard·path-guard) 복사
3. 작업하며 나온 교훈을 lab `context/lessons.md`로 회수 → 다음 프로젝트가 더 빨라진다(복리)

---

## 자동화 요약 (이 가이드를 손으로 안 해도 되게)

| 자동화 | 무엇을 | 어떻게 |
|--------|--------|--------|
| `tools/eval-summary.py` | 점수 집계 → 임계미달 탐지 | `python3 .../eval-summary.py` |
| `tools/harness-cycle.sh` | 깎기 사이클 전체 점검 한 번에 | `bash .../harness-cycle.sh` |
| `.claude/hooks/stop-eval.py` | 세션 끝에 깎기 신호 자동 알림 | settings.json Stop hook (자동) |
| `.claude/hooks/path-guard.py` | cross-folder·민감파일 쓰기 차단 | PreToolUse hook (자동) |
| `.claude/hooks/deny-guard.py` | 위험 Bash 차단 | PreToolUse hook (자동) |
