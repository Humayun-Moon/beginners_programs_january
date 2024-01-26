import requests
import bs4
# printing the taxt...
link = input("Enter the url: ")
page = requests.get(link)
print(page.text) 

# print the text in a readable form..

shop = bs4.BeautifulSoup(page.text, 'html.parser')
text_format = shop.prettify()
print(text_format) 

# print the list of image tag...

image_list = shop.find_all('img')
print(image_list)

# print the number of image tag....

count_the_image = len(image_list)
print(count_the_image)


