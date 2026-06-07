# .claude/hooks — 가드레일 강제점 (enforcement)

이 디렉토리는 lab의 핵심 원칙을 **실제로 강제**한다:

> 가드레일은 코드와 설정에. 프롬프트 지시는 보안 경계가 아니다.
> (`OPERATING-GUIDE.md`, `policies/security-checklist.md`)

기존에는 `policies/denied-commands.md`가 산문 목록일 뿐 실행 차단력이 없었다.
이 hook이 그 격차를 메운다(감사 H1).

## deny-guard.py

- **트리거**: `settings.json`의 `PreToolUse` → `matcher: "Bash"`. 즉 Bash 도구 호출 직전에 실행된다.
- **입력**: stdin으로 도구 호출 JSON(`tool_input.command`).
- **동작**: 명령을 정규식으로 검사해 `policies/denied-commands.md`의 금지 패턴과 매칭되면
  - `exit 2` → **호출 차단**, stderr 메시지가 에이전트에게 전달됨.
  - 매칭 없으면 `exit 0` → 허용.
- **범위**: 정규식 기반 **PoC**다. 완전한 샌드박싱이 아니라 흔한 위험 패턴의 방어선이다.
  쉘 난독화(base64, 변수치환 등)는 우회 가능 — 심층 방어를 원하면 컨테이너/권한 분리를 병행한다.

## 차단 패턴(요약)

`rm -rf /|~|$HOME`, `rm -rf .git`, `git push --force`, `git filter-branch/filter-repo`,
`git reflog expire`, `git gc --prune=now`, `git update-ref -d`, `curl|wget … | sh`,
`.env` 읽기, `.ssh/` 접근, `printenv`, AWS/GCP 시크릿 접근, `kubectl delete`,
`terraform destroy`, `docker system prune -a`, `chmod 777`, `dd if=`, `mkfs`, `sudo`, fork bomb.

## 유지보수

- 패턴은 **`policies/denied-commands.md`와 항상 동기화**한다(단일 정본은 denied-commands).
- 패턴 추가/수정 시 아래로 동작 검증:
  ```bash
  echo '{"tool_name":"Bash","tool_input":{"command":"sudo rm -rf /"}}' \
    | python3 .claude/hooks/deny-guard.py; echo "exit=$?"   # → exit=2
  echo '{"tool_name":"Bash","tool_input":{"command":"ls -la"}}' \
    | python3 .claude/hooks/deny-guard.py; echo "exit=$?"   # → exit=0
  ```
- 의존성 없음(Python 3 표준 라이브러리만). hook 자체 오류 시에는 가용성 우선으로 통과(`exit 0`)한다.
