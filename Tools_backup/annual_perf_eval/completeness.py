import pandas as pd
import numpy as np

# Load the file 
file_path = 'c:\\TESTINGS\\Tools_backup\\annual_perf_eval\\files\\df_2024.csv'
output_path = 'c:\\TESTINGS\\Tools_backup\\annual_perf_eval\\files\\monthly_completeness_by_laboratory.xlsx'
df = pd.read_csv(file_path)

# Replace string 'nan' with np.nan
df = df.replace(r'^\s*(nan|NaN|NAN|NaT)\s*$', np.nan, regex=True)

# Filter out rows where spec_type is 'qc', 'mi', 'un', 'wa', 'fo' and organism is 'xxx' or 'xpa'
df = df[~df['spec_type'].isin(['qc', 'mi', 'un', 'wa', 'fo', 'en', 'nvbsp'])]
df = df[~df['organism'].isin(['xxx', 'xpa', 'xep', 'xga', 'xgo', 'xmr','xsg', 'xtp'])]


# Demographic columns for completeness calculation
demographic_cols = {
    'Identification number': 'patient_id',  
    'Name (Last name)': 'last_name',
    'Sex': 'sex',
    'Age': 'age',
    'Date of birth': 'date_birth',
    'Location/Ward': 'ward',
    'Department': 'department',
    'Ward Type': 'ward_type',
    'Specimen number': 'spec_num',
    'Specimen date': 'spec_date',
    'Specimen type': 'spec_type',
    'Organism': 'organism',
    'Date of Admission': 'date_admis',
    'Diagnosis': 'diagnosis'
}

# Filter the dataframe to include only specific ward types (inpatients) for 'Date of Admission'
df_ward_type = df[df['ward_type'].isin(['in', 'inx', 'icu'])]

# Check if 'spec_date' is already in datetime format and convert if necessary
df_ward_type['spec_date'] = pd.to_datetime(df_ward_type['spec_date'], errors='coerce')

# Extract month from the 'spec_date' column for all entries in the dataframe
df['spec_date'] = pd.to_datetime(df['spec_date'], errors='coerce')
df['Month'] = df['spec_date'].dt.month

# Use ExcelWriter to save the completeness calculations for each laboratory code
with pd.ExcelWriter(output_path) as writer:

    # Get all unique laboratory codes (assuming 'laboratory' is the column with laboratory codes)
    laboratory_codes = df['laboratory'].unique()

    # Loop through each laboratory code and calculate the monthly completeness
    for lab_code in laboratory_codes:
        # Filter the DataFrame for the current laboratory code
        df_lab = df[df['laboratory'] == lab_code]

        # Prepare the DataFrame to hold completeness results
        completeness = pd.DataFrame(index=demographic_cols.keys(), columns=[
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ])

        # Loop through each demographic field and calculate completeness
        for col_name, col_label in demographic_cols.items():
            if col_name == 'Date of Admission':
                # For 'Date of Admission', only compute completeness for inpatients
                df_ward_type_lab = df_lab[df_lab['ward_type'].isin(['in', 'inx', 'icu'])]
            else:
                # For other fields, no ward_type filter is applied
                df_ward_type_lab = df_lab
            
            # Calculate completeness per month for each column
            for month in range(1, 13):
                df_month = df_ward_type_lab[df_ward_type_lab['Month'] == month]
                total_rows = len(df_month)
                
                if total_rows > 0:
                    # Calculate how many of the entries are not null
                    filled = df_month[col_label].notna().sum()
                    completeness.loc[col_name, completeness.columns[month-1]] = f"{(filled / total_rows) * 100:.2f}%"
                else:
                    completeness.loc[col_name, completeness.columns[month-1]] = "N/A"

        # Write the completeness result to an Excel sheet named after the laboratory code
        completeness.to_excel(writer, sheet_name=f'{lab_code}')

# Output a success message
print("Completeness calculations saved to 'monthly_completeness_by_laboratory.xlsx'")
