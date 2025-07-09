from pdfminer.high_level import extract_text

def extractPdfFile(pdfFile):
    text = extract_text(pdfFile)
    return text