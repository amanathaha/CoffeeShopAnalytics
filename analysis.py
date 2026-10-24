
import pandas as pd
from pathlib import Path

file_path = Path("coffee_shop_business_analytics_dataset.xlsx")

# Load sales and product costs
sales = pd.read_excel(file_path, sheet_name="Raw_Sales")
products = pd.read_excel(file_path, sheet_name="Product_Reference")

# Remove duplicate transactions
sales = sales.drop_duplicates(
    subset="transaction_id", keep="first"
)

# Clean date and numeric columns
sales["order_date"] = pd.to_datetime(
    sales["order_date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

for col in ["quantity", "unit_price", "discount"]:
    sales[col] = pd.to_numeric(sales[col], errors="coerce")

sales["category"] = (
    sales["category"].astype("string").str.strip().str.title()
)

# Remove rows missing essential sales information
sales = sales.dropna(
    subset=["order_date", "quantity", "unit_price"]
)

# Join product costs using product_id
sales = sales.merge(
    products[["product_id", "unit_cost"]],
    on="product_id",
    how="left",
    validate="many_to_one"
)

# Calculate revenue, cost and gross profit
sales["revenue"] = (
    sales["quantity"] * sales["unit_price"]
    - sales["discount"]
)

sales["product_cost"] = (
    sales["quantity"] * sales["unit_cost"]
)

sales["gross_profit"] = (
    sales["revenue"] - sales["product_cost"]
)

# Overall results
total_revenue = sales["revenue"].sum()
total_cost = sales["product_cost"].sum()
total_profit = sales["gross_profit"].sum()

print("\nCOFFEE SHOP PROFIT ANALYSIS")
print("=" * 40)
print(f"Transactions analysed: {len(sales)}")
print(f"Total revenue: Rs. {total_revenue:,.2f}")
print(f"Total product cost: Rs. {total_cost:,.2f}")
print(f"Gross profit: Rs. {total_profit:,.2f}")

if total_revenue != 0:
    print(
        f"Gross profit margin: "
        f"{total_profit / total_revenue * 100:.2f}%"
    )

# Profit by product
print("\nTOP 10 PRODUCTS BY GROSS PROFIT")
print("-" * 40)

profit_by_product = (
    sales.groupby("product_name")["gross_profit"]
    .sum()
    .sort_values(ascending=False)
)

print(profit_by_product.head(10).round(2).to_string())

# Profit by category
print("\nGROSS PROFIT BY CATEGORY")
print("-" * 40)

profit_by_category = (
    sales.groupby("category")["gross_profit"]
    .sum()
    .sort_values(ascending=False)
)

print(profit_by_category.round(2).to_string())

# Save the analysed data
sales.to_csv("analysed_sales.csv", index=False)
print("\nSaved detailed results to analysed_sales.csv")
