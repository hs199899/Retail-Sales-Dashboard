# Walmart Sales Analysis

This project analyzes Walmart sales data from 2014 to 2017 using both Excel and Python to uncover sales trends, regional performance, discount impact, and customer insights.

---

## Project Overview

The goal is to clean, transform, and explore Walmart sales data to extract meaningful business insights. The analysis includes monthly sales trends, profit comparisons by region, the effect of discounts on profit, and identification of top customers.

---

## What’s Included

### Excel Analysis
- Data cleaning: removing blank rows, fixing date formats
- Pivot tables for monthly sales, regional sales, and profit trends
- Interactive charts and dashboards with slicers for dynamic filtering

### Python Analysis
- Data loading and cleaning using Pandas
- Date parsing and creating new columns like Month-Year and Year
- Grouping and aggregation of sales, profits, and discounts
- Correlation analysis between discount and profit
- Visualizations using Matplotlib:  
  - Monthly sales trends  
  - Scatter plot of Discount vs Profit  
  - Bar chart of Top 10 Customers by Sales

---

## How to Run

1. Ensure the Excel file `data.xlsx` is located in the `/data` folder.
2. Install required Python packages:

   pip install pandas matplotlib

python data_analysis.py

/data/           ← Excel dataset files  
/scripts/        ← Python scripts for analysis  
/charts/         ← Saved visualizations (optional) 
