import matplotlib
import matplotlib.pyplot as plt
import numpy as np

bkend='qt5agg'
#bkend='GTK3Agg' #not installed, will fail
#bkend='BELevinNotExist' 
"""
backend; supported values are ['GTK3Agg', 'GTK3Cairo', 'MacOSX', 'nbAgg', 'Qt4Agg', 'Qt4Cairo', 'Qt5Agg', 'Qt5Cairo', 'TkAgg', 'TkCairo', 'WebAgg', 'WX', 'WXAgg', 'WXCairo', 'agg', 'cairo', 'pdf', 'pgf', 'ps', 'svg', 'template']
"""
#bkend='TkAgg' #can use this as it's the latestpython(3.8+) builtin
matplotlib.use(bkend)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([2001, 2002, 2003, 2004], [112.3, 142.2, 122.9, 132.6])  # Plot some data on the axes.

plt.draw()

plt.show();
