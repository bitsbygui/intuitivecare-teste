# Teste de Nivelamento - IntuitiveCare

Este repositório contém as soluções para os testes de nivelamento propostos pela IntuitiveCare.

## Estrutura do Projeto

```
📂 projeto-intuitivecare
├── 📂 TESTE_DE_API               
├── 📂 TESTE_DE_BANCO_DE_DADOS           
├── 📂 TESTE_DE_TRANSFORMAÇÃO_DE_DADOS          
├── 📂 TESTE_DE_WEB_SCRAPING                 
```

## 1. Teste de Web Scraping

Objetivo: Acessar o site da ANS, baixar os anexos I e II, e compactá-los.

- Linguagem utilizada: **Python**
- Bibliotecas utilizadas: `requests`, `BeautifulSoup`, `PyPDF2`, `zipfile`
- Caminho do código: `dados/web_scraping.py`

## 2. Teste de Transformação de Dados

Objetivo: Extrair dados da tabela do PDF do Anexo I, salvar em CSV e compactar.

- Linguagem utilizada: **Python**
- Bibliotecas utilizadas: `pandas`, `pdfplumber`, `zipfile`
- Caminho do código: `dados/processamento_dados.py`

## 3. Teste de Banco de Dados

Objetivo: Criar scripts SQL para estruturar e importar dados sobre operadoras.

- Banco de dados utilizado: **PostgreSQL**
- Caminho dos scripts SQL: `dados/scripts.sql`

## 4. Teste de API

Objetivo: Criar um backend em Python que exponha uma API para buscar operadoras e um frontend em Vue.js para interação.

- **Backend** (Python + Flask):
  - Caminho do código: `server.py`
  - Dependências: `Flask`, `pandas`

- **Frontend** (Vue.js):
  - Caminho do código: `frontend/src/App.vue`
  - Dependências: `Vue.js`

- **Coleção Postman**:
  - Caminho: `postman/collection.json`

## Como Executar o Projeto

### 1. Configurar o ambiente Python

```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 2. Executar o servidor

```sh
python server.py
```

### 3. Executar o frontend

```sh
cd frontend
npm install
npm run dev
```

### 4. Testar a API no Postman

Importe a coleção `postman/collection.json` no Postman e execute os testes.

## Contato

Caso tenha dúvidas, entre em contato pelo e-mail [guilhermesskr@gmail.com](guilhermesskr@gmail.com).
