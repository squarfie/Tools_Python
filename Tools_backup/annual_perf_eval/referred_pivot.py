import pandas as pd

# Load the Excel file
df = pd.read_excel('all_data_for_WHONET.xlsx', engine='openpyxl')

# Define output Excel file
output_file = 'organism_counts_by_site_sheets.xlsx'

# Create a writer object
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Group by Site_code
    for site, group in df.groupby('Site_code'):
        # Count organisms in that site
        org_count = group['ARSRL_Org'].value_counts().reset_index()
        org_count.columns = ['org_name', 'ref_count_df']
        
        # Write to a separate sheet named after the site
        # Ensure sheet name is Excel-compatible (max 31 chars, no special chars like / \ ? * etc.)
        safe_sheet_name = str(site)[:31].replace('/', '_').replace('\\', '_')
        org_count.to_excel(writer, sheet_name=safe_sheet_name, index=False)

print(f"Done! File saved as '{output_file}' with separate sheets per site.")
