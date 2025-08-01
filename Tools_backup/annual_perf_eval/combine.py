import pandas as pd

# Load all sheets from both Excel files
referred_sheets = pd.read_excel("referred_by_site.xlsx", sheet_name=None)
unusual_sheets = pd.read_excel("unusual_by_site.xlsx", sheet_name=None)

# Combine all sheets into single DataFrames
referred_df = pd.concat(referred_sheets.values(), ignore_index=True)
unusual_df = pd.concat(unusual_sheets.values(), ignore_index=True)

# Rename columns if necessary (optional safeguard)
if 'un_count_df' not in unusual_df.columns:
    unusual_df.rename(columns={'ref_count_df': 'un_count_df'}, inplace=True)

# Group both datasets to sum up duplicate org_name entries per site_code
referred_grouped = referred_df.groupby(['site_code', 'org_name'], as_index=False)['ref_count_df'].sum()
unusual_grouped = unusual_df.groupby(['site_code', 'org_name'], as_index=False)['un_count_df'].sum()

# Merge on site_code and org_name
merged_df = pd.merge(
    referred_grouped,
    unusual_grouped,
    on=['site_code', 'org_name'],
    how='outer'
)

# Replace missing values with 0 and convert to int
merged_df['ref_count_df'] = merged_df['ref_count_df'].fillna(0).astype(int)
merged_df['un_count_df'] = merged_df['un_count_df'].fillna(0).astype(int)

# Write per site_code to separate sheets
with pd.ExcelWriter("matched_output_by_site.xlsx", engine="openpyxl") as writer:
    for site in merged_df["site_code"].unique():
        site_df = merged_df[merged_df["site_code"] == site]
        site_df.to_excel(writer, sheet_name=site, index=False)

print("✅ Output saved to 'matched_output_by_site.xlsx'.")
