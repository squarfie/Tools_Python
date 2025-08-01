import pandas as pd

# Input CSV path
file1_path = input("Enter path to the first CSV file: ")

df1 = pd.read_csv(file1_path, low_memory=False)

# Output path
output_path = 'output_by_lab_and_month.xlsx'

# Define antibiotic panels per organism prefix
panels = {
    'eco': ['AMP', 'AMC', 'CTX', 'CAZ', 'CRO', 'FEP', 'FOX', 'CXM', 'IPM', 'MEM', 'ETP', 'GEN', 'AMK', 'KAN', 'CIP', 'NAL', 'NOR', 'OFX', 'LVX', 'TET', 'DOX', 'SXT', 'CHL', 'FOS', 'NIT', 'AZM'],
    'kpn': ['AMP', 'AMC', 'CTX', 'CAZ', 'CRO', 'FEP', 'FOX', 'CXM', 'IPM', 'MEM', 'ETP', 'GEN', 'AMK', 'KAN', 'CIP', 'NAL', 'NOR', 'OFX', 'LVX', 'TET', 'DOX', 'SXT', 'CHL', 'FOS', 'NIT', 'AZM'],
    'sal': ['AMP', 'AMC', 'CTX', 'CAZ', 'CRO', 'IPM', 'GEN', 'KAN', 'CIP', 'OFX', 'LVX', 'TET', 'SXT', 'CHL', 'AZM'],
    'shi': ['AMP', 'AMC', 'CTX', 'CAZ', 'CRO', 'IPM', 'GEN', 'KAN', 'CIP', 'OFX', 'LVX', 'TET', 'SXT', 'CHL', 'AZM'],
    'vic': ['AMP', 'AMC', 'CTX', 'CAZ', 'CRO', 'IPM', 'GEN', 'KAN', 'CIP', 'OFX', 'LVX', 'TET', 'SXT', 'CHL', 'AZM'],
    'aba': ['IPM', 'MEM', 'GEN', 'AMK', 'KAN', 'CIP', 'OFX', 'LVX', 'TET', 'SXT', 'CHL', 'FEP', 'CAZ', 'COL', 'TGC'],
    'pae': ['IPM', 'MEM', 'GEN', 'AMK', 'CIP', 'OFX', 'LVX', 'CAZ', 'FEP', 'PIP', 'TZP', 'COL', 'TGC'],
    'efa': ['AMP', 'GEN', 'CIP', 'LVX', 'TET', 'VAN', 'LZD'],
    'efm': ['AMP', 'GEN', 'CIP', 'LVX', 'TET', 'VAN', 'LZD'],
    'ent': ['AMP', 'GEN', 'CIP', 'LVX', 'TET', 'VAN', 'LZD'],
    'hpi': ['AMP', 'AMC', 'CTX', 'CAZ', 'CRO', 'IPM', 'GEN', 'KAN', 'CIP', 'OFX', 'LVX', 'TET', 'SXT', 'CHL', 'AZM'],
    'hin': ['AMP', 'AMC', 'CTX', 'CAZ', 'CRO', 'IPM', 'GEN', 'KAN', 'CIP', 'OFX', 'LVX', 'TET', 'SXT', 'CHL', 'AZM'],
    'ngo': ['CRO', 'PEN', 'CIP', 'AZM', 'SPT', 'TET'],
    'pce': ['AMP', 'GEN', 'CIP', 'LVX', 'TET', 'VAN', 'LZD'],
    'pma': ['AMP', 'GEN', 'CIP', 'LVX', 'TET', 'VAN', 'LZD'],
    'nme': ['PEN', 'RIF', 'CRO', 'CIP', 'CHL'],
    'sau': ['PEN', 'OXA', 'FOX', 'GEN', 'CIP', 'LVX', 'TET', 'CLI', 'ERY', 'SXT', 'VAN', 'LZD', 'DAP'],
    'spn': ['PEN', 'CRO', 'CTX', 'GEN', 'CIP', 'LVX', 'ERY', 'TET', 'VAN', 'LZD', 'CLI'],
    'str': ['PEN', 'CRO', 'CTX', 'GEN', 'CIP', 'LVX', 'ERY', 'TET', 'VAN', 'LZD', 'CLI'],
    'svi': ['PEN', 'CRO', 'CTX', 'GEN', 'CIP', 'LVX', 'ERY', 'TET', 'VAN', 'LZD', 'CLI']
}

# Prep the DataFrame
df1['spec_date'] = pd.to_datetime(df1['spec_date'], errors='coerce')
df1['Month'] = df1['spec_date'].dt.month
df1['Prefix'] = df1['organism'].str.lower().str[:3]

results = []

# Loop through labs and months
for lab in df1['laboratory'].dropna().unique():
    lab_df = df1[df1['laboratory'] == lab]

    for month in lab_df['Month'].dropna().unique():
        month_df = lab_df[lab_df['Month'] == month].copy()
        if month_df.empty:
            continue

        # Loop by prefix/organism group
        for prefix, abx_list in panels.items():
            sub_df = month_df[month_df['Prefix'] == prefix]
            if sub_df.empty:
                continue

            # Get the correct columns to look for, even if all values are NaN
            abx_cols = [f"{abx.lower()}_nm" for abx in abx_list]
            existing_abx_cols = [col for col in abx_cols if col in sub_df.columns]

            if not existing_abx_cols:
                continue

            # Total tests possible = num_rows × num_abx_expected
            total_possible = sub_df.shape[0] * len(abx_list)

            # Actual tested (non-NA)
            tested_count = sub_df[existing_abx_cols].notna().sum().sum()

            completeness = (tested_count / total_possible) * 100 if total_possible else 0

            results.append({
                'Lab': lab,
                'Month': int(month),
                'Prefix': prefix,
                'Isolates': sub_df.shape[0],
                'Total_Expected_Tests': total_possible,
                'Tested': tested_count,
                'Completeness (%)': round(completeness, 2)
            })

# Final DataFrame
results_df = pd.DataFrame(results)
results_df.to_excel(output_path, index=False)
print(f"Done. Output saved to {output_path}")
