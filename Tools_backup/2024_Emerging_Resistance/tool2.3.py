### WORKING ###
import pandas as pd


# match specific columns from different sheet 


# Load the specific sheets into DataFrames
df2 = pd.read_excel('2024_RefAll_edit.xlsx', sheet_name='Sheet1')  # Another sheet with Column 2
df1 = pd.read_excel('WGS_sequence_edit.xlsx', sheet_name='Sheet1')  # Sheet with Column 1


# Extract relevant columns
column2 = df2['Stock_Number'] 
column1 = df1['AccessionNo'] 

# Create a set of values from Column 2 for fast lookup
column2_set = set(column2)

# Check if each value in Column 1 exists in Column 2 and create the "Match" column
df1['Match'] = column1.apply(lambda x: 'YES' if x in column2_set else 'NO')


# Save the updated DataFrame to a new Excel file
output_file = 'WGS_sequence_match.xlsx'
df1.to_excel(output_file, index=False)

print(f"File saved as {output_file}")
