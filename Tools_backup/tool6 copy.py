import pandas as pd

# Checks the accessionno column from each files and combine the files where accession number is matched (used for merging of Referred Data )

# Read the Excel files
df1 = pd.read_excel('Emerging_all_query05132025_.xlsx')  # File 1 (sentinel site data)
df2 = pd.read_excel('Emerging_all_query05132025.xlsx')  # File 2 (data to merge)

# Merge the two DataFrames on the 'AccessionNo' column
combined_df = pd.merge(df1, df2, on='AccessionNo', how='left', suffixes=('_df1', '_df2'))

# Save the combined DataFrame to a new Excel file
try:
    combined_df.to_excel('Tool6_Output.xlsx', index=False)
    print("DataFrames successfully combined and saved.")
except Exception as e:
    print(f"Error saving combined DataFrame: {e}")
