from MotionDetector_Video_Bokeh import df #This will call the MotionDetector Programs
from bokeh.plotting import figure, output_file, show

p=figure(x_axis_type="datetime", width = 500, height=100, responsive=True, title="Motion_Capture_Graph")
#x axis data type is set to datetime
p.yaxis.minor_tick_line_color = None #To remove minor ticks from y axis
p.ygrid[0].ticker.desired_num_ticks=1 #To remove horizontal y axis grids from plot.
#ygrid is a list and we have to access first object in the grid and remove the lines byt settng it to 1
p.quad(left=df["Start"] ,right=df["End"] , top=1, bottom=0, color="Green")
#df["Start"] is the start time of object entry from the MotionDetector_Video_Bokeh py file
#df["End"] is the exit time of object from the MotionDetector_Video_Bokeh py file

output_file("Motion_Graph.html")
show(p)
