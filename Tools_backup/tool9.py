import pandas as pd

# Load the Excel file into a DataFrame
df1 = pd.read_excel('FINAL_merged_data.xlsx', engine='openpyxl')  # Use openpyxl for better .xlsx support

# Filter only blood specimens ('bl') and the organisms 'xxx' and 'xsg'
df_filtered = df1[df1['ORGANISM'].isin(['xxx', 'xsg'])]

# Make sure the 'Organism' column is treated as strings

df_filtered['ORGANISM'] = df_filtered['ORGANISM'].fillna('').astype(str)

# Create a pivot table to count occurrences of 'xxx' and 'xsg' for each laboratory
pivot_df = pd.pivot_table(
    df_filtered,
    index='LABORATORY',  # Group by Laboratory
    columns='ORGANISM',  # Separate columns for 'xxx' and 'xsg'
    aggfunc=lambda x: (x.str.lower() == 'xxx').sum() if 'xxx' in x.name else (x.str.lower() == 'xsg').sum(),  # Count occurrences of each organism (case-insensitive)
    fill_value=0  # Fill missing values with 0
)

# Create an Excel writer object using openpyxl
output_file = 'nogrowth.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Write the pivot table to a new sheet
    pivot_df.to_excel(writer, sheet_name='count_nogrowth', index=True)

# Print confirmation
print(f"Excel file '{output_file}' created with counts per antibiotic.")
