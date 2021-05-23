import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

plt.rcParams['font.sans-serif'] = 'Arial Unicode MS'

#prepare some data
x = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
y1 = [91.6, 89.2, 83.3, 88.3, 75, 79, 82.9]
y2 = [81.3, 79.2, 99.2, 132.2, 122.3, 110.0, 115.9]
y3 = [66.9, 66.7, 52.2, 62.2, 54.8, 55.0, 61.0]

#create a figure containing a single axes
fig, ax = plt.subplots() 
#plot some data on the axes
ax.plot(x, y1, label=u"铂金", color="green")
ax.plot(x, y2, label=u"黄金", color="blue")
#print('y3 %s ' % len(y3))
ax.plot(x, y3, label=u"白银", color="red")

ax.set_title("PriceIndicator")
ax.set_xlabel("x")
ax.set_ylabel("y")

#display legend or it won't display
ax.legend()
# set xaxis display as integer format, default is float type
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

#plt.draw()
plt.show();
