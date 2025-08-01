### WORKING ###
import pandas as pd


# match specific columns from different sheet 


# Load the specific sheets into DataFrames
df2 = pd.read_excel('WGS_sequence_edit', sheet_name='Sheet1')  # Another sheet with Column 2
df1 = pd.read_excel('2024_em_aba', sheet_name='aba_all')  # Sheet with Column 1


# Extract relevant columns
column1 = df1['PATIENT_ID'] 
column2 = df2['Id_no'] 

# Create a set of values from Column 2 for fast lookup
column2_set = set(column2)

# Check if each value in Column 1 exists in Column 2 and create the "Match" column
df1['Matched'] = column1.apply(lambda x: 'YES' if x in column2_set else 'NO')


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
output_file = 'tool2.1_aba.xlsx'
df1.to_excel(output_file, index=False)

print(f"File saved as {output_file}")
