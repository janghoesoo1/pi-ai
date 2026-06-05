---
name: 안전한 실행 정책 설계 프롬프트
source: pi_based_ai_coding_agent_prompt_pack.md - Prompt 05
usage: Pi, Claude Code, Codex CLI, Cursor, Cline, Aider 등에서 사용 가능
---

당신은 AI 코딩 에이전트 보안 아키텍트입니다.

Pi 또는 기타 CLI 기반 AI 코딩 에이전트를 사용할 때 필요한 실행 정책을 설계해 주세요.

상황:
- 에이전트는 파일을 읽고 쓸 수 있습니다.
- bash 명령을 실행할 수 있습니다.
- git 명령을 사용할 수 있습니다.
- 테스트 명령을 실행할 수 있습니다.
- 실수로 credential, .env, SSH key, 운영 DB 접속정보에 접근하면 안 됩니다.

작성할 문서:
1. Risk Model
2. Allowed Commands
3. Denied Commands
4. File Access Policy
5. Network Access Policy
6. Secret Handling Policy
7. Git Safety Policy
8. Review-before-apply Policy
9. Sandbox/Docker 실행 패턴
10. 사고 발생 시 복구 절차

반드시 포함할 금지 예시:
- rm -rf /
- rm -rf .git
- git push --force
- cat ~/.ssh/*
- cat .env
- printenv
- aws secretsmanager get-secret-value
- kubectl delete
- terraform destroy
- 운영 DB에 직접 write하는 명령

결과는 `policies/security-checklist.md`로 저장할 수 있는 형태로 작성해 주세요.
