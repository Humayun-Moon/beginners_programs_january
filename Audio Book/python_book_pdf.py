import PyPDF2 
import pyttsx3
pdf_reader = PyPDF2.PdfFileReader(open("C:\\python_book.pdf", "rb"))
speaker = pyttsx3.init()

for num_page in range(pdf_reader.numPages):
    text = pdf_reader.getPage(num_page).extract_text()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()    
