import PyPDF2

file = open("C:\\Users\\JC\\PycharmProjects\\Demo_Project\\Directory_pdf\\doc.pdf", 'rb')

pdfreader = PyPDF2.PdfFileReader(file)

print(pdfreader.getNumPages())

pageobj = pdfreader.getPage(0)
print(pageobj.extractText())

file.close()


