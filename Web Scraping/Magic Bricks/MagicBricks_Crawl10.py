#This
import requests
from bs4 import BeautifulSoup
import pandas

l=[]
#r=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS")
#baseurl= "http://www.magicbricks.com/property-for-sale/residential-real-estate?nsrSearchBar=N&searchTransMode=driving&price=Y&editSearch=Y&sortBy=Lowest%20Price&bar_propertyType_new=10002_10003_10021_10022&tab1=property&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune/Page-"
#baseurl="https://www.magicbricks.com/property-for-sale/residential-real-estate?nsrSearchBar=N&searchTransMode=driving&price=Y&editSearch=Y&sortBy=Lowest%20Price&bar_propertyType_new=10002_10003_10021_10022&tab1=property&bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune/Page-"
#baseurl="https://www.magicbricks.com/property-for-sale/residential-real-estate-Pune/Page-" #All property 1,2 and 3 bhk
baseurl="https://www.magicbricks.com/property-for-sale/2-BHK-Multistorey-Apartment-real-estate-Pune/Page-" #Only 2BHK
#req = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune")
#req= requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?nsrSearchBar=N&searchTransMode=driving&price=Y&editSearch=Y&sortBy=Lowest%20Price&bar_propertyType_new=10002_10003_10021_10022&tab1=property&bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune/Page-1")
req= requests.get("https://www.magicbricks.com/property-for-sale/2-BHK-Multistorey-Apartment-real-estate-Pune/Page-1")
con = req.content
bsoup=BeautifulSoup(con,"html.parser")
page_no=bsoup.find_all("a",{"class":"act"})[-1].text #By insteping element on magic bricks pune  for page link we found a, class=act is holding the number
print(page_no)
Page_Processed=0
Item_Processed=1
#for page in range(1,100,1): #Just first 9 pages
for page in range(1,int(page_no)+1,1): # (page_no)+1 to include last page as range excludes the upper limit
    Page_Processed=Page_Processed + 1
    r=requests.get(baseurl+str(page))
    c=r.content
    soup = BeautifulSoup(c, "html.parser")
    search_all = soup.find_all("div",{"class":"flex relative clearfix m-srp-card__container"}) #Supplying each property listing's identifier block value through html source code i.e div, class=flex...
    for item in search_all:
        d={}
        try:
            d["Price"]=item.find("div",{"class":"m-srp-card__price"}).text.replace('₹',"") #pulling item's price
        #print(item.find_all("div" ,{"class","m-srp-card__summary__title"})[0].text) #Pulling item's area Heading. [0] is used as there are multiple  m-srp-card__summary__title and pulling the value of firt instance
        except:
            d["Price"]=None

        try:
            d["Price/Sqft"]=item.find("span", {"class":"semi-bold"}).text.replace('₹',"")
        except:
            d["Price/Sqft"]=None

        try:
            d["Area Type"]=item.find_all("div",{"class":"m-srp-card__summary__title"})[0].text.replace("\n","")
        except:
            d["Area Type"]=None

        try:
            d["Area"]=item.find_all("div" ,{"class","m-srp-card__summary__info"})[0].text #pulling item's  area value
        except:
            d["Area"]=None

        try:
            d["Possession On"]=item.find_all("div",{"class","m-srp-card__summary__info"})[1].text.replace("\n","")
        except:
            d["Possession On"]=None

        """
        try: #Using for loop instead as resale is coming in some listings only as floor field is not mentioned in all listings
            d["Floor Number"]=item.find_all("div",{"class","m-srp-card__summary__info"})[2].text
        except:
            d["Floor Number"]=None
        """
        try:
            d["Posted By"]=item.find("div",{"class", "m-srp-card__advertiser__type"}).text
        except:
            try:
                d["Posted By"]=item.find("div", {"class":"m-srp-card__advertiser__label"}).text
            except:
                d["Posted By"]=None
        try:
            d["Posted By Name"]=item.find("b",{"class":"agentNameh"}).text
        except:
            try:
                d["Posted By Name"]=item.find("div",{"class":"m-srp-card__advertiser__name"}).text.replace("\n","")
            except:
                d["Posted By Name"]=None
        try:
            d["Posted Date"] = item.find("span",{"itemprop":"dateCreated"}).text
        except:
            d["Posted Date"] = None

        """try: #this information is included in Below "Flat Details"
            d["Flat BHK"]=item.find("span",{"class":"m-srp-card__title__bhk"}).text.replace("\n","")
            #print(item.find("span",{"class":"m-srp-card__title__bhk"}).text)
        except:
            d["Flat BHK"]=None
        """

        try:
            d["Flat Details"]=item.find("a",{"class":"m-srp-card__title"}).text.replace("\n"," ").replace("for sale in",",")
        except:
            d["Flat Details"]=None

        try: #here class=td contains field and values both when we get the field name index+1 gives its value
            index=0
            other_charges=item.find_all("div",{"class":"td"}) #Putting in variable so that it's items can be directly by index [index]  in "if" below
            for charge in other_charges:

                if "Approx. Registration Charges" in charge.text:
                    d["Price Reg"] = other_charges[index+1].text.replace("\n","").replace("₹","")

                # Code not working for brokerage
                if "Brokerage" in charge.text:
                    d["Price Broker"] = other_charges[index].text.replace("\n","") #No brokerage contains brokerage word need to check both field later* not sure but working
                    #print(other_charges[index].text.replace("\n",""))

                if "All Inclusive Price" in charge.text:
                    d["Price Total"] = other_charges[index+1].text.replace("\n","").replace("₹","")

                if "Service Tax" in charge.text:
                    d["Price Service"] = other_charges[index+1].text.replace("\n","").replace("₹","")

                index=index+1
        except:
            pass



           #if "Approx. Registration Charges" in otherChg_var.text:
            #   d["Price Reg"] = otherChg_value.text

        #Using for loop and if as to pull un-uniform/unorderly set features from feature list, features  not alwyas at the same item location in html file
        for feature_var,feature_value in zip(item.find_all("div",{"class":"m-srp-card__summary__title"}),item.find_all("div",{"class":"m-srp-card__summary__info"})):


            if "car parking" in feature_var.text:
                d["Car Parking"]=feature_value.text

            if "transaction" in feature_var.text:
                d["Property Type"]=feature_value.text

            if "floor" in feature_var.text:
                d["Floor Number"]=feature_value.text

            if "furnishing" in feature_var.text:
                d["Furnished Status"]=feature_value.text


        """ Putting all these individual "for" loops into single "for" loop above for faster processing. "For" loop was requried as the values
        are not at sepcific place like car parking or floor number details not specified in some listings and is pulling next value and inserting it under car parking or floor Number
        . So to avoid mixing up of data/ inconsistent data in excel file we are searching the field value and if the variable is found then insertuing it in the dictionary.
        The variable name like "car parking" or "transaction" is pulled from html source code by clicking inspect element.

        for floor_des,floor_num in zip(item.find_all("div",{"class":"m-srp-card__summary__title"}), item.find_all("div",{"class":"m-srp-card__summary__info"})):
            if "floor" in floor_des.text:
                d["Floor Number"]=floor_num.text

        for parking,park_type in zip(item.find_all("div",{"class":"m-srp-card__summary__title"}),item.find_all("div",{"class":"m-srp-card__summary__info"})):
            if "car parking" in parking.text:
                d["Car Parking"]=park_type.text

        for prop_var,prop_info in zip(item.find_all("div", {"class":"m-srp-card__summary__title"}),item.find_all("div",{"class":"m-srp-card__summary__info"})):
            if "transaction" in prop_var.text: #transaction this value is seen from inspect element ans the actual value in html file
                d["Property Type"]=prop_info.text

        for furnish_var, furnish_info in zip(item.find_all("div",{"class":"m-srp-card__summary__title"}),item.find_all("div", {"class":"m-srp-card__summary__info"})):
            if "furnishing" in furnish_var.text:
                d["Furnished Status"]=furnish_info.text
        """


        Item_Processed = Item_Processed + 1
        print("Items Processed :"+str(Item_Processed)+" from Pages : " + str(Page_Processed) + " / " + page_no)
        l.append(d)


df = pandas.DataFrame(l)
#df.to_csv("MagicBricksFirst10.csv")
df.to_csv("MagicBricksAll_Mar162018.csv")
