import React, { useEffect, useState } from 'react'

function Index() {

  // armazena os dados das criptomoedas
  const [data, setData] = useState([] as any[]);
  let ranking = 1; // define o ranking localmente

  // buscar os dados da API 
  useEffect(() => {
    const fetchData = async () => {
      try {
        // requisição à API 
        const response = await fetch('https://api-ranking-ad031a8852b1.herokuapp.com/api/criptos/');
        // converte a resposta em json e atualiza o estado
        const jsonData = await response.json();
        setData(jsonData);
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    };

    fetchData();
  }, []);

  // votar em uma criptomoeda
  const handleVote = async (criptoId: number) => {
    try {
      // Faz a requisição para registrar o voto na API
      const response = await fetch(`https://api-ranking-ad031a8852b1.herokuapp.com/api/criptos/votar/${criptoId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json', // Configura o tipo de conteúdo para JSON
        },
        // Se precisar enviar dados no corpo da solicitação, adicionas aqui
        // body: JSON.stringify({ key: 'value' }),
      });
  
      // verifica se a requisição está ok
      if (!response.ok) {
        throw new Error(`Erro na solicitação: ${response.status} - ${response.statusText}`);
      }
  
      // Atualiza os dados LOCALMENTE depois do voto
      const updatedData = [...data];
      const votedItemIndex = updatedData.findIndex((item) => item.id === criptoId);
      if (votedItemIndex !== -1) {
        updatedData[votedItemIndex].votos += 1;
        setData(updatedData);
      }
  
      // console.log('Voto registrado com sucesso:', await response.json());
      // alert('Parabéns! Voto realizado com sucesso!');
    } catch (error: any) {
      console.error('Erro ao enviar voto:', error.message);
    }
  }; 

  return (
    <div className='main'>
    <h1 className="font-bold">Qual sua criptomoeda favorita?</h1>
    
    {data ? (
      <div className='container'>
        <table className='custom-table'>
          <thead>
            <tr>
              <th className="font-bold">Ranking</th>
              <th className="font-bold">Nome</th>
              <th className="font-bold">Votos</th>
              <th className=""></th>
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
                    <button onClick={() => handleVote(item.id)}>
                      <div className='btn-icon'>
                        <img src="https://noxbitcoin.com.br/wp-content/themes/nox/img/icon-lighting-black.svg" alt="" />
                      </div>
                      Votar
                    </button>
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

export default Index