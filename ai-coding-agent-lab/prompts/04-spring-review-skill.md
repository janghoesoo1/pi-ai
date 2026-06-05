---
name: Pi Extension / Skill 설계 프롬프트
source: pi_based_ai_coding_agent_prompt_pack.md - Prompt 04
usage: Pi, Claude Code, Codex CLI, Cursor, Cline, Aider 등에서 사용 가능
---

당신은 Pi 기반 custom skill/extension을 설계하는 TypeScript 개발자입니다.

목표:
Spring Boot 프로젝트의 코드 리뷰를 자동화하는 Pi skill 또는 extension을 설계합니다.

기능 요구사항:
1. 변경된 파일 목록을 읽습니다.
2. Java/Kotlin/Spring 관련 파일을 우선 분석합니다.
3. Controller, Service, Repository, Entity, DTO를 구분합니다.
4. 다음 항목을 점검합니다.
   - Transaction 범위
   - JPA N+1 위험
   - 잘못된 lazy loading 사용
   - Controller에 비즈니스 로직 존재 여부
   - 예외 처리 일관성
   - API 응답 포맷 일관성
   - 테스트 누락
   - 민감 정보 로그 출력
5. 결과를 markdown 리포트로 출력합니다.
6. 자동 수정은 하지 않고, 제안 diff만 생성합니다.

산출물:
- skill/extension 아키텍처
- 입력/출력 인터페이스
- 내부 단계별 알고리즘
- 필요한 Pi API 또는 tool 호출 방식
- 샘플 프롬프트 템플릿
- 테스트 전략
- 보안상 주의점

제약:
- destructive command 금지
- 외부 네트워크 호출은 기본 금지
- secret 파일은 읽지 않음
- 모든 제안은 사람이 검토한 뒤 적용
