import pandas as pd
#counts the total kpn isolates per laboratory

# Load the Excel file into a DataFrame
df1 = pd.read_excel('KPN_CARBA.xlsx', engine='openpyxl')  # Use openpyxl for better .xlsx support

# Filter only blood specimens ('bl')
df_filtered = df1[df1['Organism'] == 'kpn']

# Create a pivot table to count occurrences of 'S' for each antibiotic per laboratory
pivot_df = pd.pivot_table(
    df_filtered,
    index='Laboratory',  # Group by Laboratory
    values=['Organism',],  # Columns to check for susceptible isolates
    aggfunc=lambda x: (x == 'kpn').sum()  # Count how many times 'S' appears in each antibiotic column
)

# Create an Excel writer object using openpyxl
output_file = 'KPN_survey_pivot_TRY3.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    # Write the pivot table to a new sheet
    pivot_df.to_excel(writer, sheet_name='Susceptible_Counts', index=True)

# Print confirmation
print(f"Excel file '{output_file}' created with susceptible counts per antibiotic.")
