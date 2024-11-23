import requests
from bs4 import BeautifulSoup

url = "https://github.com/arkadiyt/bounty-targets/commit/4e14c9ef847f6be6f3a925bda7ec14f9cc86b7b9"
resp = requests.get(url)

soup = BeautifulSoup(resp.text , 'html.parser')
city_tags = soup.find_all("span" , class_="pl-pds")
city_tags2 = soup.find_all("span" , class_="pl-v")
city_tags3 = soup.find_all("span" , class_="pl-v")
city_tags4 = soup.find_all("span" , class_ = "pl-en")
for tag1 in city_tags:
    for tag2 in city_tags2:
        for tag3 in city_tags3:
            for tag4 in city_tags4:
        

                print(tag1.text+":" , tag2.text+"::",tag3.text+"," ,tag4.text)
                

