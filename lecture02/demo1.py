import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

plt.rcParams['font.sans-serif'] = 'Arial Unicode MS'

#prepare some data
x = [2017, 2018, 2019, 2020, 2021]
y = [99.2, 132.2, 122.3, 110.0, 115.9]

#create a figure containing a single axes
fig, ax = plt.subplots() 
#plot some data on the axes
ax.plot(x, y, label=u"黄金")

ax.set_title("PriceIndicator")
ax.set_xlabel("x")
ax.set_ylabel("y")

#display legend or it won't display
ax.legend()
# set xaxis display as integer format, default is float type
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

#plt.draw()
plt.show();
