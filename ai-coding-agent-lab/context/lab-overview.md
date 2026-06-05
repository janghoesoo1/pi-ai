# Lab Overview

## 목적
Pi를 연구용/확장용 기반으로 삼고, Claude Code/Codex CLI/Aider/Cline/Goose/Continue의 장점을 벤치마킹해서 "내 개발 방식에 맞는 AI 코딩 운영체계"를 만든다.

## 현재 상태
- 실험실 구조 생성 완료 (2026-06-05)
- 프롬프트 팩 16개 (00~15) + AI-네이티브 플레이북 (16) 준비 완료
- sandbox/sample-spring-api: Spring Boot 샘플 (의도적 문제 7가지 포함) 생성 완료
- sandbox/sample-react-app: Next.js 샘플 생성 완료
- 실험 미실행 상태

## 핵심 제약
- 회사 코드 사용 금지 (sandbox만 사용)
- destructive command 기본 금지
- 모든 자동 수정은 git diff로 검토 가능
- 자동 머지 금지, 프로덕션 쓰기 금지

## 다음 마일스톤
- 실험 1~5 실행
- context/tool-insights.md 채우기
- eval 기준 정립
