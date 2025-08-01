import pandas as pd
# creates pivot table that counts carba S isolates based on column IPM, MEM, ETP (use only interpretations / combine disk & mic)

# Load the Excel file into a DataFrame
df1 = pd.read_excel('tri9_3output.xlsx', engine='openpyxl')  # Use openpyxl for better .xlsx support

# Filter only blood specimens ('bl')
df_filtered = df1[(df1['Specimen_type'].isin(['bl', 'sf'])) & (df1['AGE_GRP'] == 'a')]

# Select only susceptible isolates ('S') for the relevant antibiotics
df_filtered = df_filtered[
    (df_filtered['IPM'] == 'S') &
    (df_filtered['MEM'] == 'S') &
    (df_filtered['ETP'] == 'S') 
]

# Create a pivot table to count occurrences of 'S' for each antibiotic per laboratory
pivot_df = pd.pivot_table(
    df_filtered,
    index='Laboratory',  # Group by Laboratory
    values=['IPM','MEM','ETP',],  # Columns to check for susceptible isolates
    aggfunc=lambda x: (x == 'S').sum()  # Count how many times 'S' appears in each antibiotic column
)

# Create an Excel writer object using openpyxl
output_file = 'kpn_survey_pivot_neo_carbaS.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Write the pivot table to a new sheet
    pivot_df.to_excel(writer, sheet_name='kpn_Counts', index=True)

# Print confirmation
print(f"Excel file '{output_file}' created with counts per antibiotic.")
