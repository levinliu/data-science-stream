import matplotlib.pyplot as plt
import numpy as np
import pandas

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([2001, 2002, 2003, 2004], [112.3, 142.2, 122.9, 132.6])  # Plot some data on the axes.

a = pandas.DataFrame(np.random.randint(1,10,(3, 5))+2000, columns=list('abcde')) 
a2arr = a.values
print('a2arr %s ' % a2arr)
b = np.matrix([[1,2,3,4,5],[11,22,33,44,55],[111,222,333,444,555]])
b2arr = np.asarray(b)
print('b2arr %s ' % b2arr)

ax.plot(a2arr, b2arr)

plt.draw()

plt.show();
