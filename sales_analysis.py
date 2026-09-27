import pandas as pd

# Load the sales dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate sales for each row
df["Sales"] = df["Quantity"] * df["Unit_Price"]

print("===== SALES DATA ANALYSIS =====\n")

print("First 5 records:")
print(df.head())

print("\nTotal Sales:")
print(f"₹{df['Sales'].sum():,.0f}")

print("\nTotal Quantity Sold:")
print(df["Quantity"].sum())

print("\nAverage Order Value:")
print(f"₹{df['Sales'].mean():,.2f}")

# Sales by product
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Product:")
print(product_sales)

# Sales by city
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)

print("\nSales by City:")
print(city_sales)

# Sales by category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Category:")
print(category_sales)

# Highest-selling product
top_product = product_sales.idxmax()
print(f"\nHighest Revenue Product: {top_product}")

# Highest-revenue city
top_city = city_sales.idxmax()
print(f"Highest Revenue City: {top_city}")

# Monthly sales
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Save summary files
product_sales.to_csv("product_sales_summary.csv")
city_sales.to_csv("city_sales_summary.csv")
monthly_sales.to_csv("monthly_sales_summary.csv")

print("\nSummary CSV files created successfully.")
