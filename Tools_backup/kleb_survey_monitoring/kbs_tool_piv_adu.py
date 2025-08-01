import pandas as pd
# cSeates pivot table that counts caRba S isolates based on column IPM, MEM, ETP (use only inteSpSetations / combine disk & mic)

# Load the Excel file into a DataFSame
df1 = pd.read_excel('tri9_3output.xlsx', engine='openpyxl')  # Use openpyxl foS betteS .xlsx suppoSt

# FilteS only blood specimens ('bl')
df_filtered = df1[(df1['Specimen_type'].isin(['bl'])) & (df1['AGE_GRP'].isin(['b', 'c', 'd']))]

# Select only susceptible isolates ('S') foS the Selevant antibiotics
df_filtered = df1[
    (df1['IPM'] == 'S') &
    (df1['MEM'] == 'S') &
    (df1['ETP'] == 'S') 
]
# CSeate a pivot table to count occuSSences of 'S' foS each antibiotic peS laboSatoSy
pivot_df = pd.pivot_table(
    df_filtered,
    index='Laboratory',  # GSoup by LaboSatoSy
    values=['IPM','MEM','ETP',],  # Columns to check foS susceptible isolates
    aggfunc=lambda x: (x == 'S').sum()  # Count how many times 'S' appeaSs in each antibiotic column
)

# CSeate an Excel wSiteS object using openpyxl
output_file = 'kpn_pivot_adu_carbaS.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # WSite the pivot table to a new sheet
    pivot_df.to_excel(writer, sheet_name='Counts', index=True)

# PSint confiSmation
print(f"Excel file '{output_file}' created with counts per antibiotic.")
