import numpy as np

print("1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.")
np_array = np.array([10,15,30,45,60])

print("2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.")
np_array = np.arange(5,15)
print(np_array)

print(" 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.")
np_array = np.arange(50,100,5)
print(np_array)

print(" 4-> 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.")
np_array = np.zeros(10)
print(np_array)

print(" 5-> 10 elemanlı birlerden oluşan bir dizi oluşturunuz.")
np_array = np.ones(10)
print(np_array)

print(" 6- (0-100) arasında eşit aralıklı 5 sayı üretin.")
np_array = np.linspace(0,100,5)
print(np_array)

print(" 7- (10-30) arasında rastgele 5 tane tamsayı üretin.")
np_array = np.random.randint(10,30,5)
print(np_array)

print(" 8- [-1 ile 1] arasında 10 adet sayı üretin.")
np_array = np.random.rand(10)
print(np_array)

print(" 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.")
np_multiarray = np.random.randint(10,50,15).reshape(3,5) # 3*5 =15 elemanlı
print(np_multiarray)

print(" 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız ?")
rowSum = np_multiarray.sum(axis=1) #satırlar
print(rowSum)
colSum = np_multiarray.sum(axis=0)#sutunlar
print(colSum)

print("11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?")
print(np_multiarray)
maxNum = np_multiarray.max()
minNum = np_multiarray.min()
meanNum = np_multiarray.mean()
print(maxNum)
print(minNum)
print(meanNum)

print(" 12- Üretilen matrisin en büyük değerinin indeksi kaçtır ?")
maxNumindex = np_multiarray.argmax()
minNumindex = np_multiarray.argmin()
print(maxNumindex)
print(minNumindex)

print(" 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.")
np_array = np.arange(10,20)
print(np_array)
result = np_array[:3]
print(result)


print(" 14- Üretilen dizinin elemanlarını tersten yazdırın.")
result = np_array[::-1]
print(result)

print(" 15- Üretilen matrisin ilk satırını seçiniz.")
print(np_multiarray)
result = np_multiarray[0]
print(result)

print(" 16- Üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir ?")
result = np_multiarray[1,2]
print(result)

print(" 17- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.")
result = np_multiarray[:,0]
print(result)

print(" 18- Üretilen matrisin her bir elemanının karesini alınız.")
print(np_multiarray)
result = np_multiarray ** 2
print(result)

print(" 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır ? ")
#     Aralığı (-50,+50) arasında yapınız.
np_multiarray2 = np.random.randint(-50,50,9).reshape(3,3)
print(np_multiarray2)
result = np_multiarray2 % 2 == 0
print(np_multiarray2[result > 0])

