
import pandas as pd
import matplotlib.pyplot as plt

# Load analysed sales data
sales = pd.read_csv("analysed_sales.csv")

# Calculate revenue by category
category_revenue = sales.groupby("category")["revenue"].sum()
category_revenue = category_revenue.sort_values(ascending=False)

# Display results
print("Revenue by Product Category:")
print(category_revenue)

# Create chart
plt.figure(figsize=(9, 5))
category_revenue.plot(kind="bar")

plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("category_sales.png", dpi=300)
plt.show()

print("Category sales chart saved successfully!")
