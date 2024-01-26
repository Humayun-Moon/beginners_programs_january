import requests
import bs4

link = input("Enter the URL: ")
page = requests.get(link)
print("Script text---------------------------")
print(page.text)
print("-------------------------------------------------")
print("")
shop = bs4.BeautifulSoup(page.text, 'html.parser')
text_format = shop.prettify()
print("text format",text_format) 
print("-------------------------------------------------")
print("")

image_list = shop.find_all('img')
print("Image list",image_list)
print("-------------------------------------------------")
print("")
count_the_image = len(image_list)
print("count length", count_the_image)
print("-------------------------------------------------")
print("")
