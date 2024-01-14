import pandas as pd 
import numpy as np 

data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data , index=['a','c','e','f','h'],columns=['column1','column2','column3'])

df = df.reindex(['a','b','c','d','e','f','g','h'])
newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn
result = df

result = df.drop("column1" , axis = 1)#axis varsayılan 0 satıra denk geliyor.drop silme
result = df.drop(["column1","column2"] , axis = 1)
result = df.drop("a" , axis = 0)
result = df.drop(["a","d","h"] , axis = 0)

#NaN alanları tespit etme
result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
result = df["column1"].isnull().sum()
result = df[df["column1"].isnull()]["column1"]
result = df[df["column1"].notnull()]["column1"]
result = df[df["column1"].notnull()]

print(df)
result  = df.dropna()# Drop gibi siler na sıda NaN alanları siler. Sadece veriler olan getiri.
result = df.dropna(axis = 1)#sutuna göre
result = df.dropna(how = 'any') # herhangi bir NaN alan görürse siler 
result = df.dropna(how = 'all') # hepsi NaN olan satırları siler axis 0 olduğu için satıra bakıyor
result = df.dropna (how = 'all',axis = 1)
result = df.dropna (how = 'any',axis = 1)
result = df.dropna(subset = ["column1","column2"]) # column1 ve column2 NaN değer olmayacak şekilde getirir.
result = df.dropna(subset = ["column1","column2"],how = "all")
result = df.dropna(subset = ["column1","column2"],how = "any")
result = df.dropna(thresh = 2) # eğer satırda verilen değerden daha az Nan varsa siler
result = df.dropna(thresh = 4)# en sayıda normal veri olması gerek demek 
result = df.dropna(thresh = 4,axis = 1)
result = df.dropna(thresh = 6,axis = 1) #sutun bayunca bakar eğer 6 dan az veri değeri varsa getirmez.

result = df.fillna(value = 'no input') # NaN olan alanları verilen değer ile doldurur.
result = df.fillna(value = 1) 

# mesela NaN olan kısma avg değerler yazılabilir

result = df.sum() # column1 = 290 şeklinde değerleri toplar
print(result)
result = df.sum().sum()# her bir columndaki değerleri toplar ve df daki toplam değeri bulur 
result = df.size # df eleman sayısı - boyutu
result = df.isnull().sum()
result = df.isnull().sum().sum()


def ortalama(df):
    # toplam = df.sum().sum()
    # adet = df.size
    # ortalama =toplam /  adet
    ortalama =df.sum().sum() /  df.size
    return ortalama

print(ortalama(df))
print(result)
# print(df)