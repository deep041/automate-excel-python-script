import pandas as pd

# Load the Products Excel file
products_file = './Products.xlsx'  # Update with your Products file path
orders_file = './Orders.xlsx'      # Update with your Orders file path
output_file = './New_Orders.xlsx'  # Update with your desired output file path

# Read the Products Excel file
products_df = pd.read_excel(products_file)

# Assuming the Products file has columns 'Product Name' and 'Rate'
# Read the Orders Excel file
orders_df = pd.read_excel(orders_file)


# Merge the dataframes on a common column, e.g., 'Product Name'
merged_df = pd.merge(orders_df, products_df[['Product Name', 'Rate', 'Product ID']], on = 'Product ID', how = 'left')

# Calculate 5% GST and add it as a new column
merged_df['GST'] = merged_df['Rate'] * 0.05

# Calculate total price including GST and add it as a new column
merged_df['Total Price'] = merged_df['Rate'] + merged_df['GST']

# Add a column for quantity if it exists in the orders dataframe
if 'Quantity' in orders_df.columns:
    merged_df['Total Amount'] = merged_df['Total Price'] * orders_df['Quantity']
else:
    merged_df['Total Amount'] = merged_df['Total Price']  # Default to Total Price if Quantity is not available

# Optionally, add a column for order date if it exists in the orders dataframe
if 'Order Date' in orders_df.columns:
    merged_df['Order Date'] = orders_df['Order Date']


# Save the new dataframe to a new Excel file
merged_df.to_excel(output_file, index = False)

print("New Excel file created successfully.")