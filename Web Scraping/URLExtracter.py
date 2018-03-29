import requests
from bs4 import BeautifulSoup

base_url="https://www.magicbricks.com/property-for-rent/residential-real-estate?nsrSearchBar=N&searchTransMode=driving&price=Y&editSearch=Y&sortBy=Lowest%20Price&bar_propertyType_new=10002_10003_10021_10022&tab1=property&bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune/Page-1"

r = requests.get(base_url)
t=r.text

soup = BeautifulSoup(t,"html.parser")

links = soup.find_all('a')
link_list=[]
for l in links:
    link_list.append(l.get('href'))

print(link_list)
