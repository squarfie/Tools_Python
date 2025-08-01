import pandas as pd

#checks the ward column and automatically creates a DEPARTMENT column that assigns the appropriate department code 
#used in tricycle project (RMC)

# Load the Excel file into a DataFrame
df1 = pd.read_excel('tri_tool9_3_Output.xlsx')  # Adjust the file path if needed


# Define a function to categorize age into distribution bins
def loc_type(WARDS):
    df1['WARDS'].fillna('Unk', inplace=True) # for empty rows place Unk
    WARDS = str(WARDS) #force transpose all wards to str
    if "ER" in WARDS or "EME" in WARDS or "EMR" in WARDS:
        return "eme"
    elif "ICU" in WARDS:
        return "icu"
    elif "OBG" in WARDS:
        return "obg"
    elif "SWD" in WARDS:
        return "sur"
    elif "Unk" in WARDS:
        return "Unk"
    else:
        return "oth"
    
# Apply the function to the 'WARD' column and create a new column for age distribution
df1['DEPARTMENT'] = df1['WARDS'].apply(loc_type)


# Save the updated DataFrame to a new file
df1.to_excel('tri_tool10_Output.xlsx', index=False)

# Print a sample of the DataFrame to verify
print(df1.head())

