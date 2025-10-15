import matplotlib.pyplot as plt
import numpy as np

x = np.array([2022, 2023, 2024, 2025])

y1 = np.array([0, 0, 23, 25])
y2 = np.array([5, 15, 10, 20])
y3 = np.array([6, 8, 10, 12])

line_style = dict(marker='o', 
         markersize=10,
         markerfacecolor='Red',
         markeredgecolor='Red',
         linestyle='solid',
         linewidth=2,
         color='Blue')

plt.plot(x, y1, **line_style)


plt.plot(x, y2, **line_style) 

plt.plot(x, y3,  **line_style)
plt.show()