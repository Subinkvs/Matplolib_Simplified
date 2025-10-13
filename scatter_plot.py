import matplotlib.pyplot as plt
import numpy as np

'''
A scatter plot in Matplotlib is a type of plot that displays individual data points as markers 
on a two-dimensional graph. It is used to visualize the relationship between two numerical variables, 
where each point represents an observation with its x and y coordinates corresponding to the values 
of these variables.
'''


x1 = np.array([0, 1, 5, 6, 7, 4, 4, 3, 8])
y1 = np.array([10, 20,50, 65, 75, 60, 60, 55, 85])

plt.title('Test Scores')
plt.xlabel('Hours studied')
plt.ylabel('Marks')

plt.scatter(x1, y1, color='Blue',
            s = 50,
            label='Class A')

plt.legend()
plt.show()