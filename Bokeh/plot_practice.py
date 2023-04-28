from bokeh.plotting import output_file, show, figure
import pandas as pd

df = pd.read_excel("Bokeh/verlegenhuken.xlsx")

x = df["Temperature"]/10
y = df["Pressure"]/10

f = figure(plot_width=500,plot_height=400)

#Title formatting
f.title.text = "Temperature and Air Pressure"
f.title.text_color = "Gray"
f.title.text_font="times"
f.title.text_font_style="bold"

#Minor Line Color
f.xaxis.minor_tick_line_color="Red"
f.yaxis.minor_tick_line_color=None

#X-axis
f.xaxis.axis_label_text_font="Verdana"
f.xaxis.axis_label="Temperature(C)"
f.xaxis.axis_label_text_font_style="bold italic"

#Y-axis
f.yaxis.axis_label_text_font="Verdana"
f.yaxis.axis_label="Pressure(hPa)"
f.yaxis.axis_label_text_font_style="bold" 

f.circle(x,y,size = 0.5)
output_file("Weather_data.html")
show(f)
#Link to circle properties - https://www.geeksforgeeks.org/bokeh-plotting-figure-circle-function-in-python/

#Solution
import pandas
 
from bokeh.plotting import figure, output_file, show
 
df=pandas.read_excel("Bokeh/verlegenhuken.xlsx")
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10
 
p=figure(plot_width=500,plot_height=400,tools='pan')
 
p.title.text="Temperature and Air Pressure"
p.title.text_color="Gray"
p.title.text_font="arial"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Temperature (°C)"
p.yaxis.axis_label="Pressure (hPa)"    
 
p.circle(df["Temperature"],df["Pressure"],size=0.5)
output_file("Weather.html")
show(p)