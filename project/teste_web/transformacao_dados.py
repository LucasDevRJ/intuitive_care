import csv
import zipfile
from turtle import pd
import pandas

import pdfplumber

# Caminho do PDF do Anexo I
pdf_path = "../downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

# Nome do arquivo CSV de saída
csv_path = "tabela_anexo_I.csv"

zip_path = "Teste_Lucas_Pereira_de_Lima.zip"

# Abre o PDF e extrai a tabela
with pdfplumber.open(pdf_path) as pdf:
    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        for page in pdf.pages:
            tabelas = page.extract_tables()

            for tabela in tabelas:
                for linha in tabela:
                    writer.writerow(linha)  # Escreve cada linha no CSV

print(f"Tabela salva em {csv_path}")

# Criando o arquivo ZIP e adicionando o CSV
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_path, arcname="tabela_anexo_I.csv")


# Carregar a tabela extraída
csv_path = "tabela_anexo_I.csv"
df = pandas.read_csv("tabela_anexo_I.csv")

# Mapeamento das abreviações para descrições completas
substituicoes = {
    "OD": "Procedimento Odontológico",
    "AMB": "Procedimento Ambulatorial"
}

# Substituir valores nas colunas OD e AMB
df.replace(substituicoes, inplace=True)

# Salvar a tabela atualizada
df.to_csv(csv_path, index=False)

print("Abreviações substituídas com sucesso!")