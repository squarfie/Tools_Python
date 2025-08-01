import pandas as pd

# Load the files
ref_df = pd.read_excel('ref_data.xlsx')  # Contains AccessionNo, Age, Sex, ARSRL_Org, OrganismCode
sero_df = pd.read_excel('spn_serotype_results.xlsx')  # Contains 'genome' column

# Perform left join: match ref_df.AccessionNo to sero_df.genome
merged_df = pd.merge(
    sero_df, 
    ref_df[['AccessionNo', 'Age', 'Sex', 'ARSRL_Org', 'OrganismCode', 'Spec_Type', 'Service_Type','Ward' ]], 
    left_on='Identifier', 
    right_on='AccessionNo', 
    how='left'
)

# Save the updated serotype_sstr file with appended columns
try:
    merged_df.to_excel('spn_sero.xlsx', index=False)
    print("File successfully updated and saved as 'serotype.xlsx'.")
except Exception as e:
    print(f"Error saving updated file: {e}")
