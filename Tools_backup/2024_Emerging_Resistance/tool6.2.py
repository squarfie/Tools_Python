import pandas as pd

#Only keeps rows from df1
#Adds or updates PATIENT_ID, FIRST_NAME, and LAST_NAME from df2
#Does NOT add new rows from df2 that aren't in df1

# Load the Excel files
df1 = pd.read_excel('2024Ref_all.xlsx')
df2 = pd.read_excel('WGS_sequence_edit.xlsx')

# Set index to AccessionNo
df1.set_index('Stock_Number', inplace=True)
df2.set_index('AccessionNo', inplace=True)

# Keep only rows with unique AccessionNo
df1 = df1[~df1.index.duplicated(keep='first')]
df2 = df2[~df2.index.duplicated(keep='first')]

# Start with a copy of df1
combined_df = df1.copy()

# Columns to update
columns_to_update = ['WGS']

# Only update rows where AccessionNo exists in both
matching_indices = df1.index.intersection(df2.index)

# Add or update selected columns for matching AccessionNo
for col in columns_to_update:
    if col in df2.columns:
        combined_df.loc[matching_indices, col] = df2.loc[matching_indices, col]

# Reset index and save
combined_df.reset_index(inplace=True)
combined_df.to_excel('2024_RefAll_edit.xlsx', index=False)

print("✅ Merge complete. PATIENT_ID, FIRST_NAME, and LAST_NAME updated for matched AccessionNo only.")
