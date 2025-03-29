import csv
import zipfile
import pandas

import pdfplumber

pdf_path = "../downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

csv_path = "tabela_anexo_I.csv"

zip_path = "Teste_Lucas_Pereira_de_Lima.zip"

with pdfplumber.open(pdf_path) as pdf:
    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        for page in pdf.pages:
            tabelas = page.extract_tables()

            for tabela in tabelas:
                for linha in tabela:
                    writer.writerow(linha)  # Escreve cada linha no CSV

print(f"Tabela salva em {csv_path}")

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_path, arcname="tabela_anexo_I.csv")

csv_path = "tabela_anexo_I.csv"
df = pandas.read_csv("tabela_anexo_I.csv")

substituicoes = {
    "OD": "Procedimento Odontológico",
    "AMB": "Procedimento Ambulatorial"
}

df.replace(substituicoes, inplace=True)

df.to_csv(csv_path, index=False)

print("Abreviações substituídas com sucesso!")