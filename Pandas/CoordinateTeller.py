import pandas
from geopy.geocoders import Nominatim

#Creating Pandas data frame for csv file
df = pandas.read_csv("supermarkets.csv")
#print(df)
#creating object of Nominatim
nom = Nominatim(scheme="http")

#Formating Address Column field in the dataframe to : Road , City , State ZIP, Country
df["Address"] = df["Address"]+", "+df["City"]+", "+df["State"]+", "+df["Country"]
#print(df)

#Iterating through each value of  Address field using "apply" method of Pandas and sending it as parmeter to geocode method of Nominatim to provide  the complete location infromation
#Creating a new column Coordinates to store complete location information of each Address.

df["Coordinates"] = df["Address"].apply(nom.geocode) #() are not required after geocode method as its auto applied by "apply" method


#Creating two new columns Latitude and Longitude to store that infromation in df dataframe
#We are using lambda to store the values of Coorinates column in a temp variable x and then use x.latitude to pull lattitude information from it
#One of the value in df["Coordinates"] is None type, so x.latitude wtill Error as it will be NoneType.latitude which was not expcted. So we use an if contoidion
#to use .latitude if x!=None
df["Latitude"] = df["Coordinates"].apply(lambda x:x.latitude if x!=None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x:x.longitude if x!=None else None)

print("Latidudes :\n",df["Latitude"])
print("\nLongitudes :\n",df["Longitude"])
