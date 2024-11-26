# Distinguished_migration_patterns
# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data_path = "../data/sales_data.csv"
sales_data = pd.read_csv(data_path)

# Explore the dataset
print("Dataset Overview:")
print(sales_data.head())
print("\nDataset Info:")
print(sales_data.info())

# Handle missing values
sales_data.fillna(0, inplace=True)  # Example: Replace NaN with 0

# Basic statistics
summary = sales_data.describe()
summary.to_csv("../output/summary.csv", index=True)

# Analysis: Sales trends over time
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_trends = sales_data.groupby(sales_data['Date'].dt.to_period('M'))['Sales'].sum()

# Plot sales trends
plt.figure(figsize=(10, 6))
sales_trends.plot(kind='line', marker='o', color='b')
plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid()
plt.savefig("../visuals/sales_trends.png")
plt.show()

# Analysis: Top-performing categories
top_categories = sales_data.groupby('Category')['Sales'].sum().sort_values(ascending=False)

# Plot top-performing categories
plt.figure(figsize=(8, 5))
top_categories.plot(kind='bar', color='orange')
plt.title("Top Performing Categories")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visuals/top_categories.png")
plt.show()

# Analysis: Correlation between variables
correlation_matrix = sales_data.corr()

# Plot heatmap for correlations
plt.figure(figsize=(8, 6))
plt.matshow(correlation_matrix, fignum=1, cmap='coolwarm')
plt.colorbar()
plt.title("Correlation Heatmap", pad=20)
plt.savefig("../visuals/correlation_heatmap.png")
plt.show()

print("Analysis complete! Visualizations saved in '../visuals/' folder.")

