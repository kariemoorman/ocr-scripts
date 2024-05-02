# pip install pdfplumber

import pdfplumber

def ocr_pdfplumber(filepath): 
    output = {}
    with pdfplumber.open(filepath) as pdf:
        pages = pdf.pages
        for page in pages:
            text = page.extract_text()
            output[page] = text
    return output
          
