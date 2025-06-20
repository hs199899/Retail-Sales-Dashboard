import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data.xlsx")

# # To check null
# summOfNull = (df.isnull().sum())
# print(summOfNull)
# # To Check Duplicate Rows

# duplicate = df.duplicated().sum()
# print(duplicate)

# Converting Ship Date column from text to Date

df['ShipDate']=pd.to_datetime(df['ShipDate'], errors='coerce')
df['OrderDate']=pd.to_datetime(df['OrderDate'], errors='coerce')

# Getting Year and Month from Date Columns for month-year analysis

df['month-year'] = df['OrderDate'].dt.to_period('M')
df['month']=df['OrderDate'].dt.month_name()
df['year']=df['OrderDate'].dt.year

# Analyzing the Data by month-year Sale 
monthly_year_sales = df.groupby('Month-Year')['Sales'].sum()

monthly_year_sales=monthly_year_sales.sort_index()
print(monthly_year_sales)
#plotting the Data
plt.plot(monthly_year_sales.index.astype(str), monthly_year_sales.values, marker='o', color='Teal')
plt.title('Monthly Sales Over the Years')
plt.xlabel('Month-Year')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()

# Analyzing the Top 5 Products by Sales

top_5_products = df.groupby('ProductName')['Sales'].sum()
top_5_products = top_5_products.sort_values(ascending=False)
print(top_5_products.head(5))
#print(top_5_products.nlargest(5)) Same Function as above line 34

#Analyze the Sales by Region

region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales.sort_values(ascending=False))

#Analyze the Profit by Region

regional_profit = df.groupby('Region')['Profit'].sum()
print(regional_profit.sort_values(ascending=False))

#Analyzing correlation between discount and profit
df['Discount'] = df['Discount'].astype(float)
corr = df['Discount'].corr(df['Profit'])
plt.scatter(df['Discount'], df['Profit'], alpha=0.5, color='darkred', edgecolors='w')
plt.title("Impact of Discount on Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.grid(True)
plt.tight_layout()
plt.show()

#Top 10 Customers By Sale

customers = df.groupby('CustomerName')['Sales'].sum()
print(customers.nlargest(10))

plt.figure(figsize=(10, 6))
plt.bar(customers.nlargest(10).index, customers.nlargest(10).values)
plt.title("Top 10 Customers by Sales")
plt.ylabel("Total Sales")
plt.xlabel("Customer Name")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')
plt.show()