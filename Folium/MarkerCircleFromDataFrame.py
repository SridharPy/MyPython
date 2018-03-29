import pandas
import folium
import webcolors #This library needs br installed to convert a color into html hex,
#for this code this library was not required as we can also provid ethe color name firectly instaead of converting to hex

df = pandas.read_csv("C://Z Virtual Machines//Python Code//Folium//app2-web-map//Volcanoes_USA.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])

def produce_color(e):
    if e<1000:
        return webcolors.name_to_hex("green") # Can also pass return "green" isntead of hex as CircleMarker color and fill_color can take text value of the color
    elif 1000<=e<3000:
        return webcolors.name_to_hex("orange")
    else:
        return webcolors.name_to_hex("red")

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles = "Mapbox Bright")
fg = folium.FeatureGroup("My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location = [lt, ln], popup = "Elevation is : " +str(el)+"m" , radius = 7, fill = True, fill_color=produce_color(el), color= "grey", fill_opacity = .8 ))

map.add_child(fg)
map.save("USA Volcanos CircleMarker.html")

"""
Help on help(folium.CircleMarker)
class CircleMarker(folium.map.Marker)
 |  Creates a CircleMarker object for plotting on a Map.
 |
 |  Parameters
 |  ----------
 |  location: tuple or list
 |      Latitude and Longitude of Marker (Northing, Easting)
 |  radius: int
 |      The radius of the circle in pixels.
 |      For setting the radius in meter, use Circle.
 |  color: str, default '#3388ff'
 |      The color of the marker's edge in a HTML-compatible format.
 |  fill: bool, default False
 |      If true the circle will be filled.
    fill_color: str, default to the same as color
 |      The fill color of the marker in a HTML-compatible format.
 |  fill_opacity: float, default 0.2
 |      The fill opacity of the marker, between 0. and 1.
 |  popup: string or folium.Popup, default None
 |      Input text or visualization for object.
 |
 |  See http://leafletjs.com/reference-1.2.0.html#path for more otions.
 |
"""
