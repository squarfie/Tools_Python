import pandas as pd

# Load the Excel file
df = pd.read_excel('all_data_for_WHONET.xlsx', engine='openpyxl')

# Create an Excel writer
output_file = 'trial_referred.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Group by Site_code
    for site, group in df.groupby('Site_code'):
        # Count non-null ARSRL_Org values
        organism_count = group['ARSRL_Org'].notna().sum()

        # Add a row for the count at the bottom of the sheet
        summary_df = pd.DataFrame([['Total Organisms', organism_count]], columns=['ARSRL_Org', 'Count'])

        # Write site-specific data and then the count
        group.to_excel(writer, sheet_name=str(site), index=False, startrow=0)
        summary_df.to_excel(writer, sheet_name=str(site), index=False, startrow=len(group) + 2)

print(f"Excel file '{output_file}' created with separate sheets for each site and organism counts.")
