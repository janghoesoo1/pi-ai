# AI-네이티브 프레임워크 실험실 반영

- 날짜: 2026-06-05
- 타입: chat
- 작업: AI-네이티브 스타트업 프레임워크(cyberfund)를 실험실에 반영

## 사용자 요청

1. AI-네이티브 스타트업 글을 읽기 좋은 md 파일로 만들어줘
2. 이 글의 프레임워크를 실험실에 반영하거나, 별도 문서로 정리하는 작업도 해줘

## AI 작업 내용

### 1. 플레이북 문서 생성
- `prompts/16-ai-native-startup-playbook.md`: 원문을 구조화된 markdown으로 정리

### 2. 운영 가이드 생성
- `OPERATING-GUIDE.md`: 6단계 프레임워크를 실험실 구체적 운영 방법으로 변환

### 3. 컨텍스트 시스템 신규 생성
- `context/lab-overview.md`: 실험실 상태
- `context/tool-insights.md`: 도구별 학습 (빈 템플릿)
- `context/decisions.md`: 결정 로그 (초기 3건)
- `context/lessons.md`: 교훈 로그 (빈 템플릿)

### 4. 기존 파일 업데이트
- `README.md`: 운영 프레임워크 섹션 추가, 디렉토리 구조 갱신, 프롬프트 목록 전체(17개) 반영
- `AGENTS.md`: Autonomy Levels(L1~L4) 추가, Harness 6단계 추가, 빌드 명령 Gradle로 수정
- `policies/security-checklist.md`: 하네스 가드레일(섹션 9) + 자율성 레벨별 보안(섹션 10) 추가

## 프레임워크 매핑

| 프레임워크 개념 | 실험실 대응 |
|---------------|------------|
| 업무 매핑 + 자율성 레벨 | AGENTS.md Autonomy Levels |
| 컨텍스트 시스템 | context/ 디렉토리 |
| 하네스 6단계 | AGENTS.md Harness + policies/ |
| 스킬 인코딩 | prompts/ 파일 |
| eval | experiments/ 점수 기준 |
| 피드백 루프 | OPERATING-GUIDE.md 주간 리뷰 |
