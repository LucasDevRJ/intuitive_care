import os
import zipfile

diretorio = "../downloads"
saida_zip = "anexos_compactados.zip"

anexos = [f for f in os.listdir(diretorio) if "Anexo" in f and f.endswith(".pdf")]

with zipfile.ZipFile(saida_zip, "w") as zipf:
    for arquivo in anexos:
        caminho_completo = os.path.join(diretorio, arquivo)
        zipf.write(caminho_completo, arquivo)  # Adiciona ao ZIP mantendo o nome do arquivo

print(f"Arquivo {saida_zip} criado com sucesso com os anexos!")
