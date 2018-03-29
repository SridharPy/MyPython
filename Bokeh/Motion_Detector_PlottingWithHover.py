from MotionDetector_Video_Bokeh import df #This will call the MotionDetector Programs
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

#Since ColumnDataSource can't transalate Start and End column from df to datetime format we convert is manually.

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
#Convereted Start and END column values to datetime format Year Month Day Hour Min Sec no we will supply it to the plot

cds=ColumnDataSource(df) #Creates cds object specifyng the datasource i.e. pandas dataframe for Columns to be used in bokeh plotting

p=figure(x_axis_type="datetime", width = 500, height=100, responsive=True, title="Motion_Capture_Graph")
#x axis data type is set to datetime
p.yaxis.minor_tick_line_color = None #To remove minor ticks from y axis
p.ygrid[0].ticker.desired_num_ticks=1 #To remove horizontal y axis grids from plot.
#ygrid is a list and we have to access first object in the grid and remove the lines byt settng it to 1

#hover = HoverTool(tooltips=[("Start","@Start"),("End", "@End")]) specify the hover text with array of values with @
hover = HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")]) #Specifying the date tome converted df column values
p.add_tools(hover)
#q=p.quad(left=df["Start"] ,right=df["End"], bottom=0, top=1, color="green", source=cds)
#left, right, bottom, top are the values for the quadrant to be drawn
#df["Start"] is the start time of object entry from the MotionDetector_Video_Bokeh py file
#df["End"] is the exit time of object from the MotionDetector_Video_Bokeh py file

q= p.quad(left="Start",right="End",bottom=0, top=1, color="green", source=cds )
#Here we are using cds as the column data source which is fetched from dataframe in Montion_Detetctor_video_bokeh
#Instead of df["Start"]/df["End"] we can/have to use the actual column name itself from the dataframe

output_file("Motion_Graph.html")
show(p)
