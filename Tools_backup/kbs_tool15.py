import pandas as pd

# Load the Excel file into a DataFrame
df1 = pd.read_excel('KPN_2024_ALL_02212025.xlsx', engine='openpyxl')

# Select fully susceptible isolates (All IPM, MEM, and ETP columns must be 'S')
df_filtered = df1[
    (df1[['IPM_ND10_RIS', 'IPM_NM_RIS']].eq('S').all(axis=1)) & 
    (df1[['MEM_ND10_RIS', 'MEM_NM_RIS']].eq('S').all(axis=1)) & 
    (df1[['ETP_ND10_RIS', 'ETP_NM_RIS']].eq('S').all(axis=1))
]

# Sort results by 'Laboratory'
df_filtered = df_filtered.sort_values(by=['Laboratory'])

# Create pivot table: Count of fully susceptible isolates per Laboratory
pivot_df = df_filtered.pivot_table(index='Laboratory', aggfunc='size', fill_value=0)

# Convert Series to DataFrame and rename the column
pivot_df = pivot_df.to_frame(name='Fully_Susceptible_Count')

# Create an Excel writer object
output_file = 'KPN_survey_pivotS.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    pivot_df.to_excel(writer, sheet_name='Susceptible_Counts', index=True)

# Print confirmation
print(f"Excel file '{output_file}' created with fully susceptible isolate counts per laboratory.")
