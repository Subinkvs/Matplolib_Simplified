# ============================================================
# 1️⃣ BAR GRAPH: Total Quantity Sold by Category
# ============================================================
# Task: Create a bar graph to show the total quantity sold for each product category.
# Hint:
#   1. Group by 'Category' and sum 'Quantity'
#   2. Use plt.bar() to plot
#   3. Label X-axis, Y-axis, and add a title
# Example:
# category_quantity = df.groupby('Category')['Quantity'].sum()
# plt.bar(category_quantity.index, category_quantity.values)

# ============================================================
# 2️⃣ BAR GRAPH: Total Sales by Country
# ============================================================
# Task: Create a bar chart showing total sales for each country.
# Hint:
#   1. Add a 'Sales' column: df['Sales'] = df['Quantity'] * df['Price']
#   2. Group by 'Country' and sum 'Sales'
#   3. Sort values in descending order
#   4. Use plt.bar() to plot
#   5. Display the sales value above each bar

# ============================================================
# 3️⃣ LINE GRAPH: Daily Sales Trend
# ============================================================
# Task: Plot a line graph showing total sales per day.
# Hint:
#   1. Convert 'OrderDate' to datetime: df['OrderDate'] = pd.to_datetime(df['OrderDate'])
#   2. Group by 'OrderDate' and sum 'Sales'
#   3. Use plt.plot() with markers and line style
#   4. Label X-axis, Y-axis, and add a title

# ============================================================
# 4️⃣ LINE GRAPH: Category-wise Average Price
# ============================================================
# Task: Draw a line chart showing the average product price per category.
# Hint:
#   1. Group by 'Category' and calculate mean of 'Price'
#   2. Use plt.plot() with markers, colors, and line style
#   3. Label axes and add grid lines

# ============================================================
# 5️⃣ PIE CHART: Order Distribution by Category
# ============================================================
# Task: Create a pie chart showing the percentage of total orders for each category.
# Hint:
#   1. Use df['Category'].value_counts() to count orders
#   2. Use plt.pie() with autopct='%1.1f%%' and startangle=90
#   3. Add a title

# ============================================================
# 6️⃣ PIE CHART: Country-wise Share of Total Sales
# ============================================================
# Task: Plot a pie chart showing the share of total sales by country.
# Hint:
#   1. Group by 'Country' and sum 'Sales'
#   2. Use plt.pie() with labels, autopct='%1.1f%%', colors, and shadow=True
#   3. Add a title
