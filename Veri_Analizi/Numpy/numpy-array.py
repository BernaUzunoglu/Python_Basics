import numpy as np

result = np.arange(1,100,3)# Birden başlayarak 100 e kadar 3 artıraral dizi oluşturur.100 dahil değil.
result = np.zeros(10)  # float bir değere denk geliyor
result = np.ones(10)
result = np.linspace(25,50,3) # eşit aralıklar ile en sondaki verilen parametre kadar eşit aralklarda eleman bölüyor
result = np.random.randint(0,10) # random farklı bir sayı üretir
result = np.random.randint(1,10,3) # son indeks kadar sayı üretir
result = np.random.rand(5)#0-1 arasında rnd sayı

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)
print(np_multi.sum(axis=1)) # satırların toplamı
print(np_multi.sum(axis=0)) # sütunların toplamı
 
print("--------------------------------------------------")
rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result =  rnd_numbers.max()
result =  rnd_numbers.min()
result = rnd_numbers.mean()#ortalama
result = rnd_numbers.argmax() #en büyük sayının indeksini verir 
result = rnd_numbers.argmin() #en küçük sayının indeksini verir 
print(result)
