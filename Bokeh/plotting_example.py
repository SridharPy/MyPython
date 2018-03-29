from bokeh.plotting import figure, output_file, show
import pandas

#p = figure(plot_width=500, plot_height=400, title="Plotting Example") or add title using below command
p = figure(plot_width=500, plot_height=400)

p.title.text="Plotting Example"
p.title.text_color="Orange"
p.title.text_font ="Times"
p.title.text_font_style="italic"

p.yaxis.minor_tick_line_color=None
p.xaxis.minor_tick_line_color="Red"

p.xaxis.axis_label="Odd Numbers"
p.yaxis.axis_label="Even Numbers"
#to get all attributes of figure type help(p)

#p.circle([1,3,5,7,9],[2,4,6,8,10],size =10, alpha=0.4)
p.circle([1,3,5,7,9],[2,4,6,8,10],size =[i*2 for i in [5,6,7,8,9]], alpha=0.4)

output_file("plotting_example.html")
show(p)
