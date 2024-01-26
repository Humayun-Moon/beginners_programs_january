import PyPDF2
import pyttsx3

# pdf_reader = PyPDF2.PdfFileReader(open("C:\\python_book.pdf", "rb"))
# speaker = pyttsx3.init()

# for num_page in range(pdf_reader.numPages):
#     text = pdf_reader.getPage(num_page).extract_text()
#     speaker.say(text)
#     speaker.runAndWait()

# speaker.stop()

# above the older version of PyPDF2
# below the letest version bring up it from ChatGpt 


import PyPDF2
import pyttsx3 
start_page = 100

pdf_reader = PyPDF2.PdfReader(open("C:\\python_book.pdf", "rb"))
speaker = pyttsx3.init()

for num_page in range(start_page ,len(pdf_reader.pages)):
    text = pdf_reader.pages[num_page].extract_text()
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()
