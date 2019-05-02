import popplerqt4
import sys
import PyQt4

import os 
import codecs
#print('a')


def main(name_file):
    doc = popplerqt4.Poppler.Document.load(name_file)
    total_annotations = 0
    txt = ''
    for i in range(doc.numPages()):
        #print("========= PAGE {} =========".format(i+1))
        page = doc.page(i)
        annotations = page.annotations()
        (pwidth, pheight) = (page.pageSize().width(), page.pageSize().height())
        #txt = ""
        rect = (1 * pwidth,
                1 * pheight,
                1 * pwidth,
                1 * pheight)
        bdy = PyQt4.QtCore.QRectF()
        bdy.setCoords(*rect)
                            #txt = txt + unicode(page.text(bdy)) + ' '
        txt = txt + page.text(bdy) + ' '

    return txt 
    
#list the all files in 
path = '../poppler_ex/Dataset-BG-Petrobras'
path_to = '../poppler_ex/extr'
lista = os.listdir(path)
for item in lista:
    print(item)
    text = main(path+'/'+item)
    aux = codecs.open(path_to+'/'+item+'.txt', 'w')
    aux.write(text)
    aux.close()

