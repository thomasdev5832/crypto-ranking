import React, { useEffect, useState } from 'react'

function index() {
  const [message, setMessage] = useState("Loading");
  const [cryptos, setCryptos] = useState([]);

  // Faz uma requisição HTTP GET para a URL 
  useEffect(() => {
    fetch("http://localhost:8080/api/home")
    .then((response) => response.json())
    .then((data) => {
      // atualiza o estado do component
        setMessage(data.message);
        setCryptos(data.cryptos);
      });
  }, []);

  return (
    <div>
      <h2>{message}</h2>
      {
      // --- Renderização de listas ---
      // a função map percorre cada elemento do array de cryptos
      // para cada elemento, uma nova div é renderizada
        cryptos.map((crypto, index) => (
          <div className='crypto' key={index}>
            {crypto}
          </div>
        ))
      }
    </div>
  )
}

export default index