import pandas as pd
data = pd.read_csv("sales.csv")
total_sales = data.groupby("Product")["Amount"].sum()
print("Total Sales by Product:")
print(total_sales)
