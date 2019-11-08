import pandas as pd

df = pd.read_excel("D:\\6th Semester\\SampleData.xlsx")

print(df['OrderDate'][df['Item']=='Pen'])