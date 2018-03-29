#this is an example of plotting

from bokeh.plotting import figure, output_file, show

p = figure(plot_width=500, plot_height=400, title = "Plotting Example") #Creating a figure with plot height and width

p.circle([1,3,5,7,9],[2,4,6,8,10], size=[i*2 for i in [5,6,7,8,9]], color="red", alpha=0.5)
#p.circle([1,3,5,7,9],[2,4,6,8,10], size=10, color="red", alpha=0.5)
#Providing the values for  x and y axis and circle will be drawn at that point alpha is for transparency
#We can also use square or triangle instead of circle
#Size i*2 for i in [] specifies the circle size for each value

output_file("plotting_ex.html")
#Writes to an html file
show(p)
