import pandas as pd

# creates pivot table that counts carba R isolates 

# Load the Excel file into a DataFrame
df1 = pd.read_excel('Kleb_survey_03072025(2).xlsx', engine='openpyxl')  # Use openpyxl for better .xlsx support


# Select pan-susceptible isolates (All IPM, MEM, ETP columns are 'S')
df_filtered = df1[
    ((df1['IPM_ND10_RIS'] == 'R') | (df1['IPM_NM_RIS'] == 'R')) &
    ((df1['MEM_ND10_RIS'] == 'R') | (df1['MEM_NM_RIS'] == 'R')) &
    ((df1['ETP_ND10_RIS'] == 'R') | (df1['ETP_NM_RIS'] == 'R'))
]

# Sort results by 'Laboratory'
df_filtered = df_filtered.sort_values(by=['Laboratory'])


pivot_df = pd.pivot_table(
    df_filtered,
    index='Laboratory',  # Group by Laboratory
    values=['IPM_ND10_RIS', 'IPM_NM_RIS', 'MEM_ND10_RIS', 'MEM_NM_RIS', 'ETP_ND10_RIS', 'ETP_NM_RIS'],  # Columns to check for susceptible isolates
    aggfunc=lambda x: (x == 'R').sum()  # Count how many times 'R' appears in each antibiotic column
)


# Create an Excel writer object using openpyxl
output_file = 'KPN_survey_pivotS.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Write the pivot table to a new sheet
    pivot_df.to_excel(writer, sheet_name='Resistant_Counts', index=True)

# Print confirmation
print(f"Excel file '{output_file}' created with resistant counts per antibiotic.")


