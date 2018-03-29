import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS")
#r = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune")
c=r.content

soup = BeautifulSoup(c, "html.parser") #Loading content of c in soup with html parser

search_all = soup.find_all("div",{"class":"propertyRow"}) #Searching div with class propertyRow in the html

print(search_all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
#Finding h4 with class=propPrice within seach_all segment and extrating first element and coverting to text
#Post text conversion it becomes a sting so using string function replace to Repalce /n  with "" and then " " with ""
for item in search_all:

    print(item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ",""))

    print(item.find_all("span",{"class","propAddressCollapse"})[0].text)

    print(item.find_all("span",{"class","propAddressCollapse"})[1].text)

    try: #Some fields have no value for these so try, except is added to catch the error and run the program without stopping on error
        print(item.find("span",("class","infoBed")).find("b").text) #find(b) is used to pull just the number of bed withour beds suffixe
    except:
        print("None")


    try:
        print(item.find("span",{"class","infoSqFt"}).find("b").text)
    except:
        print("None")

    try:
        print(item.find("span",{"class","infoValueFullBath"}).find("b").text)
    except:
        print("None")

    try:
        print(item.find("span",{"class","infoValueHalfBath"}).find("b").text)
    except:
        print("None")

    #Pulling the features of property, these are not uniformal.
    #First element could be lot size or age or it can be someting else so can't use index like item[0] here
    for cg in item.find_all("div",{"class","columnGroup"}): #the features are in Columngroup class
        for feature_group, feature_name in zip(cg.find_all("span",{"class":"featureGroup"}),cg.find_all("span",{"class":"featureName"})):
            #No we iterate through the feature group and feature name in columnggroup class
            if "Age" in feature_group.text: #If we find Age feature group then we print it, else do nothing
                print(feature_name.text)
                



    print("\n")
