import pandas as pd
# Filter isolates where isolates are resistant to either one of carbapenem (IPM, MEM, and ETP ) antibiotics and creates a list per sentinel site in each sheets 


# Load the Excel file into a DataFrame
df1 = pd.read_excel('Kleb_survey.xlsx')  # Adjust the file path if needed

# Filter isolates where IPM, MEM, and ETP that may be resistant to any of the antibiotics
df_filtered = df1[(df1['IPM_ND10_RIS'] == 'R') | (df1['IPM_NM_RIS']== 'R') | (df1['MEM_ND10_RIS'] == 'R') | (df1['MEM_NM_RIS'] == 'R') | (df1['ETP_ND10_RIS'] == 'R') | (df1['ETP_NM_RIS'] == 'R')]

# Group by Laboratory and count the number of resistant isolates per site
df_filtered = df_filtered.sort_values(by=['Laboratory'])

# # Save the result to a new Excel file (optional)
# df_filtered.to_excel('KPN_resistances_summary(CARBA).xlsx', index=False)

# # Print the result
# print(df_filtered.to_string(index=False))

 #Create an Excel writer object
output_file = 'KPN_resistant_isolates_by_lab.xlsx'
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    # Loop through each unique laboratory and create a separate sheet
    for lab in df_filtered['Laboratory'].unique():
        df_lab = df_filtered[df_filtered['Laboratory'] == lab]  # Get data for that lab
        df_lab.to_excel(writer, sheet_name=lab, index=False)  # Write to separate sheet

# Print confirmation
print(f"Excel file '{output_file}' created with separate sheets for each laboratory.")
