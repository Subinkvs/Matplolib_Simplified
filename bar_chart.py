import matplotlib.pyplot as plt
import numpy as np

'''
A bar chart, or bar graph, in Matplotlib is a type of data visualization that uses rectangular bars 
to represent categorical data. The length or height of each bar is proportional to the value it 
represents, making it easy to compare different categories.
'''

fruits = np.array(['Apples', 'Bananas', 'Cherries', 'Dates'])
sales = np.array([400, 350, 300, 450])

line_style = dict(fontsize=15,
             family='Arial',
             fontweight='bold',
             color='Blue')

plt.bar(fruits, sales, color='skyblue')
plt.title('Fruit Sales', fontsize=10,color='Blue')
plt.xlabel('Fruits', **line_style)
plt.ylabel('Sales', **line_style)
plt.show()
