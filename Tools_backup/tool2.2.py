### WORKING ###
import pandas as pd


# Match multiple columns (specified columns must all be matched to output YES)

# Read the Excel file
file_path = 'Tricycle_verification.xlsx'  # replace with your actual file path
df = pd.read_excel(file_path)

# Load the specific sheets into DataFrames
df2 = pd.read_excel(file_path, sheet_name='new_regular_sep23_sep24')  # Sheet with Column 1
df1 = pd.read_excel(file_path, sheet_name='new_data_match')  # Another sheet with Column 2


# Ensure column names have no leading/trailing spaces
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# check if the required columns exist
required_columns = {'FIRST_NAME', 'MID_NAME', 'LAST_NAME'}
if not required_columns.issubset(df1.columns) or not required_columns.issubset(df2.columns):
    raise ValueError("One or more required columns are missing in df1 or df2")

# Create a 'Match' column based on whether the names exist in df2
df1['Match'] = df1[['FIRST_NAME', 'MID_NAME', 'LAST_NAME']].apply(tuple, axis=1).isin(
    df2[['FIRST_NAME', 'MID_NAME', 'LAST_NAME']].apply(tuple, axis=1)
).map({True: 'YES', False: 'NO'})


# Save the updated DataFrame to a new Excel file
output_file = 'tool2_2output.xlsx'
df1.to_excel(output_file, index=False)

print(f"File saved as {output_file}")
