#install requests and beautiful soup libraries for web scraping
#pip install requests
#pip install bs4
import requests #Reuest is used to grab the html content of a web url
from bs4 import BeautifulSoup # To extract elements from the html file BeautifulSoup is used

r=requests.get("http://pythonhow.com/example.html") #Provide the html url of a wbesite to requests variable
c=r.content #grabs the html content of request web url into c variable
#print(c) #print html file in ilegible format

soup = BeautifulSoup(c,"html.parser") #supply html content and specify to use html parser as the parser for beautifulsoup
#If we don't specify parser then we will get a warning but still it will use html parser

#To make html code legble we can use prettify function of BS, though in practical its rarely user_guide
#print(soup.prettify())

all = soup.find_all("div",{"class":"cities"})
#Searches for div in the html BS and we are passing a dictionary seraching where div contains class = cities in the html

#to extract the first item of search we can do it in two ways

#all = soup.find("div",{"class":"cities"})
#OR
#all = soup.find_all("div",{"class":"cities"})[0]

#OR
#print(all[0])

#print(all)

#To Pull h2 or headings we can use another find_all with all variable which returned delivery

#print(all[0].find_all("h2")) #this wll print [<h2>London</h2>], to pring london only

print(all[0].find_all("h2")[0].text)

#To find all h2's in the all beautisoup Varable

for item in all: #Each div is separated by a comma, so each tem is the text before comma, we can use p to get pragraph instead of h2
    print(item.find_all("h2")[0].text)
