<template>
  <div class="app">
    <input
      v-model="searchQuery"
      placeholder="Buscar operadora"
      @input="searchOperadora"
      class="search-input"
    />

    <!-- Exibição dos resultados -->
    <div v-if="results.length">
      <ul class="results-list">
        <li v-for="(operadora, index) in results" :key="index" class="result-item">
          <strong>{{ operadora.Razao_Social }}</strong> - {{ operadora.Cidade }}
          <br />
          CNPJ: {{ operadora.CNPJ }}
          <br />
          Endereço: {{ operadora.Logradouro }}, {{ operadora.Numero }} - {{ operadora.Complemento }}
          <br />
          Representante: {{ operadora.Representante }}
          <br />
          Telefone: {{ operadora.Telefone }}
          <br />
          E-mail:
          <a :href="'mailto:' + operadora.Endereco_eletronico">{{ operadora.Endereco_eletronico }}</a>
        </li>
      </ul>
    </div>

    <!-- Caso nenhum resultado seja encontrado -->
    <div v-else>
      <p>Nenhuma operadora encontrada.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '', // Termo de pesquisa
      results: [], // Resultados da pesquisa
    };
  },
  methods: {
    // Função para realizar a busca
    async searchOperadora() {
      if (this.searchQuery.length > 0) {
        try {
          const response = await fetch(`http://localhost:5000/buscar?q=${this.searchQuery}`);
          const data = await response.json();
          this.results = data; // Atualiza os resultados com os dados da API
        } catch (error) {
          console.error('Erro ao buscar as operadoras:', error);
        }
      } else {
        this.results = []; // Limpa os resultados se a busca estiver vazia
      }
    },
  },
};
</script>

<style scoped>
/* Estilo do container principal */
.app {
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
  font-family: Arial, sans-serif;
  background-color: #f4f4f9; /* Cor de fundo suave */
  border-radius: 8px;
}

/* Estilo para o campo de busca */
.search-input {
  width: 100%;
  padding: 12px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  background-color: #fff;
  color: #333;
}

/* Estilo para a lista de resultados */
.results-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.result-item {
  background-color: #ffffff; /* Fundo branco para o item */
  padding: 15px;
  margin-bottom: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* Sombra leve */
  color: #333; /* Cor do texto mais escuro */
}

.result-item strong {
  font-size: 18px;
  color: #327337; /* Cor azul para o nome da operadora */
}

.result-item a {
  color: #327337;
  text-decoration: none;
}

.result-item a:hover {
  text-decoration: underline;
}

/* Estilo para mensagens quando não há resultados */
p {
  color: #555;
  font-size: 16px;
  text-align: center;
}

/* Estilo para o placeholder do campo de pesquisa */
.search-input::placeholder {
  color: #999;
}
</style>
