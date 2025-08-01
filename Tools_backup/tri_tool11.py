import pandas as pd

#create a COUNT_DAYS column that computes the number of days a patient stays in the hospital
#used in tricycle project (RMC)

# Load the Excel file into a DataFrame
df1 = pd.read_excel('T12_tri_Output.xlsx')  # Adjust the file path if needed

admdate = pd.to_datetime(df1['DATE_ADMIS'], errors='coerce') #used to handle invalid parsing situations when converting values to datetime or numeric types. When you specify errors='coerce', any invalid or unrecognized values will be replaced with NaT (for datetime) or NaN (for numeric types), instead of raising an error.
spdate = pd.to_datetime(df1['SPEC_DATE'], errors='coerce')


df1['COUNT_DAYS'] = (spdate - admdate).dt.days #.dt.days used to access datetime properties of a column (or Series) that contains datetime-like objects. When you use .dt.days, you're extracting the number of days from a timedelta (the difference between two dates) or getting the day of the month or other related datetime information.
df1['COUNT_DAYS'] = df1['COUNT_DAYS'].fillna("") #used to replace NaT values (i.e., when 'DATE_ADMIS' is missing) with "" (BLANK) in the 'COUNT_DAYS' column. This way, you avoid the need for an explicit if-else condition.


# Save the updated DataFrame to a new file
df1.to_excel('T13_tri_Output.xlsx', index=False)

# Print a sample of the DataFrame to verify
print(df1.head())

