#Detailed Information on pandas_datareader can be found from below link
#https://pandas-datareader.readthedocs.io/en/latest/remote_data.html
#pandas-datareader support multiple fiancial website like google, yahoo
#google api is changed so using yahoo

from pandas_datareader import data
import datetime

strt=datetime.datetime(2018,1,1)
end=datetime.datetime(2018,1,17)

df=data.DataReader(name="RBLBANK.BO",data_source="yahoo",start=strt,end=end)
#in name we ne3ed to provide the scrip code from yahoo or if using google provide google's
#the DataReader is of type dataframe
print(df)
