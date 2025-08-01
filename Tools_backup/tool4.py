import pandas as pd
import openpyxl
# creates a file that lists of all ward and ward types per sentinel site
file_path = 'c:\\TESTINGS\\files\\2023_dataAll.xlsx'
output_path = 'c:\\TESTINGS\\output\\tool4_output.xlsx'


df1 = pd.read_excel(file_path)
df_con = df1[['LABORATORY','WARD','DEPARTMENT','WARD_TYPE']]
try:
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        grouped = df_con.groupby('LABORATORY')
        for site, group in grouped: # assign as site for each lab code seen in laboratory column
           group.to_excel(writer,index = False, sheet_name=site)

except Exception as e:
    print(f"Error writing the file: {e}")

