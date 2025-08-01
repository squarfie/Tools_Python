### WORKING ###

import pandas as pd
import numpy as np
import os
## A code to combine two excel files - will check for matching columns if a column is not present, add it in the file.

import pandas as pd


# Load the two Excel files into DataFrames
df1 = pd.read_excel('c:\\TESTINGS\\files\\W1024PHL_DMC.xlsx')
df2 = pd.read_excel('c:\\TESTINGS\\files\\W1124PHL_DMC.xlsx')


# Find columns that are in df2 but not in df1, and vice versa
missing_in_df1 = [col for col in df2.columns if col not in df1.columns]
missing_in_df2 = [col for col in df1.columns if col not in df2.columns]

# Add missing columns to df1 and df2 with NaN values
for col in missing_in_df1:
    df1[col] = pd.NA  # Add missing columns to df1 with NaN values

for col in missing_in_df2:
    df2[col] = pd.NA  # Add missing columns to df2 with NaN values

# Reorder columns to ensure they match
df2 = df2[df1.columns]

# Concatenate the two DataFrames along rows
combined_df = pd.concat([df1, df2], ignore_index=True)

try:
# Save the combined DataFrame to a new Excel file
    combined_df.to_excel('c:\\TESTINGS\\output\\W1124PHL_DMC(1).xlsx', index=False)   

except Exception as e:

    print("DataFrames combined and saved to {e}.")
