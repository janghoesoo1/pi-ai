# 실험: AGENTS.md 절차로 harness.sh 신규 서비스 스캐폴딩

- 실험일: 2026-06-05
- 상태: **완료** (lab 첫 실제 eval)
- 대상 프로젝트: pact-conference-api-harness (개인·저위험)
- 도구: Claude Code (에이전트) + harness.sh (결정론적 스캐폴딩 CLI)
- 브랜치: `experiment/scaffold-room-service` (미머지)

## 1. 실험 목적
방금 생성한 `AGENTS.md`의 운영 절차(Plan → dry-run → Execute → Verify)를 실제로 밟아, harness.sh로 새 마이크로서비스(room-service)를 추가하고 빌드 그린까지 도달하는 워크플로우를 검증한다.

## 2. 진행 (Harness 6단계 적용)
| 단계 | 수행 |
|------|------|
| Preflight | AGENTS.md 로드, 금지 명령 확인, 격리 브랜치 생성 |
| Plan/Approve | `./harness.sh new-service --name room --port 8084 --path /rooms --dry-run`로 7단계 변경 미리보기 |
| Execute | dry-run 없이 실제 실행 |
| Verify | `./harness.sh validate` 전 항목 그린 + `./gradlew :room-service:build` 성공 |
| Log | 본 문서 + tool-insights 갱신 |

## 3. 결과 (결정론적 지표)
| 지표 | 값 |
|------|-----|
| 빌드 | BUILD SUCCESSFUL (9s) |
| validate | 전 항목 정상 (포트·게이트웨이 라우팅·prometheus·k8s) |
| 변경 파일 수 | 17 files, +284 / -4 |
| 배선된 횡단 관심사 | gradle 모듈 등록, gateway ProxyController+yml, k8s manifest, prometheus job, start/stop 스크립트 |
| 사람 개입 | `.bak` 백업 6개 수동 정리 1회 |

## 4. 잘한 점
- dry-run 미리보기가 실제 실행과 정확히 일치 → 예측 가능, 승인 게이트로 적합
- 단일 명령으로 5개 횡단 관심사(빌드·게이트웨이·관측·k8s·기동스크립트)를 일관되게 배선
- 컨벤션(패키지 구조 controller/dto/store/config, ApiResponse 형태) 자동 준수 → 즉시 컴파일

## 5. 위험했던 점 / 한계
- 스캐폴드 store가 **`Map<String, Any>` (untyped)** + TODO 주석 → AGENTS.md의 "도메인 모델/DTO 사용" 규칙 미충족. 운영 코드로 쓰려면 `common`에 도메인 추가 + 타입 교체 필요
- **테스트 미생성** (test 디렉토리만 생성, 파일 없음) → 80% 커버리지 규칙 미충족
- `.bak` 파일을 작업 트리에 남김 → 정리 누락 시 커밋 오염 위험
- JPA 서비스였다면 빌드 실패했을 것(scaffold가 JPA 자동설정 제외 + kotlin-jpa 미적용) — 이번엔 in-memory라 우회됨

## 6. 점수 (1~5)
| 평가 항목 | Claude Code + harness.sh | 비고 |
|-----------|:---:|------|
| 정확성 | 5 | 의도대로 정확히 스캐폴딩 |
| 변경 통제 | 4 | 범위 명확하나 .bak 잔여 |
| 테스트 품질 | 1 | 테스트 미생성 |
| 설명 품질 | 5 | 단계별 로그 명확 |
| 안전성 | 4 | dry-run+백업+브랜치 격리 양호, 단 untyped store |

## 7. 다음 실험에서 바꿀 점
- harness.sh 개선 후보: (a) 기본 테스트 1개 생성 (b) `.bak` 자동 정리/`.gitignore` (c) `--jpa` 플래그 시 kotlin-jpa+exclude 해제 자동 포함
- 후속 작업: room-service에 typed 도메인(`common/model/Room`) + DTO + 컨트롤러 구현 → 두 번째 eval

## 8. 결론
스캐폴딩 워크플로우는 **L4(한계 안 자율) 수준으로 신뢰 가능** — 결정론적이고 dry-run으로 검증 가능. 단, 산출물은 "동작하는 골격"이지 "완성된 서비스"가 아니므로, 도메인 구현·테스트는 여전히 L3(사람 감독) 작업으로 남는다.
