import pandas as pd
# creates pivot table that counts carba S isolates based on column IPM, MEM, ETP (use only interpretations / combine disk & mic)

# Load the Excel file into a DataFrame
df1 = pd.read_excel('tri_tool9_3_Output1.xlsx', engine='openpyxl')  # Use openpyxl for better .xlsx support

# Filter only blood specimens ('bl')
df_filtered = df1[(df1['Specimen_type'].isin(['bl', 'sf'])) & (df1['AGE_GRP'] == 'a')]

# Select only susceptible isolates ('R') for the relevant antibiotics
df_filtered = df_filtered[
    (df_filtered['IPM'] == 'R') &
    (df_filtered['MEM'] == 'R') &
    (df_filtered['ETP'] == 'R') 
]

# Create a pivot table to count occurrences of 'R' for each antibiotic per laboratory
pivot_df = pd.pivot_table(
    df_filtered,
    index='Laboratory',  # Group by Laboratory
    values=['IPM','MEM','ETP',],  # Columns to check for susceptible isolates
    aggfunc=lambda x: (x == 'R').sum()  # Count how many times 'R' appears in each antibiotic column
)

# Create an Excel writer object using openpyxl
output_file = 'carbaR_neo.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Write the pivot table to a new sheet
    pivot_df.to_excel(writer, sheet_name='kpn_Counts', index=True)

# Print confirmation
print(f"Excel file '{output_file}' created with susceptible counts per antibiotic.")
