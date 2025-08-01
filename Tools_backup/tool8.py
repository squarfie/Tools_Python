#### WORKING ####
### this script generates an automatic interpretation (RIS) based from values in the breakpoints table###
import pandas as pd

file_path = 'c:\\TESTINGS\\files\\KPN_count.xlsx'
break_path = "c:\\TESTINGS\\files\\Breakpoints_2024.csv"

try:
    # Load the data
    df1 = pd.read_excel(file_path)
    df2 = pd.read_csv(break_path, low_memory=False)
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# Verify columns ending with _NM are float
nm_columns = [col for col in df1.columns if col.endswith('_NM')]

for col in nm_columns:
    if not pd.api.types.is_float_dtype(df1[col]):
        print(f"Warning: Column {col} is not float. Converting...")
        df1[col] = df1[col].str.replace(r'[^\d.-]', '', regex=True)
        df1[col] = pd.to_numeric(df1[col], errors='coerce')  

# Iterate over each row in df2
for index, row in df2.iterrows():
    col = row['WHONET_TEST']
    org = row['ORGANISM_CODE']
    r_val = row['R']
    s_val = row['S']
    
    # Ensure r_val and s_val are numeric for comparison
    r_val = pd.to_numeric(r_val, errors='coerce')
    s_val = pd.to_numeric(s_val, errors='coerce')
    
    # Check if the column exists in df1 and organism code matches
    if col in df1.columns and org == 'kpn':
        # Create the interpretation column if it doesn't already exist
        output_col = col + '_R_int'
        if output_col not in df1.columns:
            df1[output_col] = None
        
        
        # Assign interpretations
        for i, col_val in df1[col].items():
            
            col_val = pd.to_numeric(col_val, errors='coerce')  # Convert to numeric
            if pd.isna(col_val):  # Skip NaN values
                continue
            
            if col.endswith('_NM'): # CHECK IF THE COLUMN ENDS WITH _NM THEN DO THE INTERPRETATION  based on R and S values in breakpoints table
           
                if not pd.isna(r_val) and col_val >= r_val:
                    df1.at[i, output_col] ="R"
                elif not pd.isna(s_val) and col_val <= s_val:
                    df1.at[i, output_col] ="S"
                elif not pd.isna(r_val) and r_val < col_val and col_val > s_val:
                    df1.at[i, output_col] = "I" 
            else:
                if not pd.isna(r_val) and col_val <= r_val:
                    df1.at[i, output_col] = "R"
                elif not pd.isna(s_val) and col_val >= s_val:
                    df1.at[i, output_col] = "S"
                elif not pd.isna(r_val) and r_val < col_val < s_val:
                    df1.at[i, output_col] = "I"
              
                    
# Save the updated DataFrame back to the Excel file
output_path = 'c:\\TESTINGS\\files\\KPN_All_data.xlsx'
try:
    df1.to_excel(output_path, index=False)
    print(f"Updated file saved to {output_path}")
except Exception as e:
    print(f"Error saving file: {e}")
