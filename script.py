import pandas as pd

# Load the Products Excel file
products_file = './Products.xlsx'  # Update with your Products file path
orders_file = './Orders.xlsx'      # Update with your Orders file path
output_file = './New_Orders_2.xlsx'  # Update with your desired output file path

# Read the Products Excel file
products_df = pd.read_excel(products_file)

# Assuming the Products file has columns 'Product Name' and 'Rate'
# Read the Orders Excel file
orders_df = pd.read_excel(orders_file)

# Merge the dataframes on a common column, e.g., 'Product Name'
merged_df = pd.merge(orders_df, products_df[['Product Name', 'Rate', 'Product ID']], on='Product ID', how='left')

# Save the new dataframe to a new Excel file
merged_df.to_excel(output_file, index=False)

print("New Excel file created successfully.")