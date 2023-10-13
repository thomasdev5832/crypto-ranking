import React from 'react';

// cria uma interface das propriedades
interface CryptoListProps {
  data: any[]; // dados das criptomoedas
  handleVote: (criptoId: number) => void; // função chamada quando o voto é registrado
}

// receve as propriedades do tipo da interdface <CryptoListProps>
const CryptoList = ({ data, handleVote }: CryptoListProps) => {
  let ranking = 1; // define o ranking localmente

  return (
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
        {/* Map dos dados e renderiza as linhas da tabela */}
          {data
            .sort((a, b) => b.votos - a.votos) // Ordenação os dados com base na quantidade de votos
            .map((item, index) => (
              <tr key={index}>
                <td className="ranking-container font-medium">{ranking++}</td>
                <td className="nome-container font-medium">{item.nome}</td>
                <td className="voto-container font-bold">{item.votos}</td>
                <td className="">
                  <button onClick={() => handleVote(item.id)}> {/* função handleVote é chamada passando o ID da criptomoeda como argumento */}
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
  );
};

export default CryptoList;