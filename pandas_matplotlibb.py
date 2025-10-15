import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df)


line_style = dict(marker='o', 
         markersize=10,
         markerfacecolor='Red',
         markeredgecolor='Red',
         linestyle='solid',
         linewidth=2,
         color='Blue')

category_quantity = df.groupby('Category')['Quantity'].sum()
print(category_quantity)

# ---------- (1) Line Chart ----------
plt.plot(category_quantity.index, category_quantity.values, **line_style)

# ---------- (2) Bar Chart ----------
# plt.bar(category_quantity.index, category_quantity.values)

plt.title('Total Quantity Sold by Category')
plt.xlabel('Category')
plt.ylabel('Total Quantity')

# ---------- (3) Pie Chart ----------

# plt.pie(category_quantity.values, labels=category_quantity.index, autopct="%1.1f%%",)


plt.show()