import pandas as pd

#transpose lab_esbl column data into  ESBL column with symbols +, - and u
#used in tricycle project (RMC)

# Load the Excel file into a DataFrame
df1 = pd.read_excel('T9_tri3_Output.xlsx')  # Adjust the file path if needed

# Define a function to categorize age into distribution bins
def ESBL(lab_esbl):
    if lab_esbl == "positive":
        return "+"
    elif lab_esbl == "negative":
        return "-"
    else:
        return "u"
    
# Apply the function to the 'patient_age' column and create a new column for age distribution
df1['ESBL'] = df1['lab_esbl'].apply(ESBL)


# Save the updated DataFrame to a new file
df1.to_excel('T9_tri3_Output1.xlsx', index=False)

# Print a sample of the DataFrame to verify
print(df1.head())

