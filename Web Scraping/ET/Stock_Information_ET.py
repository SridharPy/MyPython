import requests
from bs4 import BeautifulSoup
import pandas

l=[]

def get_stk_info(stk_name,url):
    req=requests.get(url)
    cont=req.content
    page = BeautifulSoup(cont,"html.parser")
    d={}
    try:
        d["1Name"]=stk_name
        d["2NSE Price"]=page.find("div",{"id":"nseTradeprice"}).text
        d["NSE Open"] = page.find("p",{"id":"nseOpenprice"}).text
        d["NSE Prev Close"] = page.find("p",{"id":"nseCloseprice"}).text
        d["NSE Vol"]= page.find("p",{"id":"nseVolume"}).text
        d["ET Rank"]=page.find("div",{"class":"flt rankText"}).text
        d["NSE Chg Pts"]=page.find("span",{"id":"nseNetchange"}).text
        d["NSE Chg Per"]=page.find("span",{"id":"nsePercentChange"}).text.replace('(',"").replace(")","")
        d["3NSE 52 L/H"] = page.find("span",{"class":"wk_lh tar nse_tab"}).text
        d["St PE"]=page.find("span",{"class":"p_e tar"}).text
        d["St PB"]=page.find("span",{"class":"p_b tar"}).text
        d["St FC Val"]=page.find("span",{"class":"face_value tar"}).text
        d["St EPS TTM"]=page.find("span",{"class":"eps_ttm tar"}).text
        d["St Book Val/Shr"]=page.find("span",{"class":"bv_sh tar"}).text
        d["BSE Chg Per"]=page.find("span",{"id":"bsePercentChange"}).text.replace('(',"").replace(")","")
    except:
        pass
    return d



def pull_all_stks_lnk(url):
    req=requests.get(url)
    cont=req.text

    soup=BeautifulSoup(cont,"html.parser")
    search=soup.find("ul",{"class":"companyList"})# Just pulling first occurance of comanyList html tag
    #As Second one contains top gainers
    urls=search.find_all('a')

    pre_url= "https://economictimes.indiatimes.com"
    for itm in urls:
         url= pre_url + itm.get("href") #href will pull only second par of url so need to add the base page ET url
         stk_name=(itm.text)
         l.append(get_stk_info(stk_name,url))



base_url="https://economictimes.indiatimes.com/markets/stocks/stock-quotes?ticker="


for stk_num in range (2,9,1):
    #Scroll through pages of stocks starting with Number
    if stk_num==1 or stk_num==4:
        continue
    else:
        print("Stock with : " + str(stk_num) )
        pull_all_stks_lnk(base_url+str(stk_num))
    #Send complete URL of stocks list page where stok starting like 1,2..etc till 9

ltr_fst=ord('a')#Get ASCII of a
ltr_lst=ord('z')#Get ASCII of z
#for stk_ltr in range(ltr_fst, ltr_lst+1, 1):
#    print("Stock with : " +chr(stk_ltr))
#    pull_all_stks_lnk(base_url+chr(stk_ltr)) #Send complete url of stocks list starting with A, B..etc til Z

df=pandas.DataFrame(l)
df.to_csv("ET_Stock_Info.csv")
