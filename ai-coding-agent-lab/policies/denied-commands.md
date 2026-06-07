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

## 원격 코드 실행 / 공급망
- `curl ... | sh` — 원격 스크립트 직접 실행
- `wget ... | bash` — 원격 스크립트 직접 실행
- `npm install` (신뢰 불가 출처 또는 lockfile 없이)
- `pip install` (검증 안 된 패키지)
- `gem install` (검증 안 된 패키지)

## 디스크 / 권한
- `chmod 777`
- `chmod -R` (광범위한 대상)
- `dd`
- `mkfs`
- `chown` (광범위한 대상)
- `sudo` (원칙적으로 금지)
- fork bomb: `:(){ :|:& };:`

## Git 히스토리 파괴 (추가)
- `git filter-branch`
- `git filter-repo`
- `git reflog expire --expire=now --all`
- `git gc --prune=now`
- `git update-ref -d`
