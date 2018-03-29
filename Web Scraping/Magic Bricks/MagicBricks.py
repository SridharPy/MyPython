import requests
from bs4 import BeautifulSoup

#r=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS")


r= requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune")
c=r.content

soup = BeautifulSoup(c, "html.parser")

search_all = soup.find_all("div",{"flex relative clearfix m-srp-card__container"}) #Supplying each property listing's identifier block value through html source code

for item in search_all:
    print(item.find("div",{"class":"m-srp-card__price"}).text) #pulling item's price
    print(item.find_all("div" ,{"class","m-srp-card__summary__title"})[0].text) #Pulling item's area Heading. [0] is used as there are multiple  m-srp-card__summary__title and pulling the value of firt instance
    print(item.find_all("div" ,{"class","m-srp-card__summary__info"})[0].text) #pulling item's  area value
    print(item.find("div",{"class", "m-srp-card__advertiser__type"}).text)
    print(item.find("b",{"class":"agentNameh"}).text)
    #print(item.find("span",{"class":"m-srp-card__title__bhk"}).text)
    print("\n")
