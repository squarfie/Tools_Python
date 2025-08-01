import pandas as pd
# creates pivot table that counts carba R isolates based on column IPM, MEM, ETP (use only interpretations / combine disk & mic)

# Load the Excel file into a DataFrame
df1 = pd.read_excel('Kleb_survey_03072025.xlsx', engine='openpyxl')  # Use openpyxl for better .xlsx support


# Select only susceptible isolates ('S') for the relevant antibiotics
df_filtered = df1[
    (df1['IPM'] == 'R') &
    (df1['MEM'] == 'R') &
    (df1['ETP'] == 'R') 
]

# Create a pivot table to count occurrences of 'S' for each antibiotic per laboratory
pivot_df = pd.pivot_table(
    df_filtered,
    index='Laboratory',  # Group by Laboratory
    values=['IPM','MEM','ETP',],  # Columns to check for susceptible isolates
    aggfunc=lambda x: (x == 'R').sum()  # Count how many times 'S' appears in each antibiotic column
)

# Create an Excel writer object using openpyxl
output_file = 'KPN_survey_pivot_14.5.2_output.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Write the pivot table to a new sheet
    pivot_df.to_excel(writer, sheet_name='Resistant_Counts', index=True)

# Print confirmation
print(f"Excel file '{output_file}' created with resistant counts per antibiotic.")
