
import pandas as pd

# Load analysed sales data
sales = pd.read_csv("analysed_sales.csv")

# Calculate key business metrics
total_revenue = sales["revenue"].sum()
total_quantity = sales["quantity"].sum()
total_profit = sales["gross_profit"].sum()

profit_margin = (
    total_profit / total_revenue * 100
    if total_revenue != 0 else 0
)

# Find best-performing product
product_revenue = sales.groupby("product_name")["revenue"].sum()
best_product = product_revenue.idxmax()
best_product_revenue = product_revenue.max()

# Find best-performing category
category_revenue = sales.groupby("category")["revenue"].sum()
best_category = category_revenue.idxmax()
best_category_revenue = category_revenue.max()

# Generate insights
insights = f"""
COFFEE SHOP BUSINESS ANALYTICS REPORT
=====================================

1. KEY PERFORMANCE INDICATORS

Total Revenue: Rs. {total_revenue:,.2f}
Total Quantity Sold: {total_quantity}
Gross Profit: Rs. {total_profit:,.2f}
Gross Profit Margin: {profit_margin:.2f}%

2. PRODUCT PERFORMANCE

Top Product: {best_product}
Revenue from Top Product: Rs. {best_product_revenue:,.2f}

3. CATEGORY PERFORMANCE

Top Category: {best_category}
Category Revenue: Rs. {best_category_revenue:,.2f}

4. BUSINESS INSIGHTS

- The top-selling product by revenue is {best_product}.
- The highest-revenue category is {best_category}.
- The gross profit margin is {profit_margin:.2f}%.

5. BUSINESS RECOMMENDATIONS

- Maintain sufficient stock of the best-performing products.
- Promote products in lower-revenue categories using offers.
- Monitor product costs and discounts to protect profit margins.
- Review monthly sales trends to plan promotions and inventory.
"""

# Display report
print(insights)

# Save report to a text file
with open("business_insights_report.txt", "w", encoding="utf-8") as file:
    file.write(insights)

print("\nBusiness insights report saved successfully!")
