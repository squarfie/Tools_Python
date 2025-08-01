import pandas as pd

#create a column called "Age Distribution" and add age categories based on patient_age column and creates another list that counts the age categories in csv format
#used in tricycle project (RMC)
file_path = 'kleb_0625.xlsx'  # replace with your actual file path
# Load the Excel file into a DataFrame
df1 = pd.read_excel(file_path, sheet_name='Sheet1')  # Another sheet with Column 2


def clean_age(Age):
    if isinstance(Age, str):  
        if "m" or "d" in Age.lower():  # Handle cases like "6m"
            return 0  # Treat all months as infants (0 years)
        try:
            return int(Age)  # Convert string numbers to integers
        except ValueError:
            return None  # Return None for invalid values
    return Age  # If already an integer, return as is

# Apply cleaning function to Age column
df1['patient_age'] = df1['Age'].apply(clean_age)

def categorize_age(patient_age): #adjust this if needed
    
        if patient_age <= 0 <= 4:
            return "0-4"
        elif 5 <= patient_age <= 19:
            return "5-19"
        elif 20 <= patient_age <= 64:
            return "20-64"
        elif patient_age >= 65:
            return "65+"
        else:
            return "Unknown"

# Apply the function to the 'patient_age' column and create a new column for age distribution
df1['Age_Distribution'] = df1['patient_age'].apply(categorize_age) 

# Count the number of entries in each category
age_distribution_counts = df1['Age_Distribution'].value_counts()

# Print the counts for each category
print("Age_Distribution Counts:")
print(age_distribution_counts)

# Optionally save the counts to a file
age_distribution_counts.to_csv('Age_Distribution_Counts.csv', header=["Count"])


# Save the updated DataFrame to a new file
df1.to_excel('tri9_1output.xlsx', index=False)

# Print a sample of the DataFrame to verify
print(df1.head())