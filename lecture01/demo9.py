from bokeh.layouts import layout
from bokeh.models import Div, RangeSlider, Spinner
from bokeh.plotting import figure, show

# prepare some data
x = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2010]
y = [54, 55, 45, 47, 52, 56, 34, 39, 51, 63]

# create plot with circle glyphs
p = figure(x_range=(2000, 2020), plot_width=500, plot_height=250)
points = p.circle(x=x, y=y, size=30, fill_color="#21a7df")

# set up textarea (div)
div = Div(
    text="""
          <p>这里指定圆点的大小-></p>
          """,
    width=200,
    height=30,
)

# set up spinner
spinner = Spinner(
    title="圆点大小",
    low=0,
    high=60,
    step=5,
    value=points.glyph.size,
    width=200,
)
spinner.js_link("value", points.glyph, "size")

# set up RangeSlider
range_slider = RangeSlider(
    title="调整 x轴的范围",
    start=2010,
    end=2020,
    step=1,
    value=(p.x_range.start, p.x_range.end),
)
range_slider.js_link("value", p.x_range, "start", attr_selector=0)
range_slider.js_link("value", p.x_range, "end", attr_selector=1)

# create layout
layout = layout(
    [
        [div, spinner],
        [range_slider],
        [p],
    ]
)

# show result
show(layout)
