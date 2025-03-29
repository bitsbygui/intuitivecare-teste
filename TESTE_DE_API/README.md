
# Projeto Operadora

Este projeto consiste em um sistema simples de busca de operadoras de saúde. Ele é dividido em duas partes principais:

- **Backend**: Servidor em Python (Flask) que fornece a API para buscar operadoras.
- **Frontend**: Interface em Vue.js para realizar buscas e exibir os resultados de maneira amigável.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
├── dados/               # Arquivos de dados para o back-end
├── frontend/            # Código do front-end (Vue.js)
├── postman/             # Coleção do Postman com os testes da API
├── venv/                # Ambiente virtual para o back-end
├── server.py            # Servidor em Python (Flask)
└── README.md            # Este arquivo
```

## Requisitos

Antes de rodar o projeto, você precisará ter os seguintes softwares instalados:

- **Python 3.x** (para o back-end)
- **Node.js** e **npm** (para o front-end)
- **Postman** (opcional, para testar a API)

## Instruções para Configuração

### 1. Configuração do Backend (Flask)

#### Passo 1: Criar o ambiente virtual

Dentro da pasta principal do projeto, execute o seguinte comando para criar um ambiente virtual (se ainda não estiver criado):

```bash
python -m venv venv
```

#### Passo 2: Ativar o ambiente virtual

- No **Windows**:

```bash
.\venv\Scripts\activate
```

- No **Linux/Mac**:

```bash
source venv/bin/activate
```

#### Passo 3: Instalar as dependências do back-end

Com o ambiente virtual ativado, instale as dependências necessárias para o back-end com o comando:

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` não esteja presente, você pode instalar o Flask diretamente:

```bash
pip install Flask
```

#### Passo 4: Rodar o servidor

Execute o servidor com o comando:

```bash
python server.py
```

A API estará disponível em `http://localhost:5000`.

### 2. Configuração do Frontend (Vue.js)

#### Passo 1: Navegar até a pasta `frontend`

```bash
cd frontend
```

#### Passo 2: Instalar as dependências do front-end

Instale as dependências necessárias para o Vue.js com o comando:

```bash
npm install
```

#### Passo 3: Rodar o front-end

Execute o servidor de desenvolvimento do Vue.js com o comando:

```bash
npm run dev
```

A aplicação estará disponível em `http://localhost:5173`.

### 3. Testes com o Postman

1. Importe a coleção presente na pasta `postman` para o **Postman**.
2. Execute as requisições para testar a API.

### 4. Teste a aplicação

- Abra a aplicação no **front-end** (`http://localhost:5173`).
- Realize buscas no campo de pesquisa e veja os resultados sendo exibidos.

## Como Testar a API

Você pode testar a API diretamente no Postman, importando a coleção presente na pasta `postman`.

1. Abra o **Postman**.
2. Clique em "Import" e selecione a coleção salva.
3. Execute os testes para garantir que a API esteja funcionando corretamente.

---

## Problemas Comuns

1. **CORS no Front-End**: Se você enfrentar problemas relacionados a CORS (Cross-Origin Resource Sharing), verifique se o back-end está sendo executado corretamente e se as permissões de CORS estão configuradas no servidor Flask.
   
2. **Erro de Dependências no Backend**: Certifique-se de que todas as dependências foram instaladas corretamente no ambiente virtual. Caso contrário, instale novamente utilizando `pip install -r requirements.txt`.

---

