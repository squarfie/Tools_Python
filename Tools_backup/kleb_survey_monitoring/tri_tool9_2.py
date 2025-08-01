import pandas as pd

#create a column called "Age_GRP" and assigns the appropriate age group based on Age column
#used in tricycle project (RMC)

# Load the Excel file into a DataFrame
df1 = pd.read_excel('tri9_1output.xlsx')  # Adjust the file path if needed

# Define a function to categorize age into distribution bins
def categorize_age(Age):
    if 0 <= Age <= 4:
        return "0-4"
    elif 5 <= Age <= 19:
        return "5-19"
    elif 20 <= Age <= 64:
        return "20-64"
    elif Age >= 65:
        return "65+"
    else:
        return "Unknown"
    
# Apply the function to the 'patient_age' column and create a new column for age distribution
df1['AGE_GRP'] = df1['Age'].apply(categorize_age)


# Save the updated DataFrame to a new file
df1.to_excel('sero_agegrp_data.xlsx', index=False)

# Print a sample of the DataFrame to verify
print(df1.head())

