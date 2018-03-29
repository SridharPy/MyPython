from bokeh.plotting import figure, output_file, show
import pandas

#df = pandas.read_excel("http://www.google.com/finance/historical?q=NASDAQ:ADBE&startdate=Jan+01%2C+2009&enddate=Aug+2%2C+2012&output=csv", parse_dates=["Date"])
#since the above link is blocked in office laptop/network, so using same file locally stored in PC
df= pandas.read_csv("C://Sridhar//Z1//Learnings//Python//Codes//Programs//Bokeh//adbe.csv", parse_dates=["Date"])
# parse_dates here provide the Date column from excel

p=figure(width = 500, height= 250,x_axis_type = "datetime", responsive=True)
#responsive = True ; To extend graph to all throughout the page

p.line(df["Date"],df["Close"], color="Green", alpha=0.5)
#line_width = 1, we can set line width here

output_file("Financial_Graph.html")

show(p)
