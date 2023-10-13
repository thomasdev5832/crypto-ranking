import React, { useEffect, useState } from 'react';
import CryptoList from './components/CryptoList';

const Index = () => {
  // cria um estado para armazenar os dados das criptomoedas
  const [data, setData] = useState([] as any[]);

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
          'Content-Type': 'application/json',  // Configura o tipo de conteúdo para JSON
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
      alert('Parabéns! Voto realizado com sucesso!');
    } catch (error: any) {
      console.error('Erro ao enviar voto:', error.message);
    }
  };

  return (
    <div className='main'>
      <h1 className="font-bold">Qual sua criptomoeda favorita?</h1>
      {/* Renderizando o componente CryptoList e passando as propriedades 'data' e 'handleVote' */}
      {data ? <CryptoList data={data} handleVote={handleVote} /> : <p>Carregando dados...</p>}
    </div>
  );
};

export default Index;