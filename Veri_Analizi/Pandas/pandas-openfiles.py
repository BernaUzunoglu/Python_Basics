import sqlite3
import pandas as pd

df = pd.read_csv('DataSets/sample.csv')
df = pd.read_json('DataSets/sample.json',encoding="UTF-8")
df = pd.read_excel("DataSets/sample.xlsx")

connection = sqlite3.connect("DataSets/sample.db")
df = pd.read_sql_query("SELECT * FROM students",connection)

print(df)