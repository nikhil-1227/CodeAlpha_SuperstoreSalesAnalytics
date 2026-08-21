"""
CodeAlpha - Data Analytics Internship
Task 2: Exploratory Data Analysis (EDA)
Dataset: Sample - Superstore.csv (Kaggle)

Goals:
- Understand data structure (variables, types)
- Clean and check for data quality issues
- Identify trends and patterns
- Answer meaningful business questions using stats + visuals
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

print("=" * 60)
print("STEP 1: BASIC INFO")
print("=" * 60)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns\n")
print("Column names and data types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

# ---------------------------------------------------------
# 2. DATA QUALITY CHECK
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 2: DATA QUALITY CHECK")
print("=" * 60)

print("\nMissing values per column:")
print(df.isnull().sum())

print(f"\nDuplicate rows: {df.duplicated().sum()}")

# ---------------------------------------------------------
# 3. DATA CLEANING
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 3: DATA CLEANING")
print("=" * 60)

# Convert date columns to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Drop exact duplicate rows (if any)
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print(f"Removed {before - after} duplicate rows.")

# Add helpful derived columns
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month_name()
df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

print("Cleaning complete. Added 'Order Year', 'Order Month', 'Shipping Days' columns.")

# ---------------------------------------------------------
# 4. DESCRIPTIVE STATISTICS
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 4: DESCRIPTIVE STATISTICS")
print("=" * 60)
print(df[["Sales", "Profit", "Discount", "Quantity"]].describe())

# ---------------------------------------------------------
# 5. KEY BUSINESS QUESTIONS
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 5: KEY INSIGHTS")
print("=" * 60)

# Q1: Which category makes the most profit?
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by Category:")
print(category_profit)

# Q2: Which sub-category is losing money?
subcat_profit = df.groupby("Sub-Category")["Profit"].sum().sort_values()
print("\nTop 5 loss-making Sub-Categories:")
print(subcat_profit.head())

# Q3: Which region performs best?
region_sales = df.groupby("Region")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False)
print("\nSales & Profit by Region:")
print(region_sales)

# Q4: Does discount hurt profit?
discount_profit_corr = df["Discount"].corr(df["Profit"])
print(f"\nCorrelation between Discount and Profit: {discount_profit_corr:.3f}")

# Q5: Top 10 customers by sales
top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Customers by Sales:")
print(top_customers)

# ---------------------------------------------------------
# 6. VISUALIZATIONS
# ---------------------------------------------------------
sns.set_style("whitegrid")

# Plot 1: Profit by Category
plt.figure(figsize=(8, 5))
sns.barplot(x=category_profit.values, y=category_profit.index, palette="viridis")
plt.title("Total Profit by Category")
plt.xlabel("Profit ($)")
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.close()

# Plot 2: Sales by Region
plt.figure(figsize=(8, 5))
sns.barplot(x=region_sales.index, y=region_sales["Sales"], palette="magma")
plt.title("Total Sales by Region")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.close()

# Plot 3: Discount vs Profit scatter
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.4)
plt.title("Discount vs Profit")
plt.tight_layout()
plt.savefig("discount_vs_profit.png")
plt.close()

# Plot 4: Monthly sales trend
monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
plt.figure(figsize=(12, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales ($)")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.close()

print("\n" + "=" * 60)
print("Saved 4 charts: profit_by_category.png, sales_by_region.png,")
print("discount_vs_profit.png, monthly_sales_trend.png")
print("=" * 60)

# ---------------------------------------------------------
# 7. EXPORT CLEANED DATA
# ---------------------------------------------------------
df.to_csv("superstore_cleaned.csv", index=False)
print("\nCleaned dataset saved as 'superstore_cleaned.csv'")
print("\nEDA COMPLETE.")