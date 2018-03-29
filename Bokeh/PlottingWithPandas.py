#pip install xlrd to read from excel file
import pandas
from bokeh.plotting import figure, output_file, show

df = pandas.read_excel("C://Sridhar//Z1//Learnings//Python//Codes//Programs//Bokeh//verlegenhuken.xlsx",sheet_name=0) #Read from excel
df["Temperature"] = df["Temperature"]/10
df["Pressure"] = df["Pressure"]/10

p=figure(plot_width=400, plot_height=400)

# tools="" this will remove tool bar from the graph
# tools = "pan, resize" this will show only the listed tools
# logo = None this will remove the bokeh logo as well

p.title.text="Temperature and Air Pressure"
p.title.text_color="Gray"
p.title.text_font="arial"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Temperature (°C)"
p.yaxis.axis_label="Pressure (hPa)"

p.circle(df["Pressure"],df["Temperature"],size=0.5, alpha=0.2)

output_file("pandas_temp_press.html")
#default mode is cdn, we can pass mode ="relative"/"absolute"/"inline"
#cdn is content delivery network, the js and css file are donwloaded from intreenet, we can store them locally with relative or absolute.
#inline: javascript file and stylesheet will load in line in the html file
show(p)
print(df)
