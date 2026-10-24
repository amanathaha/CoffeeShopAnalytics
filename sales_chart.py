
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path("analysed_sales.csv")

sales = pd.read_csv(file_path)

# Calculate revenue by product
product_revenue = (
    sales.groupby("product_name")["revenue"]
    .sum()
    .sort_values(ascending=True)
    .tail(10)
)

# Create the chart
plt.figure(figsize=(10, 6))

product_revenue.plot(kind="barh")

plt.title("Top 10 Coffee Shop Products by Revenue")
plt.xlabel("Revenue (Rs.)")
plt.ylabel("Product")
plt.tight_layout()

# Save the chart
plt.savefig("top_products_revenue.png", dpi=300)

plt.show()

print("Chart saved as top_products_revenue.png")
