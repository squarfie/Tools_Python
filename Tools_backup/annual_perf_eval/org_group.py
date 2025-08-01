import pandas as pd

file1_path = input("Enter the path of the first Excel file (with WHONET_ORG_CODE): ")
file2_path = input("Enter the path of the second CSV file (with organism column): ")

try:
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_csv(file2_path, low_memory=False)
except Exception as e:
    print("Error reading files:", e)
    exit()

required_cols_file1 = ['WHONET_ORG_CODE', 'GENUS_GROUP', 'GENUS_CODE', 'SPECIES_GROUP', 'FAMILY_CODE']
if not all(col in df1.columns for col in required_cols_file1):
    print(f"File 1 must contain the following columns: {required_cols_file1}")
    exit()

if 'organism' not in df2.columns:
    print("File 2 must contain a column named 'organism'")
    exit()

# Drop duplicates to ensure WHONET_ORG_CODE is unique
df1_unique = df1.drop_duplicates(subset='WHONET_ORG_CODE')

# Create mapping
org_info = df1_unique.set_index('WHONET_ORG_CODE')[['GENUS_GROUP', 'GENUS_CODE', 'SPECIES_GROUP', 'FAMILY_CODE']]

# Perform the mapping
df2['GENUS_GROUP'] = df2['organism'].map(org_info['GENUS_GROUP'])
df2['GENUS_CODE'] = df2['organism'].map(org_info['GENUS_CODE'])
df2['SPECIES_GROUP'] = df2['organism'].map(org_info['SPECIES_GROUP'])
df2['fAMILY_CODE'] = df2['organism'].map(org_info['FAMILY_CODE'])

# Output
output_path = "merged_output.csv"
df2.to_csv(output_path, index=False)
print(f"Merged data saved to {output_path}")
