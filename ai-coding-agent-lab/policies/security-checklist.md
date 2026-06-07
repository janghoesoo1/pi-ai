# Security Checklist

AI 코딩 에이전트 사용 시 보안 체크리스트.

## 1. Risk Model
- 파일 수정으로 인한 코드 손상
- 명령 실행으로 인한 시스템 손상
- 시크릿 유출
- 운영 환경 영향

## 2. File Access Policy
- 프로젝트 디렉토리 내 파일만 접근
- .env, .ssh, credentials 파일 접근 금지
- 홈 디렉토리 설정 파일 수정 금지

## 3. Network Access Policy
- localhost만 기본 허용
- 외부 API 호출은 사전 승인 필요
- 패키지 설치(npm, gradle)는 커밋된 lockfile이 있고 사람이 승인한 경우에만 허용. 신뢰 불가 출처 또는 임시(ad-hoc) 설치 금지

## 4. Secret Handling Policy
- 시크릿은 환경 변수로만 관리
- 코드에 하드코딩 절대 금지
- 로그에 시크릿 출력 금지
- .env 파일은 .gitignore에 포함

## 5. Git Safety Policy
- force push 금지
- main/master/develop 직접 commit 금지
- 새 브랜치에서 작업 후 PR

## 6. Review-before-apply Policy
- 모든 자동 수정은 git diff로 검토
- destructive command 실행 전 사전 승인
- 사람이 승인해야 다음 단계 진행

## 7. Sandbox 실행 패턴
- Docker 컨테이너 내에서 실험 권장
- 샘플 프로젝트에서 먼저 검증
- 회사 코드 직접 사용 금지

## 8. 사고 발생 시 복구 절차
1. 즉시 에이전트 중단
2. git log로 마지막 안전 상태 확인
3. git stash 또는 git checkout으로 복구
4. 영향 범위 파악
5. 원인 분석 및 정책 업데이트

## 9. Harness 가드레일 (코드/설정 레벨)

프롬프트 지시는 보안 경계가 아니다. 다음은 런타임에 강제해야 할 협상 불가 항목이다.

- 실행/일일 비용 상한 설정
- 재시도 상한 (무한 루프 방지)
- 최대 도구 호출 깊이 제한
- 에이전트별 스코프 자격증명 (최소 권한)
- 승인 없는 프로덕션 쓰기 금지
- 코드 자동 머지 금지
- 전체 에이전트 킬 스위치 확보

## 10. 자율성 레벨별 보안 규칙

| 레벨 | 보안 규칙 |
|------|----------|
| L1 (사람 전용) | 에이전트 실행 불가. 사람만 수행 |
| L2 (AI 준비 + 사람 승인) | 출력을 사람이 반드시 검토 후 적용. git diff 확인 필수 |
| L3 (AI 실행 + 사람 감독) | 실행 허용하되 결과 로그 필수. 금지 명령 자동 차단 |
| L4 (한계 내 자율) | 사전 정의된 명령만 실행 가능. 범위 이탈 시 즉시 중단 |
