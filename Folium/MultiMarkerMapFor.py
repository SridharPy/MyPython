import folium

map1 = folium.Map(location =[18.500,73.700],zoom_start=12)

fg= folium.FeatureGroup("Map Feature")

for coordinates in [[18.577953,73.743163],[18.578726,73.765101]]:
    fg.add_child(folium.Marker(location=coordinates,popup="Multi-Marker Testing",icon=folium.Icon("blue")))

map1.add_child(fg)
map1.save("Dell EMC and DSP.html")
