import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([2001, 2002, 2003, 2004], [112.3, 142.2, 122.9, 132.6])  # Plot some data on the axes.

plt.draw()

plt.show();
