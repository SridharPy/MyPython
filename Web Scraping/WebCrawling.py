#Here we are scraping through all pages in the web
#The next pages have some changes in url what we see is in the url s= changes to 0, 10, 20 for next three pages
#So we use the base url as s= and then supply s= in for loop to iterate through each page
#Then we add the program from RealEstateScrapping.py un der this for loop to fetch data from each page
#We can grab the last page number from base page inspect element and send in for loop as upper limit by supplying it in a variable

import requests
from bs4 import BeautifulSoup
import pandas

l=[] #Creating an empty list to save dictinary values from web page scrapping

req=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/") #loading the first page
con=req.content

bsoup=BeautifulSoup(con,"html.parser")
page_no=bsoup.find_all("a",{"class":"Page"})[-1].text #By inspect element on page number links in web browser we found a and class=page for those, so grabbed last element of that class which is the last page no of the website
print(page_no)

baseurl="http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
#for page in range(0,30,10):
for page in range(0,int(page_no)*10,10): #Supplied last page no grabbed from above and multiply by 10 as las t page has s=20 in url not s=3 and skipping by 10 
    r=requests.get(baseurl+str(page)+".html")
    c=r.content

    soup=BeautifulSoup(c,"html.parser")

    search_all=soup.find_all("div",{"class":"propertyRow"}) #Searching div with class propertyRow in the html

    #print(search_all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
    #Finding h4 with class=propPrice within seach_all segment and extrating first element and coverting to text
    #Post text conversion it becomes a string so using string function replace to Repalce /n  with "" and then " " with ""

    for item in search_all:
        d={} #Creating an empty dictinary to store web scrapped data , key-value pair into it in each iteration
        d["Price"]=item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ","")

        d["Address"]=item.find_all("span",{"class","propAddressCollapse"})[0].text

        d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text

        try: #Some fields have no value for these so try, except is added to catch the error and run the program without stopping on error
            d["Beds"]=item.find("span",("class","infoBed")).find("b").text #find(b) is used to pull just the number of bed withour beds suffixe
        except:
            d["Beds"]=None


        try:
            d["Area"]=item.find("span",{"class","infoSqFt"}).find("b").text
        except:
            d["Area"]=None

        try:
            d["Full Bath"]=item.find("span",{"class","infoValueFullBath"}).find("b").text
        except:
            d["Full Bath"]=None

        try:
            #print(item.find("span",{"class","infoValueHalfBath"}).find("b").text)
            d["Half Bath"]=item.find("span",{"class","infoValueHalfBath"}).find("b").text
        except:
            d["Half Bath"]=None

        #Pulling the features of property, these are not uniformal.
        #First element could be lot size or age or it can be someting else so can't use index like item[0] here
        for cg in item.find_all("div",{"class","columnGroup"}): #the features are in Columngroup class
            for feature_group, feature_name in zip(cg.find_all("span",{"class":"featureGroup"}),cg.find_all("span",{"class":"featureName"})):
                #No we iterate through the feature group and feature name in columnggroup class
                if "Age" in feature_group.text: #If we find Age feature group then we print it, else do nothing
                    #print(feature_name.text)
                    d["Property Age"]=feature_name.text
        l.append(d)


    df = pandas.DataFrame(l)

    df.to_csv("WebCrawlData.csv")
