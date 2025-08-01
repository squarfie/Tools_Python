import pandas as pd

# Load your dataset
df = pd.read_excel("consolidated_unusual.xlsx")  # Replace with actual filename

# Group by both site_code and org_name, then sum ref_count_df
grouped = df.groupby(['site_code', 'org_name'], as_index=False)['un_count_df'].sum()

# Create a writer object
with pd.ExcelWriter("unusual_by_site.xlsx", engine='openpyxl') as writer:
    # Loop through each site_code and write to separate sheets
    for site in grouped['site_code'].unique():
        site_df = grouped[grouped['site_code'] == site]
        site_df.to_excel(writer, sheet_name=site, index=False)

print("Excel file 'unusual_by_site.xlsx' created successfully.")
