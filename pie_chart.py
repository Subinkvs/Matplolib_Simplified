import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 15, 4])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]


plt.pie(y, labels= mylabels,
        autopct="%1.1f%%",
        explode=[0, 0, 0, 0.3],
        shadow=True,
        startangle=180)

plt.title('Fruit Sales')
plt.show()