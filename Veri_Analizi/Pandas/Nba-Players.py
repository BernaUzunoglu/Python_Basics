import pandas as pd
import os
print(os.getcwd())


# df = pd.read_csv("DataSets/nba.csv")
df = pd.read_csv("C:\\Users\\BERNA\\OneDrive\\Masaüstü\\Python_Basics\\Veri_Analizi\\Pandas\\DataSets\\nba.csv")

#ilk  kaydı getiriniz.
result = df.head(10)
print(result)

#Toplam kaç kayıt vardır.
result = len(df.index)
print(result)

# Tüm oyuncuların toplam maaş ortalaması kaçtır.
result = df["Salary"].mean() # Kolonların ismi büyük küçük harf duyarlı
print(result)

# Yaşı 20 -25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
result = df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name","Team","Age"]].sort_values("Age",ascending=False)
print(result) 

print('"John Holland" isimli oyuncunun oynadığı takım hangisidir ?')
'''Loc komutu ile etiket kullananarak verimize ulaşırken, iloc komutunda satır ve sütün index numarası ile verilerimize 
ulaşmaktayız, Yani loc komutunu kullanırken satır yada kolon ismi belirtirken, iloc komutunda satır yada sütünün index numarasını 
belirtiyoruz.'''
result = df[df["Name"] == "John Holland" ]["Team"].iloc[0]
print(result)

print("Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?")
result = df.groupby(["Team"])["Salary"].mean()
print(result)

print(" # 9- Kaç farklı takım mevcut ?")
result = len(df.groupby(["Team"]))
print(result)
result = df["Team"].unique() # Tekrar etmeyen değerleri ekrana getirir.
print(result)

print("# 10- Her takımda kaç oyuncu oynamaktadır ?")
result = df["Team"].value_counts()
print(result)

print("# 11- İsmi içinde 'and' geçen kayıtları bulunuz.")
result = df.dropna(inplace = True)


def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = df[df["Name"].apply(str_find)]

print(result)

