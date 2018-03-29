
#pip install bokeh=0.12.6
#pip intsall bkcharts
#Bokeh User Guide https://bokeh.pydata.org/en/latest/docs/user_guide.html
from bkcharts import Scatter, output_file, show
import pandas

df = pandas.DataFrame(columns=["X","Y"])
df["X"]=[1,3,5,7,9]
df["Y"]=[2,4,6,8,0]

p = Scatter(df, x="X",y="Y", title="Scatter Test", xlabel="Odd Numbers", ylabel="Even Numbers")
# tools="" this will remove tool bar from the graph
# tools = "pan, resize" this will show only the listed tools
# logo = None this will remove the bokeh logo as well

output_file("Scatter_Example.html", mode="relative")
# default mode is cdn, we can pass mode ="relative"/"absolute"/"inline"
#cdn is content delivery network, the js and css file are donwloaded from intreenet, we can store them locally with relative or absolute.
#inline: javascript file and stylesheet will load in line in the html file

show(p)
