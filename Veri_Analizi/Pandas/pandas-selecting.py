import pandas as pd 
from numpy.random import randn 

df = pd.DataFrame(randn(3,3),index=['A','B','C'],columns=['Column1','Column2','Column3'])

result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]

# loc["row","column"] => loc["row"] => loc[":","column"]
result = df.loc['A']#locationdan geliyor
print("--------------1------------------")
result = df.iloc[2]#örnekte indexleri A,B,C diye ayarladık ama yinede index olarak kullanmak istiyorsak iloc yaparız.
print(result)
print("--------------2------------------")
result = df.loc[:,"Column1"]#: öncesi satır
print(result)
print("--------------3------------------")
result = df.loc[:,["Column1","Column2"]]
print(result)
print("---------------4-----------------")
result = df.loc[:,"Column1":"Column2"] # : nokta arada olunca verilen kolonlar arsında veriler gelir
print(result)
print("---------------5-----------------")
result = df.loc[:,:"Column2"]
print(result)
print("----------------6----------------")
result = df.loc["A":"B",:"Column2"]
print(result)
print("----------------7----------------")
result = df.loc[:"B",:"Column2"]
print(result)
print("----------------8----------------")
result = df.loc["A","Column2"]
print(result)
print("-----------------9---------------")
result = df.loc["C","Column1"]
print(result)
print("-----------------10---------------")
result = df.loc[["A","B"],["Column1","Column2"]]
print(result)
print("-----------------11---------------")

df["Column4"] = pd.Series(randn(3), ["A","B","C"])
print(df)
print("-----------------12---------------")
df["Column5"] = df["Column1"] + df["Column3"]
print(df)
print("-----------------13---------------")
print(df)
print(df.drop("Column5", axis = 1, inplace = False) )# kolon silme axis ile 1 sutun, 0 satır ifade eder, inplace => If False, return a copy. Otherwise, do operation in place and return None.


print(df) 
