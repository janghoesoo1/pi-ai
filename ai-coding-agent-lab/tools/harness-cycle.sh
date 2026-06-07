#!/usr/bin/env bash
# 하네스 깎기 사이클 점검 — 한 명령으로 깎기 상태를 본다.
# HOWTO.md §A 의 ②단계 자동화. eval 집계 + 미기록 경고 + 다음 액션 권고.
set -euo pipefail

LAB="$(cd "$(dirname "$0")/.." && pwd)"

echo "════════════════════════════════════════════"
echo " 하네스 깎기 사이클 점검"
echo "════════════════════════════════════════════"

echo
echo "▶ 1) eval 집계 (약점 자동탐지)"
echo "────────────────────────────────────────────"
python3 "$LAB/tools/eval-summary.py"

echo
echo "▶ 2) 도구 가용성"
echo "────────────────────────────────────────────"
for t in claude codex; do
  if command -v "$t" >/dev/null 2>&1; then
    echo "  ✓ $t 사용 가능 ($("$t" --version 2>/dev/null | head -1))"
  else
    echo "  ✗ $t 없음 — 교차검증(19) 제한"
  fi
done

echo
echo "▶ 3) 최근 실험 기록 (최신 5건)"
echo "────────────────────────────────────────────"
ls -1t "$LAB/experiments"/*.md 2>/dev/null | head -5 | while read -r f; do
  echo "  - $(basename "$f")"
done

echo
echo "▶ 4) 다음 액션 권고"
echo "────────────────────────────────────────────"
echo "  - 위 '임계 미달' 항목이 있으면:"
echo "      prompts/17-agent-1on1.md 또는 18-meta-tune.md 로 해당 스킬 회고"
echo "  - 중요 산출물은 prompts/19-cross-verify.md (codex exec --sandbox read-only) 로 교차검증"
echo "  - 실제 코드 작업은 그 프로젝트 폴더에서 (lab 밖은 path-guard 차단)"
echo "════════════════════════════════════════════"
