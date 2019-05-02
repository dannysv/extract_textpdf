import popplerqt4
import sys
import PyQt4
#print('a')


def main():
    doc = popplerqt4.Poppler.Document.load(sys.argv[1])
    total_annotations = 0
    for i in range(doc.numPages()):
        #print("========= PAGE {} =========".format(i+1))
        page = doc.page(i)
        annotations = page.annotations()
        (pwidth, pheight) = (page.pageSize().width(), page.pageSize().height())
        print(pwidth)
        print(pheight)
        if len(annotations) > 0:
            for annotation in annotations:
                if  isinstance(annotation, popplerqt4.Poppler.Annotation):
                    total_annotations += 1
                    if(isinstance(annotation, popplerqt4.Poppler.HighlightAnnotation)):
                        quads = annotation.highlightQuads()
                        txt = ""
                        for quad in quads:
                            
                            rect = (quad.points[0].x() * pwidth,
                                    quad.points[0].y() * pheight,
                                    quad.points[2].x() * pwidth,
                                    quad.points[2].y() * pheight)
                            '''
                            rect = (1 * pwidth,
                                    1 * pheight,
                                    1 * pwidth,
                                    1 * pheight)
                            '''
                            bdy = PyQt4.QtCore.QRectF()
                            #print(bdy)
                            #bdy.setCoords(*rect)
                            #txt = txt + unicode(page.text(bdy)) + ' '
                            txt = txt + page.text(bdy) + ' '

                        #print("========= ANNOTATION =========")
                        print(txt)

    if total_annotations > 0:
        print(str(total_annotations) + " annotation(s) found")
    else:
        print("no annotations found")

if __name__ == "__main__":
    main()

