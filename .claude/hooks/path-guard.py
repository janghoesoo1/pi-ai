#!/usr/bin/env python3
"""PreToolUse guard for file-writing tools (Edit/Write/NotebookEdit/MultiEdit).

deny-guard.py(Bash 전용)를 보완하는 두 번째 강제점이다.
lab의 두 원칙을 코드로 강제한다:
  1) cross-folder 쓰기 금지 — 프로젝트 루트 밖 파일 수정 차단
     (lessons: "동시 세션 산출물/노이즈가 워킹트리에" + lab-overview "cross-folder 금지")
  2) 민감 파일 쓰기 금지 — .env / SSH 키 / .pem 류

규약: exit 2 = 차단(stderr가 에이전트에게 전달됨), exit 0 = 허용.
주의: PoC 방어선이다. 완전한 샌드박싱이 아니다.
"""
import sys
import json
import os

try:
    data = json.load(sys.stdin)
except Exception:
    # 파싱 실패 시 가용성 우선 — 차단하지 않는다(hook 오류로 작업이 막히지 않게).
    sys.exit(0)

tool = data.get("tool_name")
if tool not in ("Edit", "Write", "NotebookEdit", "MultiEdit", None):
    sys.exit(0)

ti = data.get("tool_input") or {}
path = ti.get("file_path") or ti.get("notebook_path") or ""
if not path:
    sys.exit(0)


def block(reason: str) -> None:
    print(
        f"path-guard 차단: {reason}\n"
        f"대상: {path}\n"
        f"lab 원칙(cross-folder 쓰기 금지 / 민감 파일 보호) 위반. "
        f"다른 프로젝트 작업은 그 폴더에서 별도 세션으로, 민감 파일은 사람이 직접 다루세요.",
        file=sys.stderr,
    )
    sys.exit(2)


# --- 1) 민감 파일명 차단 (프로젝트 내부라도) ---
base = os.path.basename(path)
if (
    base == ".env"
    or base.startswith(".env.")
    or "id_rsa" in base
    or "id_ed25519" in base
    or base.endswith(".pem")
    or base.endswith(".key")
):
    block(f"민감 파일 쓰기 금지 패턴: '{base}'")

# --- 2) 프로젝트 루트 밖 쓰기 차단 ---
proj = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
proj = os.path.realpath(proj)
target = os.path.realpath(os.path.abspath(os.path.expanduser(path)))

if not (target == proj or target.startswith(proj + os.sep)):
    block(f"프로젝트 루트({proj}) 밖 파일 수정")

sys.exit(0)
