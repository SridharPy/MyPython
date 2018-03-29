#This script pull all 2 and 3 bhk rental apparments list from pune in low to high
import requests
from bs4 import BeautifulSoup
import pandas
l=[]
i=0
base_url= "https://www.magicbricks.com/property-for-rent/residential-real-estate?nsrSearchBar=N&searchTransMode=driving&price=Y&editSearch=Y&sortBy=Lowest%20Price&bar_propertyType_new=10002_10003_10021_10022&tab1=property&bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune/Page-"
#This url is used to pull last page number
r= requests.get("https://www.magicbricks.com/property-for-rent/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment&cityName=Pune")
c= r.content

bsoup= BeautifulSoup(c,"html.parser")
page_num=bsoup.find_all("a",{"class":"act"})[-1].text # Pulling last page number
print(page_num)
#for pg in range(1,10,1): #For testing only 
for pg in range(1,int(page_num)+1,1):
    r=requests.get(base_url+str(pg))
    c=r.content

    soup=BeautifulSoup(c,"html.parser")

    all_listings= soup.find_all("div",{"class":"flex relative clearfix m-srp-card__container"})

    for listing in all_listings:
        i=i+1
        d={}

        d["Price Rent"]=listing.find("span",{"class","m-srp-card__price"}).text.replace("\n","")

        try:
            d["Posted On"]=listing.find("span",{"itemprop":"dateCreated"}).text.replace("\n","")
        except:
            d["Posted On"]=None

        try:
            d["Flat Details"]=listing.find("a",{"class":"m-srp-card__title"}).text.replace("\n"," ")
        except:
            d["Flat Details"]=None

        try:
            d["Posted By"]=listing.find("div",{"class":"m-srp-card__advertiser__type"}).text
        except:
            d["Posted By"]=None

        try:
            d["Posted Person"]=listing.find("b",{"class":"agentNameh"}).text
        except:
            d["Posted Person"]=None


        for feature_var,feature_val in zip (listing.find_all("div", {"class":"m-srp-card__summary__title"}),listing.find_all("div",{"class":"m-srp-card__summary__info"})):
            if "floor" in feature_var.text:
                d["Floor No"]=feature_val.text
            if "furnishing" in feature_var.text:
                d["Furnished"]=feature_val.text
            if "tenants preferred" in feature_var.text:
                d["Tenant Pref"]=feature_val.text.replace("\n","")
            if "balcony" in feature_var.text:
                d["Balcony"]=feature_val.text
            #if "car parking" in feature_var.text: Car Parking not working wierd
            #    d["Parking"]=feature_val.text
            if "availability" in feature_var.text: #"This is pulling car parking wierd need to check the html code"
                d["Car Parking"]=feature_val.text

        try:
            other_chg = listing.find_all("div",{"class":"td"})
            index=0
            for chgs in (other_chg):
                if "Monthly Maintenance" in chgs.text:
                    d["Price Maint"]=other_chg[index+1].text.replace("\n","").replace("₹","")
                if "Security Deposit" in chgs.text:
                    d["Price Dep"]=other_chg[index+1].text.replace("\n","").replace("₹","")
                if "Brokerage" in chgs.text:
                    d["Price Brok"]=other_chg[index+1].text.replace("\n","").replace("₹","")
                if "First Month Charges" in chgs.text:
                    d["Price Month 1"]=other_chg[index+1].text.replace("\n","").replace("₹","")
                index=index+1
        except:
            d["Price Maint"]=None
        percent=pg*100/int(page_num)
        print("Processed items: " +str(i)+ " from pages: "+str(pg)+"/"+page_num + ": "+str(percent)+" %")
        l.append(d)


    df=pandas.DataFrame(l)

    df.to_csv("MagicBricks_Rent.csv")
