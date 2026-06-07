# Allowed Commands

에이전트가 실행 가능한 명령 목록.

## 파일 읽기
- cat, less, head, tail (프로젝트 파일만)
- find, ls, tree
- grep, rg, ag

## 빌드
- ./gradlew build
- ./gradlew test
- ./mvnw compile
- ./mvnw test
- npm install
- npm run build
- npm test

## Git (Read-only)
- git status
- git diff
- git log
- git branch
- git show

## Git (Write - 승인 필요)
- git add (특정 파일)
- git commit
- git checkout -b (새 브랜치 생성)
- git reset --hard (사람 승인 필요)
- git rebase -i (사람 승인 필요)

## 기타
- curl (localhost만)
- docker-compose up/down (로컬 개발 환경만)
