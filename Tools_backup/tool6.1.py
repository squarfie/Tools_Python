import pandas as pd

#Merge based on accession no.

# Load the Excel files
df1 = pd.read_excel('Emerging_List.xlsx')
df2 = pd.read_excel('Emerging_all_query.xlsx')

# Set index to AccessionNo
df1.set_index('AccessionNo', inplace=True)
df2.set_index('AccessionNo', inplace=True)

# Ensure only rows with unique AccessionNo are processed
df1 = df1[~df1.index.duplicated(keep='first')]
df2 = df2[~df2.index.duplicated(keep='first')]

# Start with df1 copy
combined_df = df1.copy()

# Loop through df2
for acc_no, row2 in df2.iterrows():
    if acc_no in df1.index:
        row1 = df1.loc[acc_no]

        # Only compare shared columns
        common_cols = df1.columns.intersection(df2.columns)
        row1_common = row1[common_cols]
        row2_common = row2[common_cols]

        # Compute difference with NaN-aware comparison
        differences = (row1_common != row2_common) & ~(row1_common.isnull() & row2_common.isnull())

        # Check if any difference exists and cast to boolean
        if differences.any().item():
            combined_df.loc[acc_no, common_cols[differences]] = row2_common[differences]
    else:
        # Row does not exist, so add it
        combined_df.loc[acc_no] = row2

# Reset index and save
combined_df.reset_index(inplace=True)
combined_df.to_excel('Tool6_Output(2).xlsx', index=False)

print("✅ Merge complete. Differences updated or new rows added.")
