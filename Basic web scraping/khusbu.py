import requests
import bs4

print("Welcome to Web Scraping program")

def web_scraping(url):
    link = url 
    page = requests.get(link)
    print(page.text) 
    print("")


    shop = bs4.BeautifulSoup(page.text, 'html.parser')
    format_text = shop.prettify()
    print(f"Format text of the url: {link} is = {format_text}")
    print("")

    image_list = shop.find_all('img')
    print(f"All image list of {link} : {image_list} ") 
    print("")

    count_the_image = len(image_list)
    print(f"Total count of the image of the url: {link} : is  :{count_the_image} ")
    print("")

    site_connectivity_code = page
    print(f"The response code of the url : {link} is {site_connectivity_code} ")
    print("")


while True:
    user_url = input("Enter the URL to Scrap : ") 

    if user_url.isdigit():
        print("Please, Enter the Exact URL address")
        continue
    else:
        web_scraping(user_url)
        print("")
        print("Thanks , BYE")
        break




