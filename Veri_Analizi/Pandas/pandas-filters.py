import pandas as pd
import numpy as np

# DataFrame filter uygulamaları
data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns = ["Column1","Column2","Column3","Column4","Column5"])
result = df

result = df.columns # Kolon isimlerini getirir.
result = df.head()
result = df.head(10) # ilk 10 kaydı getirir.
result = df.tail(10) # son 10 satır getirilir.
result = df["Column1"].head() # Kolon seçme
result = df.Column1.head()
result = df[["Column1","Column2"]]# birden fazla kolon seçimi yapacaksak eğer liste şeklinde göndermemiz gerek.
result = df[["Column1","Column2"]].head() # varsayılan 5 olarak alıyor 5 kayıt.
result = df > 50 # Kolonlardaki verilere bakar 50 den büyük olanlara true değeri döndürür.
result = df[df>50]
result = df[df %2 == 0]
result = df[df["Column1"] >50] # Column1 üzerinden 50 den büyük olan kayıtları getirir.
result = df[df["Column1"] >50][["Column1","Column2"]] 
result = df[(df["Column1"] >50) & (df["Column1"] <= 70)][["Column1","Column2"]] 
result = df[(df["Column1"] >50) | (df["Column1"] <= 70)][["Column1","Column2"]] 

result = df.query("Column1 >= 50 & Column1 % 2 == 0")
result = df.query("Column1 >= 50 | Column1 % 2 == 0")
print(result)
