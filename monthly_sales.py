
import pandas as pd
import matplotlib.pyplot as plt

# Load the analysed sales data
sales = pd.read_csv("analysed_sales.csv")

# Convert order date to datetime
sales["order_date"] = pd.to_datetime(
    sales["order_date"], format="mixed", dayfirst=True, errors="coerce"
)

# Remove rows with invalid dates
sales = sales.dropna(subset=["order_date"])

# Calculate monthly revenue
sales["month"] = sales["order_date"].dt.to_period("M").astype(str)
monthly_revenue = sales.groupby("month")["revenue"].sum()

# Create the chart
plt.figure(figsize=(10, 5))
monthly_revenue.plot(kind="line", marker="o")

plt.title("Monthly Coffee Shop Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig("monthly_sales_trend.png", dpi=300)
plt.show()

print("Monthly sales chart saved successfully!")
print(monthly_revenue)
