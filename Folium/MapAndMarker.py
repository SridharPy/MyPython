import folium

#For webmaps this library is used
#Provide Latitude and Longitude in Location param and zoom factor for zoon start
#Default tiles or map is loaded from "OpenStreetMap" dir(folium)or help(folium.Map)
#The default layer or basemap is coming from OpenStreetMap we can add other laeyrs or map aswell help(folium.Map) look for other tiles for base map
#We can add points on top of base layer

#Creating map object
map1 = folium.Map(location=[22.54489995,88.3425805274656],zoom_start = 6)
#Saving map object to a file
map1.save("India_Map.html")

#Using Mapbox Bright for basema
#Adding pointer on top of basemap
#Use help(folium.Map), we can see Marker or CircleMarker methods for marking on map2
#Also check help(folium.Marker), supply location coordinate (lat and long) when marker needs to be put, what message to pop up in popup and the icon plugin to set the color of icon etc
#We add a AMrker to our Map byt adding children to out Map using add_child
map2 = folium.Map(location = [22.54489995,88.3425805274656], zoom_start = 5, tiles = "MapBox Bright")
map2.add_child(folium.Marker(location =[22.54489995,88.3425805274656],popup = "Victoria Memorial, Kolkata", icon=folium.Icon(color="green")))
map2.save("India_Map_Bright.html")


#For better code organization and also to help add more layers and control layers by switching on them on or off  on the map later we use FeatureGroup:
#Basically Marker is a feature so we can create a featuregroup instead and add features to the featuregroug object  like Marker , polygrams etc
#then add that featuregroup object to our map and turn the features on or off later on the map

map3 = folium.Map(location=[42.2241632142232,-71.5217111261125],zoom_start=5)
#Creating a feature group object
fg = folium.FeatureGroup("US Map")
#Adding features to the feature group
fg.add_child(folium.Marker(location =[42.208363,-71.550869],popup="DellEMC Office, Hopkinton, MA", icon=folium.Icon("Orange")))
#Applying feature gorup fg features to mapobject map3
map3.add_child(fg)
#Saving the map object to an html file
map3.save("USA Map.html")
