import requests
from bs4 import BeautifulSoup
import pandas

all_info=[]
l=[]

def stock_info(stock):
    d={}
    try:
        stock_page=requests.get(stock)
        stock_cont= stock_page.content
        bs_stock=BeautifulSoup(stock_cont,"html.parser")
    except:
        pass
    try:
        #General Data
        d["Stock Name"]=bs_stock.find("h1", {"class":"b_42 company_name"}).text
        d["Stock Sector"]=bs_stock.find("a",{"class":"gry10"}).text
        d["Senti Buy"]= bs_stock.find("span",{"class":"pl_txt"}).text
        d["Senti Sell"]= bs_stock.find("span",{"class":"pl_txt rtxt"}).text
        d["Senti Hold"]= bs_stock.find("span",{"class":"pl_txt grytxt"}).text
        #d["Senti Recommend"]= bs_stock.find("p",{"class":"gDl_15"}).text
        d["Senti Recommend"]= bs_stock.find("span",{"class":"grnb_20"}).text +" "+ bs_stock.find("span",{"class":"gD_18"}).text

    except:
        pass

    try:
        d["NSE Price"]=bs_stock.find("span",{"id":"Nse_Prc_tick"}).text
        d["NSE Prev Close"]=bs_stock.find("div",{"id":"n_prevclose"}).text
        d["NSE Open"]=bs_stock.find("div",{"id":"n_open"}).text
        d["NSE Vol"]= bs_stock.find("span",{"id":"nse_volume"}).text
        d["NSE Vol 5"]=bs_stock.find("td",{"id":"avgvol5daysN"}).text
        d["NSE Vol 10"]=bs_stock.find("td",{"id":"avgvol10daysN"}).text
        d["NSE Vol 30"]= bs_stock.find("td",{"id":"avgvol30daysN"}).text
        d["NSE Buy QTY"]= bs_stock.find("p",{"id":"n_total_buy_qty"}).text
        d["NSE Sell QTY"]= bs_stock.find("p",{"id":"n_total_sell_qty"}).text
    except:
        pass

    try:
        d["BSE Price"]=bs_stock.find("span",{"id":"Bse_Prc_tick"}).text
        d["BSE Prev Close"]=bs_stock.find("div",{"id":"b_prevclose"}).text
        d["BSE Open"] = bs_stock.find("div",{"id":"b_open"}).text
        d["BSE Vol"]= bs_stock.find("span",{"id":"bse_volume"}).text
        d["BSE Vol 5"]=bs_stock.find("td",{"id":"avgvol5daysB"}).text
        d["BSE Vol 10"]=bs_stock.find("td",{"id":"avgvol10daysB"}).text
        d["BSE Vol 30"]= bs_stock.find("td",{"id":"avgvol30daysB"}).text
        d["BSE Buy QTY"]= bs_stock.find("p",{"id":"b_total_buy_qty"}).text
        d["BSE Sell QTY"]= bs_stock.find("p",{"id":"b_total_sell_qty"}).text
    except:
        pass

    return(d)


home_page=requests.get("http://www.moneycontrol.com/india/stockpricequote/") # Go to Stocks Page
cont=home_page.text

bs = BeautifulSoup(cont,"html.parser")
stock_table=bs.find_all("table",{"class":"pcq_tbl MT10"})

for item in stock_table:
    links_list=item.find_all('a')
    #print(links_list)
    for stock in links_list:
        stock_link=stock.get("href")
        #print(stock_link)
        l.append(stock_info(stock_link))
        print(l)


df=pandas.DataFrame(l)
df.to_csv("Stocks_All_Price_22_Jan.csv")