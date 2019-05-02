import os
import textract
import codecs

def main(name_file):
    text = textract.process(name_file)
    return text 

#list the all files in 
path = '../poppler_ex/Dataset-BG-Petrobras'
path_to = '../textract/extr'
lista = os.listdir(path)
for item in lista:
    print(item)
    text = main(path+'/'+item)
    #print(str(text))
    aux = codecs.open(path_to+'/'+item+'.txt', 'wb')
    aux.write(text)
    aux.close()

