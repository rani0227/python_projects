import pyttsx3
import PyPDF2
file=open("climate_change.pdf",mode="rb")
pdf_reader=PyPDF2.PdfFileReader(file)
pages=pdf_reader.numPages
melo=pyttsx3.init()
for i in range(2,pages):
    page=pdf_reader.getPage(6)
    text=page.extractText()
    melo.say("text")
    melo.runAndWait()
