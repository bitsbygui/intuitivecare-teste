
# Extração e Substituição de Dados de Tabelas de PDF - ANS

## Autor: 
Guilherme Alves Silva

## Data de Criação: 
24/03/2025

## Descrição:
Este script realiza a **extração de dados** de um arquivo **PDF** contendo tabelas e **substitui as abreviações** presentes nas colunas por suas descrições completas, conforme a legenda no rodapé do arquivo. Os dados extraídos são então salvos em um arquivo **CSV**, que é compactado em um arquivo **ZIP** para facilitar o armazenamento e distribuição.

### Funcionalidades:
- Abre e lê o arquivo PDF especificado.
- Extrai as tabelas das páginas do PDF.
- Substitui as abreviações "OD" por "Seg. Odontológica" e "AMB" por "Seg. Ambulatorial" nas colunas correspondentes.
- Salva os dados extraídos em um arquivo CSV, utilizando ponto e vírgula como delimitador.
- Compacta o arquivo CSV em um arquivo ZIP para distribuição.

## Como Usar:

1. Certifique-se de ter o **Python 3.x** instalado no seu computador.
2. Instale as dependências necessárias executando o comando:
   ```bash
   pip install pdfplumber
   ```
3. Coloque o arquivo PDF que deseja processar no mesmo diretório do script ou ajuste o caminho no código.
4. Execute o script Python para realizar a extração e substituição de dados, e gerar o arquivo CSV compactado:
   ```bash
   python nome_do_arquivo.py
   ```
5. Após a execução, um arquivo ZIP chamado **"Teste_Guilherme_Alves_Silva.zip"** será gerado com o arquivo CSV que contém os dados extraídos.

## Observações:
- O script assume que o arquivo PDF tem um formato específico, com tabelas nas páginas e abreviações a serem substituídas conforme a legenda no rodapé.
- O arquivo CSV gerado utiliza o delimitador **";"** para separar as colunas.
- O arquivo CSV é compactado em um arquivo ZIP para facilitar o armazenamento e envio.

## Licença:
Este script é de uso pessoal e educacional, podendo ser modificado conforme necessidade.
