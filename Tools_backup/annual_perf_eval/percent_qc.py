import pandas as pd
import numpy as np

# Load the file
# Load the file 
file_path = 'c:\\TESTINGS\\Tools_backup\\annual_perf_eval\\files\\df_2024.csv'
output_path = 'c:\\TESTINGS\\Tools_backup\\annual_perf_eval\\files\\monthly_qc.xlsx'
df = pd.read_csv(file_path)

# Replace string 'nan', 'NaN', 'NAN', 'NaT' with real np.nan
df = df.replace(r'^\s*(nan|NaN|NAN|NaT)\s*$', np.nan, regex=True)

# Filter where spec_type is 'qc'
df = df[df['spec_type'] == 'qc']

# Parse the 'spec_date' column into datetime format
df['spec_date'] = pd.to_datetime(df['spec_date'], errors='coerce')

# Extract month as a number
df['Month'] = df['spec_date'].dt.month

# Map month numbers to month short names
month_mapping = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}
df['Month_Name'] = df['Month'].map(month_mapping)

# Create the pivot table
pivot_table = pd.pivot_table(
    df,
    index='laboratory',      # Row: laboratory code
    columns='Month_Name',    # Column: month name
    values='organism',       # Value: organism (any non-null entry will be counted)
    aggfunc=lambda x: 1 if x.count() > 0 else 0,  # 1 if there is data, else 0
    fill_value=0             # Fill missing with 0
)

# Ensure correct month order
pivot_table = pivot_table.reindex(columns=[
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
], fill_value=0)

# Save to Excel
with pd.ExcelWriter(output_path) as writer:
    pivot_table.to_excel(writer)

print("Done! File saved as mmonthly_qc.xlsx.")
