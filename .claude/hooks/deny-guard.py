#!/usr/bin/env python3
"""PreToolUse guard for the Bash tool.

이 스크립트는 "가드레일은 코드와 설정에, 프롬프트 지시는 보안 경계가 아니다"
원칙의 실제 강제점(enforcement point)이다. policies/denied-commands.md의
금지 명령 패턴을 런타임에 차단한다.

규약: exit 2 = 차단(stderr가 에이전트에게 전달됨), exit 0 = 허용.
대상 도구: Bash (settings.json의 matcher로 한정).

주의: 이것은 정규식 기반 PoC다. 완전한 샌드박싱이 아니라 흔한 위험
패턴에 대한 방어선이다. 패턴은 policies/denied-commands.md와 동기화해야 한다.
"""
import sys
import json
import re

try:
    data = json.load(sys.stdin)
except Exception:
    # 입력 파싱 실패 시 차단하지 않는다(가용성 우선). hook 오류로 작업이 막히지 않게.
    sys.exit(0)

# 다른 도구 이벤트가 들어오면 통과(설정상 Bash만 매칭되지만 방어적으로 확인)
if data.get("tool_name") not in ("Bash", None):
    sys.exit(0)

cmd = ((data.get("tool_input") or {}).get("command") or "")
if not cmd.strip():
    sys.exit(0)

# (정규식, 사람이 읽을 라벨) — policies/denied-commands.md와 동기화
PATTERNS = [
    (r'\brm\s+-rf\s+(/|~|\$HOME)\b', 'rm -rf 시스템/홈 경로'),
    (r'\brm\s+-rf\s+\.git\b', 'rm -rf .git'),
    (r'\bgit\s+push\b.*(--force|\s-f\b)', 'git push --force'),
    (r'\bgit\s+filter-branch\b', 'git filter-branch'),
    (r'\bgit\s+filter-repo\b', 'git filter-repo'),
    (r'\bgit\s+reflog\s+expire\b', 'git reflog expire'),
    (r'\bgit\s+gc\b.*--prune=now', 'git gc --prune=now'),
    (r'\bgit\s+update-ref\s+-d\b', 'git update-ref -d'),
    (r'\b(curl|wget)\b.*\|\s*(sudo\s+)?(sh|bash|zsh)\b', '원격 스크립트 파이프 실행 (curl|sh)'),
    (r'(^|\s)cat\s+[^\n]*\.env\b', '.env 읽기'),
    (r'\.ssh/', 'SSH 키 경로 접근'),
    (r'(^|\s)printenv(\s|$)', 'printenv (환경변수 덤프)'),
    (r'\baws\s+secretsmanager\s+get-secret-value\b', 'AWS 시크릿 접근'),
    (r'\bgcloud\s+secrets\s+versions\s+access\b', 'GCP 시크릿 접근'),
    (r'\bkubectl\s+delete\b', 'kubectl delete'),
    (r'\bterraform\s+destroy\b', 'terraform destroy'),
    (r'\bdocker\s+system\s+prune\b.*-a', 'docker system prune -a'),
    (r'\bchmod\s+(-R\s+)?777\b', 'chmod 777'),
    (r'(^|\s)dd\s+if=', 'dd if='),
    (r'(^|\s)mkfs', 'mkfs'),
    (r'(^|\s)sudo(\s|$)', 'sudo'),
    (r':\(\)\s*\{\s*:\s*\|\s*:\s*&\s*\}\s*;\s*:', 'fork bomb'),
]

for pat, label in PATTERNS:
    if re.search(pat, cmd):
        print(
            f"deny-guard 차단: '{label}' 패턴 감지 — policies/denied-commands.md 위반.\n"
            f"명령: {cmd}\n"
            f"필요하면 사람이 직접 검토·실행하세요(에이전트 자동 실행 금지).",
            file=sys.stderr,
        )
        sys.exit(2)

sys.exit(0)
