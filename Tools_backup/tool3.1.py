# import pandas as pd
# import numpy as np

# # Read the Excel file (2 sheets only)
# file_path = 'NGO_referred.xlsx'  # replace with your actual file path
# df = pd.read_excel(file_path)


# # Load the specific sheets into DataFrames
# df2 = pd.read_excel(file_path, sheet_name='com_1')  # Sheet with Column 1
# df1 = pd.read_excel(file_path, sheet_name='2024')  # Another sheet with Column 2

# # Ensure 'AccessionNo' column exists
# if 'AccessionNo' not in df1.columns or 'AccessionNo' not in df2.columns:
#     raise KeyError("The column 'AccessionNo' must exist in Excel file.")

# # Add missing columns to both DataFrames
# missing_in_df1 = [col for col in df2.columns if col not in df1.columns]
# missing_in_df2 = [col for col in df1.columns if col not in df2.columns]

# for col in missing_in_df1:
#     df1[col] = pd.NA
# for col in missing_in_df2:
#     df2[col] = pd.NA

# # Reorder df2 to match df1
# df2 = df2[df1.columns]

# # Find common and unique AccessionNos
# accession1 = df1['AccessionNo'].dropna().astype(str)
# accession2 = df2['AccessionNo'].dropna().astype(str)

# # Filter matched
# df1_matched = df1[df1['AccessionNo'].astype(str).isin(accession2)]
# df2_matched = df2[df2['AccessionNo'].astype(str).isin(accession1)]

# # Filter unmatched
# df1_unmatched = df1[~df1['AccessionNo'].astype(str).isin(accession2)]
# df2_unmatched = df2[~df2['AccessionNo'].astype(str).isin(accession1)]

# # Combine all: matched + unmatched
# combined_df = pd.concat([df1_matched, df2_unmatched, df1_unmatched], ignore_index=True)

# # Drop fully empty columns (optional)
# combined_df = combined_df.dropna(axis=1, how='all')

# # Save result
# try:
#     combined_df.to_excel('COMBINED_alldata.xlsx', index=False)
#     print("Combined data saved to 'COMBINED_alldata(2).xlsx'.")
# except Exception as e:
#     print(f"Error saving combined file: {e}")



# combine multiple data sheet with no reordering and no dropping of blank columns
import pandas as pd
import numpy as np

# Read all sheets from the Excel file
file_path = 'NGO_referred.xlsx'
df2022 = pd.read_excel(file_path, sheet_name='2022')
df2023 = pd.read_excel(file_path, sheet_name='2023')
df2024 = pd.read_excel(file_path, sheet_name='2024')
df2025 = pd.read_excel(file_path, sheet_name='2025')

dfs = [df2022, df2023, df2024, df2025]

# Check for 'AccessionNo' in all sheets
for i, df in enumerate(dfs, start=2022):
    if 'AccessionNo' not in df.columns:
        raise KeyError(f"'AccessionNo' column missing in sheet {i}")

# Step 1: Get all unique columns across all DataFrames
all_columns = set().union(*[df.columns for df in dfs])

# Step 2: Add missing columns to each DataFrame WITHOUT reordering
aligned_dfs = []
for df in dfs:
    missing_cols = all_columns - set(df.columns)
    if missing_cols:
        # Create a DataFrame for the missing columns
        missing_df = pd.DataFrame({col: pd.NA for col in missing_cols}, index=df.index)
        # Concatenate original df with missing columns (to the right)
        df = pd.concat([df, missing_df], axis=1)
    aligned_dfs.append(df)

# Step 3: Concatenate all aligned DataFrames
combined_df = pd.concat(aligned_dfs, ignore_index=True)

# Step 4: Do NOT drop any columns

# Step 5: Save to Excel
try:
    combined_df.to_excel('COMBINED_alldatacols.xlsx', index=False)
    print("✅ Combined data saved to 'COMBINED_alldata.xlsx'.")
except Exception as e:
    print(f"❌ Error saving combined file: {e}")

