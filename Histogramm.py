import matplotlib.pyplot as plt
import numpy as np

'''
A histogram in Matplotlib is a graphical representation used to display the distribution of numerical data. 
It groups data into "bins" (intervals) and shows the frequency or count of data points falling within 
each bin as bars.
'''

x = np.random.normal(loc=70, scale=10, size=100)
x = np.clip(x, 0, 85)

plt.hist(x, bins=10, edgecolor='black')

plt.title('Test Scores')
plt.xlabel('Marks')
plt.ylabel('Students')

plt.show()