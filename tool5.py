import pandas as pd
import openpyxl
# group the data per lab code and save it in separate sheets
file_path = 'c:\\TESTINGS\\files\\2023_dataAll.xlsx'
output_path = 'c:\\TESTINGS\\output\\con_data.xlsx'


df1 = pd.read_excel(file_path)
df_con = df1[['LABORATORY','WARD','DEPARTMENT','WARD_TYPE']]
try:
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        grouped = df_con.groupby('LABORATORY')
        for site, group in grouped: # assign as site for each lab code seen in laboratory column
           group.to_excel(writer,index = False, sheet_name=site)

except Exception as e:
    print(f"Error writing the file: {e}")

