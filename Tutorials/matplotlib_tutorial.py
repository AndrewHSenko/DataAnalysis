##################################################################################################################
#                                            MATPLOTLIB TUTORIAL                                                 #
# Courtesy of NeuralNine: https://www.youtube.com/watch?v=OZOOLe2imFohttps://www.youtube.com/watch?v=OZOOLe2imFo #
# Covers:                                                                                                        #
# - Creating all standard graphs and charts                                                                      #
# - Layering, inline styling, and using a stylesheet                                                             #
# - 3D projections and animating                                                                                 #
##################################################################################################################
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use("ggplot")

heads_tails = [0, 0]

for _ in range(100000):
    heads_tails[random.randint(0, 1)] += 1
    plt.bar(["Heads", "Tails"], heads_tails, color=["red", "blue"])
    plt.pause(0.002)
plt.show()

# ax = plt.axes(projection="3d")

# x = np.arange(-5, 5, 0.1)
# y = np.arange(-5, 5, 0.1)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(X) * np.cos(Y)

# ax.plot_surface(X, Y, Z, cmap="Spectral")
# ax.set_title("3D Plot")
# ax.view_init(azim=0, elev=90)

# x1, y1 = np.random.random(100), np.random.random(100)
# x2, y2 = np.arange(100), np.random.random(100)

# plt.figure(1)
# plt.scatter(x1, y1)

# plt.figure(2)
# plt.plot(x2, y2)

# x = np.arange(100)
# fig, axs = plt.subplots(2, 2) # 4 subplots

# ul = axs[0, 0]
# ur = axs[0, 1]
# ll = axs[1, 0]
# lr = axs[1, 1]
# ul.plot(x, np.sin(x))
# ul.set_title("Sine Wave")

# ur.plot(x, np.cos(x))
# ur.set_title("Cosine Wave")

# ll.pie(x)
# ll.set_title("Groooovy")

# lr.scatter(x, np.random.randint(0, 101, 100), s=25)
# lr.set_title("Pointilism")

# fig.suptitle("Four Plots")

# plt.tight_layout() # Prevents overlap
# plt.show()
# plt.savefig("fourplots.png", dpi=300, transparent=True, bbox_inches="tight") # Export

# Inline styling

# years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
# income = [55, 56, 62, 61, 72, 72, 73, 75]
# income_ticks = list(range(50, 81, 2))

# plt.plot(years, income)
# plt.title("Income of John (in USD)", fontsize=24, fontname="Impact")
# plt.xlabel("Year")
# plt.ylabel("Income in USD")
# plt.yticks(income_ticks, [f'${x}k USD' for x in income_ticks])

# stock_a = np.random.randint(100, 111, 7)
# stock_b = np.random.randint(90, 111, 7)
# stock_c = np.random.randint(100, 121, 7)

# plt.plot(stock_a, label="Company1")
# plt.plot(stock_b, label="Company2")
# plt.plot(stock_c, label="Company3")
# plt.legend(loc="lower right")

# votes = [10, 2, 5, 16, 22]
# people = ["A", "B", "C", "D", "E"]

# plt.pie(votes, labels=None)
# plt.legend(labels=people, loc="upper left")

# plt.show()

# Box Plot chart
# heights = np.random.normal(172, 8, 300)

# plt.boxplot(heights)
# plt.show()

# a = np.linspace(0, 10, 25)
# b = np.linspace(10, 200, 25)
# c = np.linspace(200, 210, 25)
# d = np.linspace(210, 230, 25)
# data = np.concatenate((a, b, c, d))

# plt.boxplot(data)
# plt.show()

# Pie chart
# x = ["C++", "C#", "Python", "Java", "Go"]
# y = [50, 24, 14, 6, 17]
# explodes = [0, 0, 0, 0.2, 0]

# plt.pie(y, labels=x, explode=explodes, autopct="%.2f%%", pctdistance=1.4, startangle=45) # startangle rotates ccw
# plt.show()

# Histogram
# ages = np.random.normal(20, 1.5, 1000)
# plt.hist(ages, bins=(
#         [ages.min(), 18, 21, ages.max()]
#     ), cumulative=True)
# plt.show()

# Scatter plot
# X_data = np.random.random(1000) * 100
# Y_data = np.random.random(1000) * 100

# plt.scatter(X_data, Y_data, c="#e95f30", marker="*", s=50, alpha=0.7)
# plt.show()

# Line graph
# years = [2006 + x for x in range(16)]
# weights = [125, 136, 140, 139, 156, 145, 147, 145, 146, 141, 140, 142, 146, 145, 143, 140]

# plt.plot(years, weights, "g--", lw=3)# "g--" = (c="g", linestyle="--")
# plt.show()

# Bar graph
# x = ["C++", "C#", "Python", "Java", "Go"]
# y = [20, 50, 140, 1, 45]

# plt.bar(x, y, color="y", align="edge", width=0.5, edgecolor="black")
# plt.show()

