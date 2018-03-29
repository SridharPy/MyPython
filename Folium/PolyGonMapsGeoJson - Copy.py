import pandas
import folium
#import webcolors #This library needs br installed to convert a color into html hex,
#for this code this library was not required as we can also provid ethe color name firectly instaead of converting to hex

df = pandas.read_csv("C://Z Virtual Machines//Python Code//Folium//app2-web-map//Volcanoes_USA.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])

def produce_color(e):
    if e<1000:
        return "green"
    elif 1000<=e<3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58,-99.09], zoom_start=3, tiles = "Mapbox Bright")
fgv = folium.FeatureGroup("Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt, ln], popup = "Elevation is : " +str(el)+"m", radius = 7, fill = True, fill_color=produce_color(el), color= "grey", fill_opacity = .8 ))

fgp = folium.FeatureGroup("Population")
#fg.add_child(folium.GeoJson(data=(open('world.json','r', encoding='utf-8-sig').read())))
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"]<=10000000 else "orange" if 10000000<x["properties"]["POP2005"]<=100000000 else "red" if 100000000<x["properties"]["POP2005"]<500000000 else "black"}))
#world.json is a geojson file with polygon, we are loading it to the map and polygons are formed on the lat and long of each country
#We are loading opening world.json as read and then reading it with .read() and feeding it into data and that is used by folium.GeoJson to create polygon on the map by adding it in feture group fg along with above feature
#by creating featuregroup we can add multiple features to it. Or Create separate features for Marker and Polygons and use LayerControl to enable each feature in map
#Recent version of folium needs a string instead of files as data input . Therefore we need to add read() method
#in GeoJason we can alos add  point layers and ,line layer (like we did in above fg.add where we used CircleMarker which is a point marker)
#point marker is used for a location, line markesr are used for roads or rivers and polygon marker layer is used for an area.
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("World Map_Vol_Pop.html")
