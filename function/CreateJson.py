import json

def createJSONArt(dados_artigos, nome_do_arquivo):
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(dados_artigos, arquivo_json, indent=4, ensure_ascii=False)

    print(f"Arquivo '{nome_do_arquivo}' foi criado com sucesso.")