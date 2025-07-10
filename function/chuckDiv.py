from langchain.text_splitter import RecursiveCharacterTextSplitter
import re
def chunkLoad(textoPDF):
    padrao_artigo = r'(Art\.\s*[\w-]+[\.°]?)'

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )

    partes = re.split(padrao_artigo, textoPDF)
    if len(partes) < 3:
        return {}

    chaves_artigos = partes[1::2]
    conteudos_artigos = partes[2::2]

    documento_estruturado = {}
    for chave, conteudo in zip(chaves_artigos, conteudos_artigos):
        if conteudo.strip():

            artigo_estruturado = {}
            article_text = conteudo.strip()

            padrao_subsecoes = r'(§\s*\d+[º°]?|[IVXLCDM]+\s*-|\b[a-z]\))'

            partes_internas = re.split(padrao_subsecoes, article_text)

            if partes_internas[0] and partes_internas[0].strip():
                caput_text = partes_internas[0].strip()
                artigo_estruturado['caput'] = text_splitter.split_text(caput_text)

            resto_iter = iter(partes_internas[1:])
            for delimitador in resto_iter:
                conteudo_subsecao = next(resto_iter, "").strip()
                if conteudo_subsecao:
                    chave_limpa = delimitador.replace('-', '').replace(')', '').strip()
                    artigo_estruturado[chave_limpa] = text_splitter.split_text(conteudo_subsecao)

            documento_estruturado[chave.strip()] = artigo_estruturado

    return documento_estruturado