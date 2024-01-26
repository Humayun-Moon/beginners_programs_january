import pyautogui
import qrcode

screen_short = pyautogui.screenshot()
screen_short.save("C://screenshort_program//screenshort_3.png") 


def qr_generator (url):
    code_image = qrcode.make(url)
    code_image.save("C://screenshort_program//qr.png")
input_url = input("Enter the url to generate qrcode: ") 
qr_generator(input_url)   

    