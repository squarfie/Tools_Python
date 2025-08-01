import pandas as pd

#checks the generated count days from using tool11_tri.py and department column then generates nosocomial "n,o,x,y,u"
#used in tricycle project (RMC)

# Load the Excel file into a DataFrame
df1 = pd.read_excel('T13_tri_Output.xlsx')  # Adjust the file path if needed


# Define a function to categorize nosocomial into distribution bins
def nosocomial(COUNT_DAYS, DEPARTMENT):
    if pd.notna(COUNT_DAYS):  # if count days is not blank then proceed with the condition for n and y else use the department column
        if COUNT_DAYS <= 48:
            return "n"
        else:
            return "y"
    else:
        if DEPARTMENT == "opd":
            return "o"
        elif DEPARTMENT == "icu" or DEPARTMENT =="sur":
            return "x"
        else:
            return "u"

# Apply the function to each row, passing both 'COUNT_DAYS' and 'DEPARTMENT'
df1['NOSOCOMIAL'] = df1.apply(lambda row: nosocomial(row['COUNT_DAYS'], row['DEPARTMENT']), axis=1) #use the nosocomial function for each rows of count_days and department

#EXPLANATION
#lambda = It allows you to create a function in a single line, making the code more concise.
# syntax: lambda arguments: expression
# lambda: The keyword to define the function.
# arguments: The parameters the function accepts (just like in a regular function, but you can have multiple arguments).
# expression: The expression that is evaluated and returned. It can be any valid Python expression.
# lambda row: The lambda function takes each row of the DataFrame as an argument (row is the variable).
# axis=1: This tells apply() to apply the lambda function row-wise (not column-wise).

# Save the updated DataFrame to a new file
df1.to_excel('T14_tri_Output.xlsx', index=False)

# Print a sample of the DataFrame to verify
print(df1.head())

