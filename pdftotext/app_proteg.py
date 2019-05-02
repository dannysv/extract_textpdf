import os
import pdftotext
import codecs

def main(name_file):
    #text = textract.process(name_file)
    with codecs.open(name_file, 'rb') as f:
        #textpdf = pdftotext.PDF(f,"secret")
        textpdf = pdftotext.PDF(f)
    return "\n\n".join(textpdf)

#list the all files in 
path = '../protegido_v'
path_to = '../pdftotext/protected'
lista = os.listdir(path)
for item in lista:
    print(item)
    text = main(path+'/'+item)
    #print(str(text))
    aux = codecs.open(path_to+'/'+item+'.txt', 'w')
    aux.write(text)
    aux.close()
