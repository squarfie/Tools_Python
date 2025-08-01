import pandas as pd

# creates a list of carba r isolates from bl and sf (for kleb survey)

# Load the Excel file into a DataFrame
df1 = pd.read_excel('Kleb_survey_03072025(2).xlsx', engine='openpyxl') 


df_filtered = df1[(df1['Specimen_type'].isin(['bl', 'sf']))]

# Select pan-susceptible isolates (All IPM, MEM, ETP columns are 'S')
df_filtered = df_filtered[
    ((df_filtered['IPM_ND10_RIS'] == 'R') | (df_filtered['IPM_NM_RIS'] == 'R')) &
    ((df_filtered['MEM_ND10_RIS'] == 'R') | (df_filtered['MEM_NM_RIS'] == 'R')) &
    ((df_filtered['ETP_ND10_RIS'] == 'R') | (df_filtered['ETP_NM_RIS'] == 'R'))
]

# Sort results by 'Laboratory'
df_filtered = df_filtered.sort_values(by=['Laboratory'])

# Create an Excel writer object using openpyxl
output_file = 'KPN_survey_list_allCarbaR.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Loop through each unique laboratory and create a separate sheet
    for lab in df_filtered['Laboratory'].unique():
        df_lab = df_filtered[df_filtered['Laboratory'] == lab]  # Get data for that lab
        df_lab.to_excel(writer, sheet_name=str(lab), index=False)  # Write to separate sheet

# Print confirmation
print(f"Excel file '{output_file}' created with separate sheets for each laboratory.")
