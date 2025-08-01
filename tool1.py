### WORKING ###

import pandas as pd
import numpy as np


# this code will check the spec type values if it exists in SPCELISTE and adds the corresponding numeric specimen code to the sentinel site data

df1 = pd.read_excel('c:\\TESTINGS\\files\\W1124PHL_DMC.xlsx')  ## indicate the filename of the sentinel site data here
df2 = pd.read_excel('c:\\TESTINGS\\files\\SPCLISTE.xlsx') ## do not delete this file

df1['SPEC_CODE'] = df1['SPEC_TYPE'].map(df2.set_index('CODE')['NUMERIC'])
print(df1)

output_file = 'c:\\TESTINGS\\output\\W1124PHL_DMC.xlsx'  ### change the filename of the output file here
df1.to_excel(output_file, index=False)