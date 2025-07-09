from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunkLoad(textoPDF):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(textoPDF)

    print(f"--- Exibindo todos os {len(chunks)} chunks sequencialmente (LangChain) ---")
    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i + 1}/{len(chunks)} ---")
        print(chunk)

    print("\n\n--- Resumo Final ---")
    print(f"Texto total com {len(textoPDF)} caracteres.")
    print(f"Dividido em {len(chunks)} chunks semânticos.")