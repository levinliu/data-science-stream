from bokeh.plotting import figure, output_file, save

# prepare some data
x = [2017, 2018, 2019, 2020, 2021]
y = [83.3, 88.3, 75, 79, 82.9]

# set output to static HTML file
output_file(filename="price_indicator.html", title="Static HTML file")

# create a new plot with a specific size
p = figure(sizing_mode="stretch_width", max_width=500, plot_height=250)

# add a circle renderer
circle = p.circle(x, y, fill_color="red", size=15)

# save the results to a file
save(p)
