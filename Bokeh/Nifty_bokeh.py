from bokeh.plotting import figure, output_file, show
import pandas

df = pandas.read_excel("https://www.nseindia.com/content/indices/top10nifty50_110118.csv",sheet_name=0)

p= figure(width=500, height = 250, responsive = True)

p.line(df["SECURITY"],df["WEIGHTAGE"], line_width=1, alpha=0.5)

output_file("Nifty_top_10.html")
show(p)
