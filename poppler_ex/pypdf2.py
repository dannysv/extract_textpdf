from PyPDF2 import PdfFileReader
import PyPDF2
import os
import codecs
def main(path):
    extracted_text = ""
    with open(path, 'r') as f:
        pdf = PdfFileReader(f)
        number_of_pages = pdf.getNumPages()
        for page_number in range(number_of_pages):
            page = pdf.getPage(page_number)
            text_page = page.extractText()
            extracted_text += text_page+'\n'
    return extracted_text
  

  
import time    
#list the all files in 
path = '../poppler_ex/Dataset-BG-Petrobras'
path_to = '../poppler_ex/extr/pypdf2'
lista = os.listdir(path)
for item in lista:
    t0 = time.time()
    print(item)
    text = main(path+'/'+item)
    aux = codecs.open(path_to+'/'+item+'.txt', 'w')
    aux.write(text.encode('utf-8'))
    aux.close()
    t1 = time.time()
    print(t1-t0)
