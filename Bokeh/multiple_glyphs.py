#Bokeh User Guide https://bokeh.pydata.org/en/latest/docs/user_guide.html
from bokeh.plotting import figure, output_file, show

p= figure(width=500, height=250,responsive=True) #Responsive puts plot accross the page

p.line([1,3,5,7],[2,4,6,8],line_width=1, alpha=0.5)
p.circle([1,3,5,7],[2,4,6,8], size = 10, alpha= 0.3, color = "Red")

output_file("glyphs.html")
show(p)
