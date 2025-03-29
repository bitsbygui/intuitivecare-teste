# --------------------------------------------------------------
# Autor: Guilherme Alves Silva
# Data de Criação: 24/03/2025
# Descrição: Script para extração de dados de uma tabela em PDF,
#           substituição de abreviações das colunas OD e AMB, 
#           salvamento dos dados em formato CSV e compactação 
#           em arquivo ZIP. O objetivo é processar os dados da
#           tabela do arquivo PDF, substituindo abreviações por 
#           descrições completas, e gerar o arquivo final compactado.
# --------------------------------------------------------------



import pdfplumber  # Para extrair os dados do PDF
import csv         # Para criar o arquivo CSV
import zipfile     # Para compactar o arquivo CSV em ZIP

# Caminho para o arquivo PDF
pdf_path = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

# Função para substituir as abreviações
def substituir_abreviacoes(linha):
    for i in range(len(linha)):
        if linha[i] == "OD":
            linha[i] = "Seg. Odontológica"
        elif linha[i] == "AMB":
            linha[i] = "Seg. Ambulatorial"
    return linha

# Função para extrair os dados da tabela do PDF
def extrair_dados_pdf(pdf_path):
    dados_extraidos = []  # Lista onde vamos armazenar as linhas da tabela extraída

    # Abrindo o PDF com o pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        # Iterando pelas páginas 3 a 181 (índices 2 a 180)
        for pagina in range(2, len(pdf.pages)):
            pagina_atual = pdf.pages[pagina]  # Pega a página atual
            tabela = pagina_atual.extract_table()  # Extrai a tabela da página

            if tabela:  # Verifica se a tabela foi extraída com sucesso
                # Se for a primeira página com dados, armazena o cabeçalho
                if pagina == 2:
                    cabecalho = tabela[0]  # O cabeçalho é a primeira linha da tabela
                for linha in tabela[1:]:  # Ignora o cabeçalho e pega as linhas de dados
                    linha_corrigida = substituir_abreviacoes(linha)  # Substitui as abreviações
                    dados_extraidos.append(linha_corrigida)  # Adiciona cada linha à lista

    return cabecalho, dados_extraidos  # Retorna o cabeçalho e os dados extraídos

# Função para salvar os dados extraídos no formato CSV
def salvar_csv(cabecalho, dados, nome_arquivo):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv, delimiter=';')  # Usando ponto e vírgula como delimitador
        writer.writerow(cabecalho)  # Escreve o cabeçalho no CSV
        writer.writerows(dados)  # Escreve os dados no CSV

# Função para compactar o CSV em um arquivo ZIP
def compactar_zip(nome_arquivo_csv, nome_arquivo_zip):
    with zipfile.ZipFile(nome_arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona o arquivo CSV ao arquivo ZIP
        zipf.write(nome_arquivo_csv, arcname=nome_arquivo_csv.split('/')[-1])
    print(f"Arquivo ZIP '{nome_arquivo_zip}' criado com sucesso.")

# Função principal
def main():
    cabecalho, dados_extraidos = extrair_dados_pdf(pdf_path)  # Extrai os dados do PDF
    nome_arquivo_csv = 'dados_extraidos.csv'  # Nome do arquivo CSV
    salvar_csv(cabecalho, dados_extraidos, nome_arquivo_csv)  # Salva os dados no CSV
    nome_arquivo_zip = 'Teste_Guilherme_Alves_Silva.zip'  # Nome do arquivo ZIP
    compactar_zip(nome_arquivo_csv, nome_arquivo_zip)  # Compacta o CSV em um arquivo ZIP
    print(f"Processo concluído com sucesso!")

# Chama a função principal para rodar o processo
if __name__ == "__main__":
    main()
