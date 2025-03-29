# --------------------------------------------------------------
# Autor: Guilherme Alves Silva
# Data de Criação: 24/03/2025
# Descrição: Script de Web Scraping para download e compactação
#           de arquivos PDF do site da ANS (Agência Nacional de Saúde).
#           O script faz o acesso ao site, encontra os links para
#           os PDFs dos Anexos I e II, faz o download e compacta os
#           arquivos em um único arquivo ZIP.
# --------------------------------------------------------------


import os
import requests
import shutil
from bs4 import BeautifulSoup

# URL do site da ANS onde estão os arquivos
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Função para obter o conteúdo HTML da página
def obter_conteudo_pagina(url):
    response = requests.get(url)
    return response.text if response.status_code == 200 else None

# Função para extrair links de arquivos PDF da página
def extrair_links_pdf(conteudo_html):
    soup = BeautifulSoup(conteudo_html, "html.parser")
    links = soup.find_all("a", href=True)
    return[link["href"] for link in links if link["href"].endswith(".pdf")]
    
 

# Função para fazer o download de um PDF
def baixar_pdf(pdf_url, download_folder):
    pdf_name = pdf_url.split("/")[-1]
    pdf_path = os.path.join(download_folder, pdf_name)
    
    pdf_response = requests.get(pdf_url, stream=True)
    if pdf_response.status_code == 200:
        with open(pdf_path, "wb") as pdf_file:
            for chunk in pdf_response.iter_content(chunk_size=1024):
                pdf_file.write(chunk)
        print(f"Download concluído: {pdf_name}")
        return pdf_path
    else:
        print(f"Erro ao baixar {pdf_url}. Código: {pdf_response.status_code}")
        return None

# Função para compactar os arquivos baixados
def compactar_arquivos(download_folder):
    shutil.make_archive("anexos", 'zip', download_folder)
    print("Compactação concluída: anexos.zip")

# Função principal para orquestrar todo o processo
def main():
    # Criação do diretório para salvar os arquivos baixados
    download_folder = "downloads"
    os.makedirs(download_folder, exist_ok=True)
    
    # Obter conteúdo da página
    conteudo_html = obter_conteudo_pagina(URL)
    if conteudo_html:
        # Extrair links para PDFs
        pdf_links = extrair_links_pdf(conteudo_html)

        # Baixar os arquivos PDF necessários
        anexos_necessarios = ["Anexo_I", "Anexo_II"]
        anexos_baixados = {}

        for pdf_url in pdf_links:
            for anexo in anexos_necessarios:
                if anexo in pdf_url and anexo not in anexos_baixados:
                    pdf_path = baixar_pdf(pdf_url, download_folder)
                    if pdf_path:
                        anexos_baixados[anexo] = pdf_path

        # Compactar os arquivos baixados
        compactar_arquivos(download_folder)
    else:
        print("Erro ao acessar a página.")

# Executar a função principal
if __name__ == "__main__":
    main()
