from geopy.geocoders import Nominatim

street = input("Enter Street Name: ")
city = input("Enter City Name: ")
state = input("Enter State Name: ")
#pin = input("Enter PIN Code: ")
#country = input("Enter Country Name")

coord = street + ", "+city+", "+state
nom = Nominatim(scheme="http")
loc = nom.geocode(coord)
if loc !=None:
    lat = loc.latitude
    lon = loc.longitude
    print("For the location : " + street + ", " +city+", "+state+ "\nLatitude is : ",lat,"\nLongitude is : ",lon )
else:
    print("This location not found in our database",loc)
