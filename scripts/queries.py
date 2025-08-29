import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite DB
engine = create_engine("sqlite:///./data/ecommerce.db")

# 1. Total number of rows
total_rows = pd.read_sql("SELECT COUNT(*) as count FROM sales;", con=engine)
print("\nTotal Rows in Sales Table:", total_rows.iloc[0]["count"])

# 2. Top 10 products by revenue (GBP)
top_products = pd.read_sql("""
    SELECT Description, ROUND(SUM(Revenue_GBP), 2) as TotalRevenue_GBP
    FROM sales
    GROUP BY Description
    ORDER BY TotalRevenue_GBP DESC
    LIMIT 10;
""", con=engine)
print("\nTop 10 Products by Revenue (GBP):\n", top_products)

# 3. Revenue by country (USD)
revenue_by_country = pd.read_sql("""
    SELECT Country, ROUND(SUM(Revenue_USD), 2) as TotalRevenue_USD
    FROM sales
    GROUP BY Country
    ORDER BY TotalRevenue_USD DESC
    LIMIT 10;
""", con=engine)
print("\nRevenue by Country (USD):\n", revenue_by_country)

# 4. Monthly sales trend (GBP)
monthly_sales = pd.read_sql("""
    SELECT strftime('%Y-%m', InvoiceDate) as Month, ROUND(SUM(Revenue_GBP), 2) as TotalRevenue_GBP
    FROM sales
    GROUP BY Month
    ORDER BY Month;
""", con=engine)
print("\nMonthly Sales Trend (GBP):\n", monthly_sales.head(10))

# 5. Top 5 customers by total spend (GBP)
top_customers = pd.read_sql("""
    SELECT CustomerID, ROUND(SUM(Revenue_GBP), 2) as TotalSpend_GBP
    FROM sales
    GROUP BY CustomerID
    ORDER BY TotalSpend_GBP DESC
    LIMIT 5;
""", con=engine)
print("\nTop 5 Customers by Spend (GBP):\n", top_customers)
