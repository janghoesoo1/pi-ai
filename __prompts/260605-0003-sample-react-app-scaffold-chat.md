# 260605-0003 | sample-react-app 스캐폴딩 | chat

## 요청

sample-spring-api와 연동하는 간단한 Next.js 프론트엔드를 `/ai-coding-agent-lab/sandbox/sample-react-app/` 경로에 생성.

npm 프로젝트 최소 구성. Next.js 14 App Router 기반.

## 작업 내용

다음 파일들을 생성:

- `package.json` — Next.js 14.2.0 + React 18.3.1 + TypeScript 구성
- `tsconfig.json` — strict 모드, bundler moduleResolution, `@/*` path alias
- `next.config.js` — 빈 config
- `.gitignore` — node_modules, .next, out, .env*.local
- `src/app/layout.tsx` — RootLayout, 한국어 lang 설정
- `src/app/page.tsx` — `/api/users` 서버 컴포넌트 fetch, 테이블 렌더링

## 결과

6개 파일 생성 완료. 디렉토리 구조:

```
sample-react-app/
├── .gitignore
├── next.config.js
├── package.json
├── tsconfig.json
└── src/
    └── app/
        ├── layout.tsx
        └── page.tsx
```

`npm install` 후 `npm run dev`로 실행. 백엔드(localhost:8080) 미실행 시 빈 상태 메시지 표시.
