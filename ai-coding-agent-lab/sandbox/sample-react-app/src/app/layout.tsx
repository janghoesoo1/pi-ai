export const metadata = {
  title: 'AI Coding Agent Lab - Sample React App',
  description: 'Sample frontend for AI coding agent experiments',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ko">
      <body>{children}</body>
    </html>
  );
}
