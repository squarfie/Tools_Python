import pandas as pd

#create a column called "AGE_GRP" and add age categories 'a,b,c,d,u' based on AGE_DISTRIBUTION column generated from tri_tool9_1.py
#used in tricycle project (RMC)

# Load the Excel file into a DataFrame
df1 = pd.read_excel('COMBINED_RMC_agedist.xlsx')  # Adjust the file path if needed

# Define a function to categorize age into distribution bins
def categorize_age(Age_Distribution):
    if Age_Distribution == "0-4":
        return "a"
    elif Age_Distribution == "5-19":
        return "b"
    elif Age_Distribution == "20-64":
        return "c"
    elif Age_Distribution == "65+":
        return "d"
    else:
        return "u"
    
# Apply the function to the 'patient_age' column and create a new column for age distribution
df1['AGE_GRP'] = df1['Age_Distribution'].apply(categorize_age)


# Save the updated DataFrame to a new file
df1.to_excel('tri_tool9_3_Output1.xlsx', index=False)

# Print a sample of the DataFrame to verify
print(df1.head())

