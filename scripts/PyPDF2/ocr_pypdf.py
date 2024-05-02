# pip install PyPDF2

import PyPDF2

def pdf_reader(filepath):
  pdfFile = open(filepath, 'rb')
  pdfReader = PyPDF2.PdfReader(pdfFile)

  text = ""
  for page in range(len(pdfReader.pages)):
      pageObj = pdfReader.pages[page]
      text += pageObj.extract_text()
 
  return text
