import React, { useState } from 'react';

function App() {
  const [userId, setUserId] = useState('');
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const fetchRecommendations = async () => {
    if (!userId) {
      setError('Digite um User ID válido');
      return;
    }

    setLoading(true);
    setError('');
    setMovies([]);

    try {
      const res = await fetch(`http://127.0.0.1:8000/recommendations/${userId}`);
      if (!res.ok) throw new Error('Erro ao buscar recomendações');
      const data = await res.json();
      setMovies(data.recommendations);
    } catch (err) {
      setError('Não foi possível carregar as recomendações');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>🎬 Recomendador de Filmes</h1>

      <div style={{ marginBottom: '10px' }}>
        <input
          type="number"
          placeholder="Digite o User ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          style={{ padding: '5px', marginRight: '10px' }}
        />
        <button onClick={fetchRecommendations} style={{ padding: '5px 10px' }}>
          Buscar
        </button>
      </div>

      {loading && <p>Carregando recomendações...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      <ul>
        {movies.map((m) => (
          <li key={m.movie_id}>{m.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
