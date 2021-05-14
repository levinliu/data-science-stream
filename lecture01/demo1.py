from bokeh.plotting import figure, show

#prepare some data
x = [2017, 2018, 2019, 2020, 2021]
y = [99.2, 132.2, 122.3, 110.0, 115.9]


#create a new plot with a title and axis labels
p = figure(title="PriceIndicator", x_axis_label="x", y_axis_label="y")

#add a line renderer with legend and line thickness
p.line(x, y, legend_label="黄金", line_width=2)

#show the results
show(p)
