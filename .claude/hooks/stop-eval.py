#!/usr/bin/env python3
"""Stop hook — 세션 종료 시 깎기 신호 자동 알림.

HOWTO.md §A 의 깎기 루프를 자동화한다. 세션이 끝날 때 eval-summary를 돌려
임계(70%) 미달 항목이 있으면 깎기 권고를 사용자에게 보여준다.
임계 미달이 없으면 조용히 통과한다(노이즈 최소화).

규약: exit 0 = 통과(세션 종료 허용). 차단하지 않는다 — 알림 전용.
무한 루프 방지: stop_hook_active 가 true면 즉시 통과.
"""
import sys
import os
import json
import subprocess

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

# Stop hook 재진입 방지
if data.get("stop_hook_active"):
    sys.exit(0)

proj = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
script = os.path.join(proj, "ai-coding-agent-lab", "tools", "eval-summary.py")
if not os.path.exists(script):
    sys.exit(0)

try:
    out = subprocess.run(
        [sys.executable, script],
        capture_output=True, text=True, timeout=20,
    ).stdout
except Exception:
    sys.exit(0)

# "깎기 권고" 섹션에서 임계 미달 라인만 추출
lines = out.splitlines()
flagged = [ln for ln in lines if "임계 미달" in ln and ln.strip().startswith("-")]

if flagged:
    msg = ["", "🪚 하네스 깎기 신호 (세션 종료 점검):"]
    msg += [f"  {ln.strip()}" for ln in flagged]
    msg.append("  → prompts/17-agent-1on1.md 또는 18-meta-tune.md 로 해당 스킬을 깎으세요.")
    msg.append("  (전체: bash ai-coding-agent-lab/tools/harness-cycle.sh)")
    print("\n".join(msg), file=sys.stderr)

sys.exit(0)
