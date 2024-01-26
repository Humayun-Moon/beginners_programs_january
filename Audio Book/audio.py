import PyPDF2
import  pyttsx3



# Initialize the text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 100)

# # Set properties (optional)
# # engine.setProperty('rate', 150)  # Speed of speech
# # engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# # Provide the text you want to convert to speech
# text_to_speak = "Hello, this is a test. Hey pagli where are you now i don't know but I also know it you miss my paglami and again and again you are haunting on my heart like you are my all of these things right now"

# # Convert the text to speech
# engine.say(text_to_speak)

# # Wait for the speech to finish
# engine.runAndWait() 

pdf_reader = PyPDF2.PdfFileReader(open("C:\\python_book.pdf", "rb"))
speaker = pyttsx3.init()

for num_page in range(pdf_reader.numPages):
    text = pdf_reader.getPage(num_page).extract_text()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()    
