# 실험: 스캐폴드된 room-service를 typed 도메인으로 완성

- 실험일: 2026-06-05
- 상태: **완료** (lab 두 번째 eval)
- 대상: pact-conference-api-harness (개인·저위험)
- 도구: Claude Code
- 브랜치: `experiment/scaffold-room-service`
- 선행: [2026-06-05-claudecode-scaffold-room.md] (스캐폴딩 골격)

## 1. 목적
첫 실험에서 harness.sh가 만든 untyped `Map<String,Any>` 골격을, AGENTS.md의 컨벤션(도메인 모델 + DTO + ApiResponse + 검증 + 테스트)에 맞춰 완성한다. session-service를 레퍼런스로 삼는다.

## 2. 수행
- `common/model/Room` 도메인 추가 (Session 모델과 동일 패턴)
- `RoomStoreInterface`/`RoomStore` 타입화 (getRooms/getRoom/addRoom/... + 샘플 데이터)
- `RoomDto`: Create/Update Request(`@NotBlank`/`@Positive`/`@Size` 검증) + Response(`from`)
- `RoomController`: ApiResponse 엔벨로프, 201+Location, 204, 404 — SessionController와 동형
- `MetricsConfig`: `getAll()` → `getRooms()` 적응
- `RoomControllerTest`: 7개 (목록/단건/404/생성/검증400/수정/삭제)
- `build.gradle.kts`: `spring-boot-starter-validation` 명시 추가

## 3. 결과 (결정론적 지표)
| 지표 | 값 |
|------|-----|
| RoomControllerTest | **7 tests, 0 failure** (검증 400 포함) |
| 전체 빌드 | BUILD SUCCESSFUL (1m23s, Testcontainers 포함 전 모듈 그린) |
| 컨벤션 일치 | session-service와 동형 (DTO·ApiResponse·ProblemDetail 위임) |

## 4. 발견한 실제 버그 (중요)
**harness.sh 스캐폴드의 gateway 주입 버그**: `new-service`가 `ProxyController.kt`에 추가한
`@Value("${services.room.url:...}")` 의 `$`가 **escape되지 않아**(`\$` 아님) Kotlin 문자열 보간으로
해석 → `gateway:compileKotlin` 실패. 기존 필드(session/attendee/cfp)는 `\${...}`로 정상.
→ 수동으로 `\$` 추가해 수정. **harness.sh의 sed/heredoc 이스케이프 결함**.

## 5. 교훈
- **스캐폴드 직후 단일 모듈만 빌드하면 gateway 회귀를 놓친다.** 첫 실험에서 `:room-service:build`만 그린이라 통과로 봤으나, 스캐폴드는 gateway도 수정했고 그건 깨져 있었다. **스캐폴딩 후에는 반드시 전체 `./gradlew build`로 횡단 영향까지 검증.**
- harness.sh가 만든 골격은 "컴파일되는 단일 서비스"일 뿐, gateway 통합까지 검증된 게 아님.

## 6. 점수 (1~5)
| 평가 항목 | 점수 | 비고 |
|-----------|:---:|------|
| 정확성 | 5 | 컨벤션 정확히 일치, 전 모듈 그린 |
| 변경 통제 | 5 | 범위 명확, 회귀까지 추적·수정 |
| 테스트 품질 | 4 | 컨트롤러 7개(검증 포함). store 단위테스트·Pact는 미작성 |
| 설명 품질 | 5 | |
| 안전성 | 5 | 브랜치 격리, 전체 빌드 검증 |

## 7. 다음에 반영할 것
- harness.sh 개선 PR 후보: gateway `@Value` 주입 시 `\$` 이스케이프 + 스캐폴드 말미 `./gradlew :gateway:compileKotlin` 자동 검증
- room-service: store 단위테스트 + (선택) Pact consumer 추가 시 3번째 eval

## 8. 결론
"스캐폴드 골격 → 컨벤션 준수 완성"은 레퍼런스(session-service)가 있을 때 L3(사람 감독) 수준으로 신뢰 가능.
단, **스캐폴딩 도구(harness.sh) 자체의 결함**을 사람이 잡아야 하므로, 스캐폴드 산출물은 항상 전체 빌드로 검증한다.
