import pandas as pd

# Load all sheets from both Excel files
referred_sheets = pd.read_excel("referred_by_site.xlsx", sheet_name=None)
unusual_sheets = pd.read_excel("unusual_by_site.xlsx", sheet_name=None)

# Combine all sheets into DataFrames
referred_df = pd.concat(referred_sheets.values(), ignore_index=True)
unusual_df = pd.concat(unusual_sheets.values(), ignore_index=True)

# Rename if needed
if 'un_count_df' not in unusual_df.columns:
    unusual_df.rename(columns={'ref_count_df': 'un_count_df'}, inplace=True)

# Group and sum counts per site/org
referred_grouped = referred_df.groupby(['site_code', 'org_name'], as_index=False)['ref_count_df'].sum()
unusual_grouped = unusual_df.groupby(['site_code', 'org_name'], as_index=False)['un_count_df'].sum()

# Merge the two summaries
merged_df = pd.merge(
    referred_grouped,
    unusual_grouped,
    on=['site_code', 'org_name'],
    how='outer'
)

# Fill missing values
merged_df['ref_count_df'] = merged_df['ref_count_df'].fillna(0).astype(int)
merged_df['un_count_df'] = merged_df['un_count_df'].fillna(0).astype(int)

# Dictionary of required counts
required_dict = {
    "Acinetobacter baumanni": 15,
    "Enterococcus faecalis": 15,
    "Escherichia coli": 15,
    "Klebsiella pneumoniae": 10,
    "Pseudomonas aeruginosa": 15,
    "Staphylococcus aureus": 15
}

# Add Required column
merged_df['Required'] = merged_df['org_name'].map(required_dict)

# Function to compute % referred
def compute_percent(row):
    if pd.notna(row['Required']) and row['ref_count_df'] < row['Required']:
        return f"{round(row['ref_count_df'] / row['Required'] * 100)}%"
    elif pd.isna(row['Required']) and row['un_count_df'] != 0 and row['ref_count_df'] < row['un_count_df']:
        return f"{round(row['ref_count_df'] / row['un_count_df'] * 100)}%"
    else:
        return "100%"

# Apply the logic
merged_df['% referred'] = merged_df.apply(compute_percent, axis=1)

# Export per site_code
with pd.ExcelWriter("matched_output_with_required_and_percent.xlsx", engine="openpyxl") as writer:
    for site in merged_df['site_code'].unique():
        site_df = merged_df[merged_df['site_code'] == site]
        site_df.to_excel(writer, sheet_name=site, index=False)

print("✅ Output saved to 'matched_output_with_required_and_percent.xlsx'.")
