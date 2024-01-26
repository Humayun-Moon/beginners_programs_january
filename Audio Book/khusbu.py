import pyttsx3 
import PyPDF2

pdf_reader = PyPDF2.PdfReader(open("C:\\python_book.pdf", "rb"))
start_page = 50
end_page = 500
    
speaker= pyttsx3.init() 

for num_page in range(start_page -1, min(end_page, len(pdf_reader.pages))):
    text = pdf_reader.pages[num_page].extract_text()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()    

# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
# engine.setProperty('volume', 0.2)
# text = "Hello world Here I'm humayun kabir try to learn Python computer programming language but I deeply know that It's a very tough jurney to reach but I have that will power if may Allah want I may be reached my goal Inshallah"
# engine.say(text)
# engine.runAndWait()

# # print(dir(engine)) 