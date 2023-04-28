from bokeh.plotting import figure
from bokeh.io import show,output_file
import pandas

df = pandas.read_csv("Bokeh/bachelors.csv")
x = df["Year"]
y = df["Engineering"]

output_file("plot.html")

f = figure()

f.line(x,y)

show(f)