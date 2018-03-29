#Bokeh and bkcharts are depricated
#To use bokeh dont install default instead use:  pip install bokeh==0.12.5
#or  pip install bokeh==0.12.6
#pip install bkcharts

from bkcharts import Scatter, output_file, show
import pandas

df = pandas.DataFrame(columns=["X","Y"])
df["X"]=[1,3,5,7,9,11,13,15,17,19,21]
df["Y"]=[2,4,6,8,10,12,14,16,18,20,22]

p=Scatter(df,x='X',y='Y',title='Test BK Charts', xlabel="Odd Numbers", ylabel="Even Numbers")
#Creates scatter object passing data frame, x axis value with data frame values of X and y axis value with data frame values of Y, title, x label, y label
output_file=("Scatter_File_Ex.html") #Displaying the output  in html format
show(p) #Showing the output
