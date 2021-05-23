import matplotlib.pyplot as plt

#prepare some data
x = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2010]
y = [54, 55, 45, 47, 52, 56, 34, 39, 51, 63]

area=500

#set marker refer to source : matplotlib/markers.py
plt.scatter(x, y, marker='d', c='red', s=area)

plt.show()
