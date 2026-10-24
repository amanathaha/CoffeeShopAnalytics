
import pandas as pd
from pathlib import Path
from datetime import datetime

# Load analysed sales data
sales = pd.read_csv("analysed_sales.csv")

# Calculate key metrics
total_revenue = sales["revenue"].sum()
total_profit = sales["gross_profit"].sum()
total_quantity = sales["quantity"].sum()
profit_margin = total_profit / total_revenue * 100 if total_revenue else 0

# Product and category performance
product_revenue = sales.groupby("product_name")["revenue"].sum()
category_revenue = sales.groupby("category")["revenue"].sum()

top_products = product_revenue.sort_values(ascending=False).head(10)
top_category = category_revenue.idxmax()

# Build HTML tables
product_table = top_products.rename("Revenue (Rs.)").to_frame().to_html(
    classes="data-table", float_format=lambda x: f"{x:,.2f}"
)
category_table = category_revenue.sort_values(
    ascending=False
).rename("Revenue (Rs.)").to_frame().to_html(
    classes="data-table", float_format=lambda x: f"{x:,.2f}"
)

# Chart images generated earlier
charts = [
    ("Top 10 Products by Revenue", "top_products_revenue.png"),
    ("Monthly Sales Trend", "monthly_sales_trend.png"),
    ("Revenue by Category", "category_sales.png"),
]

chart_html = ""
for title, filename in charts:
    if Path(filename).exists():
        chart_html += f"""
        <section>
            <h2>{title}</h2>
            <img src="{filename}" alt="{title}">
        </section>
        """
    else:
        chart_html += f"<p>Chart not found: {filename}</p>"

# Create report
report = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Coffee Shop Business Analytics Report</title>
<style>
body {{
    font-family: Arial, sans-serif;
    max-width: 1000px;
    margin: 30px auto;
    padding: 20px;
    color: #333;
    line-height: 1.6;
}}
h1, h2 {{ color: #6f4e37; }}
.metrics {{
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
}}
.metric {{
    background: #f5eee8;
    padding: 15px;
    flex: 1;
    min-width: 180px;
    border-radius: 8px;
}}
img {{ max-width: 100%; height: auto; }}
.data-table {{ border-collapse: collapse; width: 100%; }}
.data-table th, .data-table td {{
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}}
.data-table th {{ background: #6f4e37; color: white; }}
@media print {{
    body {{ margin: 0; max-width: none; }}
    section {{ break-inside: avoid; }}
}}
</style>
</head>
<body>
<h1>Coffee Shop Business Analytics Report</h1>
<p>Generated on: {datetime.now().strftime("%d %B %Y")}</p>

<h2>1. Executive Summary</h2>
<p>This report summarizes coffee shop sales, product performance,
category revenue, and gross profitability based on the analysed dataset.
The dataset is simulated for educational purposes.</p>

<h2>2. Key Performance Indicators</h2>
<div class="metrics">
    <div class="metric">
        <strong>Total Revenue</strong><br>
        Rs. {total_revenue:,.2f}
    </div>
    <div class="metric">
        <strong>Gross Profit</strong><br>
        Rs. {total_profit:,.2f}
    </div>
    <div class="metric">
        <strong>Quantity Sold</strong><br>
        {total_quantity:,.0f}
    </div>
    <div class="metric">
        <strong>Gross Profit Margin</strong><br>
        {profit_margin:.2f}%
    </div>
</div>

<h2>3. Top 10 Products by Revenue</h2>
{product_table}

<h2>4. Revenue by Category</h2>
{category_table}
<p>The highest-revenue category is <strong>{top_category}</strong>.</p>

<h2>5. Visual Analysis</h2>
{chart_html}

<h2>6. Business Insights</h2>
<ul>
    <li>The highest-revenue product is
        <strong>{top_products.index[0]}</strong>.</li>
    <li>The highest-revenue category is <strong>{top_category}</strong>.</li>
    <li>The gross profit margin is {profit_margin:.2f}%.</li>
</ul>

<h2>7. Recommendations</h2>
<ul>
    <li>Keep sufficient inventory for high-revenue products.</li>
    <li>Review low-revenue products before deciding whether to promote them.</li>
    <li>Monitor product costs, discounts, and profit margins.</li>
    <li>Use monthly sales patterns to plan stock and promotions.</li>
</ul>

<h2>8. Limitations</h2>
<p>The dataset is simulated, so results do not represent a real business.
Revenue and profit calculations depend on the available prices, costs,
and discounts. Revenue alone does not establish which products are most
popular by quantity.</p>

</body>
</html>
"""

Path("final_coffee_shop_report.html").write_text(report, encoding="utf-8")

print("Final report created: final_coffee_shop_report.html")
print("Open this file in your browser to view the report.")
