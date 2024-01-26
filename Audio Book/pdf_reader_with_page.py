import PyPDF2
import pyttsx3

start_page = 20
end_page = 400

pdf_reader = PyPDF2.PdfReader(open("C:\\python_book.pdf", "rb"))
speaker = pyttsx3.init()

for num_page in range(start_page -1, min(end_page, len(pdf_reader.pages))):
    text = pdf_reader.pages[num_page].extract_text()
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()
