
# Web Scraping para Download e Compactação de Arquivos PDF - ANS

## Autor: 
Guilherme Alves Silva

## Data de Criação: 
24/03/2025

## Descrição:
Este script realiza o processo de **Web Scraping** para acessar o site da **Agência Nacional de Saúde Suplementar (ANS)** e realizar o download dos arquivos PDF relacionados aos Anexos I e II. Após o download, os arquivos são compactados em um único arquivo **ZIP**.

### Funcionalidades:
- Acessa o site da ANS.
- Identifica e extrai links de arquivos PDF para os Anexos I e II.
- Faz o download dos arquivos PDF para uma pasta local.
- Compacta os arquivos baixados em um arquivo ZIP.

## Como Usar:

1. Certifique-se de ter o Python 3.x instalado no seu computador.
2. Instale as dependências necessárias executando o comando:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Execute o script Python para realizar o download e a compactação dos PDFs:
   ```bash
   python nome_do_arquivo.py
   ```

## Observações:
- O script cria uma pasta **"downloads"** na qual os arquivos PDF serão armazenados.
- Após o download, os arquivos serão compactados em um arquivo ZIP chamado **"anexos.zip"**.
  
## Licença:
Este script é de uso pessoal e educacional, podendo ser modificado conforme necessidade.
