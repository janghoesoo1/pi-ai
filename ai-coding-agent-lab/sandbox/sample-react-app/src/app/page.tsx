async function getUsers() {
  try {
    const res = await fetch('http://localhost:8080/api/users', {
      cache: 'no-store',
    });
    if (!res.ok) return [];
    return res.json();
  } catch {
    return [];
  }
}

export default async function Home() {
  const users = await getUsers();

  return (
    <main style={{ padding: '2rem', fontFamily: 'monospace' }}>
      <h1>Sample React App</h1>
      <p>AI 코딩 에이전트 실험용 프론트엔드</p>
      <p>Backend: http://localhost:8080/api</p>

      <h2>Users</h2>
      {users.length === 0 ? (
        <p>백엔드 서버가 실행되지 않았거나 사용자가 없습니다.</p>
      ) : (
        <table style={{ borderCollapse: 'collapse', width: '100%' }}>
          <thead>
            <tr>
              <th style={{ border: '1px solid #ccc', padding: '8px' }}>ID</th>
              <th style={{ border: '1px solid #ccc', padding: '8px' }}>Name</th>
              <th style={{ border: '1px solid #ccc', padding: '8px' }}>Email</th>
              <th style={{ border: '1px solid #ccc', padding: '8px' }}>Orders</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user: any) => (
              <tr key={user.id}>
                <td style={{ border: '1px solid #ccc', padding: '8px' }}>{user.id}</td>
                <td style={{ border: '1px solid #ccc', padding: '8px' }}>{user.name}</td>
                <td style={{ border: '1px solid #ccc', padding: '8px' }}>{user.email}</td>
                <td style={{ border: '1px solid #ccc', padding: '8px' }}>
                  {user.orders?.length ?? 0}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </main>
  );
}
