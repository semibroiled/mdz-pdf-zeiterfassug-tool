from PyPDF2 import PdfFileReader
from pathlib import Path

#Create new instance of PDfFileReader class
#First get Padth to PDF File

pdf_path = ( Path.home()/'HESSENBOX-DA'/'Austausch Amitav - Evaluation MDZ (Phillip Bausch)'/'Stundenschreibung'/'Offizielle Liste copy.pdf')

#It was showing erros because Path.home() brings me to my home direction which is already Users/acm/
#Having it again in string meant having Users/acm/Users/acm instead of Users/acm
#Hence, beachten wo deine Home Directory liegt

#Now create instance

pdf = PdfFileReader(str(pdf_path))

#Now that instance is created...you can use methods to get attributes

print(pdf.documentInfo)
print(pdf.documentInfo.author) #access individual attributes as such 

print(pdf.getNumPages())

#Extracting text from a file

page1 = pdf.getPage(0)

print(type(page1))

text_from_pdf= page1.extractText()

print(text_from_pdf)


