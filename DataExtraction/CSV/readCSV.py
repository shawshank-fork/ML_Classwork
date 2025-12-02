import pandas as pd
from io import StringIO

csv_data = """Name,Age,Occupation
Shashank,21,CSE"""

df_csv = pd.read_csv(StringIO(csv_data))

engineers_data_csv = df_csv[df_csv['Occupation'] == 'CSE'][['Name', 'Age']]

print("data:")
print(engineers_data_csv)