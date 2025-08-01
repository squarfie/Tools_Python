import pandas as pd

# Load the files
df  = pd.read_excel('spn_sero_data.xlsx')  # Contains AccessionNo, Age, Sex, ARSRL_Org, OrganismCode

df_filter = df[df['Spec_Type']=='bl']

pivot_table = pd.pivot_table(df_filter, index='Serotype', columns='Age_Distribution', aggfunc='size', fill_value='0')



# Create an Excel writer object using openpyxl
output_file = 'pivot_spn_serotype_bl.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Write the pivot table to a new sheet
    pivot_table.to_excel(writer, sheet_name='serotype', index=True)

# Print confirmation
print(f"Excel file '{output_file}' created with counts per age.")
