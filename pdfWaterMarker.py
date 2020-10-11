import PyPDF2
import sys


file = sys.argv[1]

template = PyPDF2.PdfFileReader(open('file', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('waterMarkedOutput.pdf', 'rb') as file:
        output.write(file)
