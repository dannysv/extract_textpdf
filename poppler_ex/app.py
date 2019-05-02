import popplerqt4
d = popplerqt4.Poppler.Document.load('../poppler_ex/test.pdf')

total_ann = 0
for i in range(d.numPages()):
    page = d.page(i)
    #print(page)
    ann = page.annotations()
    if len(ann)>0:
        #print(ann)
        for a in ann:
            if isinstance(a, popplerqt4.Poppler.Annotation):
                total_ann+=1
                if isinstance(a, popplerqt4.Poppler.HighlightAnnotation):
                    print(str(page.text(a.boundary())))

if total_ann >0 :
    print(str(total_ann) + "annotation(s) found")
else:
    print("no annotation found")
