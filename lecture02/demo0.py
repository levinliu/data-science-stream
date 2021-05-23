import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [4, 3, 2, 1])  # Plot some data on the axes.

plt.draw()
plt.show()
