import React, { useEffect, useState } from 'react'

function index() {

  const [data, setData] = useState([] as any[]);
  let ranking = 1;

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:8080/');
        const jsonData = await response.json();
        setData(jsonData);
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className='main'>
    <h2 className="font-bold">Qual sua criptomoeda favorita?</h2>
    
    {data ? (
      <div>
        <table>
          <thead>
            <tr>
              <th className="font-bold">Ranking</th>
              <th className="font-bold">Nome</th>
              <th className="font-bold">Votos</th>
              <th className="font-bold"></th>
            </tr>
          </thead>
          <tbody>
            {data
              .sort((a, b) => b.votos - a.votos)
              .map((item, index) => (
                <tr key={index}>
                  <td className="ranking-container font-medium">{ranking++}</td>
                  <td className="nome-container font-medium">{item.nome}</td>
                  <td className="voto-container font-bold">{item.votos}</td>
                  <td className="">
                    <button><div className='btn-icon'><img src="https://noxbitcoin.com.br/wp-content/themes/nox/img/icon-lighting-black.svg" alt="" /></div>Votar</button>
                  </td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>
    ) : (
      <p>Carregando dados...</p>
    )}
  </div>
  )
}

export default index