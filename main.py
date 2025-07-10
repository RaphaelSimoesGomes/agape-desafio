from function.chuckDiv import chunkLoad
from function.extractFile import extractPdfFile
from function.CreateJson import createJSONArt


try:
    pdf_path = "pdf/LEI Nº 14.133, DE 1º DE ABRIL DE 2021 - Lei de Licitações e Contratos Administrativos.pdf"
    texto_completo = extractPdfFile(pdf_path)

except FileNotFoundError:
    print("Erro: Arquivo PDF não encontrado. Por favor, verifique o caminho.")
    texto_completo = ""
except Exception as e:
    print(f"Ocorreu um erro ao processar o arquivo: {e}")
    texto_completo = ""

if texto_completo:

    createJSONArt(chunkLoad(texto_completo),"Artigos extraidos.json")
