import pandas as pd

#a code that checks whether columns of df1 exists in df2 if not merge the dataframes while deleting the common columns and retaining only columns with values based on PATIENT_ID
# Read the Excel files
df1 = pd.read_excel('tri-rmc-final-00122-2.xlsx')  # File 1 (sentinel site data)
df2 = pd.read_excel('T9_tri3_Output1.xlsx')  # File 2 (data to merge)

# Identify matching columns
common_columns = set(df1.columns).intersection(df2.columns)  #.intesection is used to find common elements between two or more sets.

# Ensure 'patient_ID' is in both DataFrames
if 'PATIENT_ID' not in df1.columns or 'PATIENT_ID' not in df2.columns:
    raise ValueError("'PATIENT_ID' column is required in both DataFrames.")

# Merge the DataFrames based on 'patient_ID'
merged_df = pd.merge(df1, df2, on='PATIENT_ID', how='inner', suffixes=('_df1', '_df2'))  #inner join selects only the rows that have matching values in the key column(s) from both DataFrames.

# Retain values from non-blank fields for overlapping columns
for col in common_columns - {'PATIENT_ID'}:  # Exclude 'patient_ID' from processing
    merged_df[col] = merged_df[f"{col}_df1"].combine_first(merged_df[f"{col}_df2"])

    # Drop temporary columns
    merged_df.drop(columns=[f"{col}_df1", f"{col}_df2"], inplace=True) #inplace=True to modify the original object directly, instead of returning a modified copy

# Save the resulting DataFrame
merged_df.to_excel('tool7_output.xlsx', index=False)

print("Merged data saved to 'tool7_output.xlsx'.")
