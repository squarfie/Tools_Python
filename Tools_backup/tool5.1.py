import pandas as pd
import openpyxl
import csv
# a code to check for the unique ward, ward type and department for each sentinel site, and create an excel file that 
# puts the code of each sentinel site as sheet name
file_path = 'C:\\TESTINGS\\Tools_backup\\df_2024.csv'
output_path = 'c:\\TESTINGS\\output\\tool5_output.xlsx'


# Load the Excel file
try:
    df = pd.read_csv(file_path)
except Exception as e:
    print(f"Error reading input file: {e}")
    exit()

# Write data to separate sheets
try:
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        labs = df.groupby('laboratory')  # Group by sentinel site
        for site, lab in labs:
            # delete the duplicates in each columns
            unique_data = lab[['ward', 'institut', 'department', 'ward_type']].drop_duplicates()
            unique_data = unique_data.sort_values(by='ward') # sort by ward
            # Write to the Excel sheet
            unique_data.to_excel(writer, index=False, sheet_name=site)
    print(f"Data successfully saved to {output_path}")
except Exception as e:
    print(f"Error writing Excel file: {e}")

