

import requests
import bs4

link = input("Enter the URL: ")
script = requests.get(link)
print(script.text) 

response = script

print("")
print(f"Response code : {response}") 

print("")



shop = bs4.BeautifulSoup(script.text, 'html.parser') 
format_text = shop.prettify()
print(f"HTML format text: {format_text}")

list_image = shop.find_all('img')
print(f"List of image: {list_image}")

count_the_image = len(list_image)
print(f"Total count of image list: {count_the_image}")
