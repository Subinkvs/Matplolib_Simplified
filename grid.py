import matplotlib.pyplot as plt
import numpy as np

'''
 grid() = grid() function in Matplotlib is used to enhance the readability and interpretability 
 of plots by adding a grid of horizontal and/or vertical lines. These lines serve as visual aids, 
 making it easier to analyze and understand the data presented in a graph.
'''

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 10, 15, 20, 25])

plt.grid(linewidth=1,
         color='Blue',
         linestyle='dashed')
plt.plot(x, y, marker='o')
plt.show()
