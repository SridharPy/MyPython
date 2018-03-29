import pandas
import folium


df = pandas.read_csv("C://Z Virtual Machines//Python Code//Folium//app2-web-map//Volcanoes_USA.txt")
lat = list(df["LAT"]) #load lat column from df into a list
lon = list(df["LON"]) #load lon column from df into a list
elev = list(df["ELEV"]) #Load Elev column from df into a list, ELEV is a float

def color(e):
    if e <=1000:
        return"green"
    elif 1000<= e < 3000:
        return"orange"
    else:
        return"red"

map = folium.Map(location=[38.58,-99.09],zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup("My Map")
for lt,ln,el in zip(lat,lon,elev):

    fg.add_child(folium.Marker(location=[lt,ln],popup="Elevation is : "+str(el)+"m", icon = folium.Icon(color(el)))) #here We are converting el which is float into stringa and supplying it to popup
    #We are calling function color to return icon marker color based on the elevation of volcano

map.add_child(fg)

map.save("world map.html")
