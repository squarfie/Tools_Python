### WORKING ###
import pandas as pd


# match specific columns from different sheet

# Read the Excel file
file_path = 'c:\\TESTINGS\\files\\MAR-ABA.xlsx'  # replace with your actual file path
df = pd.read_excel(file_path)

# Load the specific sheets into DataFrames
df1 = pd.read_excel(file_path, sheet_name='regular_data')  # Sheet with Column 1
df2 = pd.read_excel(file_path, sheet_name='MAR')  # Another sheet with Column 3

# Extract relevant columns
column1 = df1.iloc[:, 0]  # Column 1 from regular_data
column3 = df2.iloc[:, 2]  # Column 3 from sheet2

# Create a set of values from Column 3 for fast lookup
column3_set = set(column3)

# Check if each value in Column 1 exists in Column 3 and create the "Match" column
df1['Match'] = column1.apply(lambda x: 'YES' if x in column3_set else '')


#or use this if you prefer not to use lambda
# Define a regular function to check if a value is in column3_set
# def check_match(value):
#     if value in column3_set:
#         return 'YES'
#     else:
#         return ''

# # Use the function instead of lambda with apply
# df1['Match'] = column1.apply(check_match)


# Save the updated DataFrame to a new Excel file
output_file = 'c:\\TESTINGS\\output\\output_file.xlsx'
df1.to_excel(output_file, index=False)

print(f"File saved as {output_file}")
