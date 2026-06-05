# Denied Commands

에이전트에게 절대 금지된 명령 목록.

## 파일 삭제
- rm -rf /
- rm -rf .git
- rm -rf ~ 또는 rm -rf $HOME

## Git 위험 명령
- git push --force
- git reset --hard (승인 없이)
- git rebase -i (승인 없이)

## 시크릿 노출
- cat ~/.ssh/*
- cat .env
- printenv
- aws secretsmanager get-secret-value
- gcloud secrets versions access

## 인프라 파괴
- kubectl delete
- terraform destroy
- docker system prune -af

## 운영 환경
- 운영 DB에 직접 write하는 모든 명령
- 프로덕션 서버 SSH 접근
- 프로덕션 환경 변수 수정
