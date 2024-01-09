import numpy as np

numbers = np.array([0,5,10,15,25,50,75 ])

result = numbers[5]
print(result)
result = numbers[-1]
print(result)
result = numbers[0:3]
print(result)
result = numbers[:3]
print(result)
result = numbers[3:]
print(result)
result = numbers[::]
print(result)
result = numbers[::-1] #listeyi ters çevirme birer birer
print(result)
result = numbers[::-2] #listeyi ters çevirme ikişer ikişer
print(result)

print("---------------------------------------------")

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
print(numbers2)
result = numbers2[0] # birinci satır yazdırılır
result = numbers2[0,2]
result = numbers2[2,2]
print(result)
result = numbers2[:,2] # bütün satırları seç ve 2.indexteki değerleri geit. 2. indexteki sütun seçildi.
print(result)
result = numbers2[:,0:2] # tüm satırları seç 0 ve 2 indexteki aralıktaki 0 ve 1 sütun gelir 2 dahil değil
print(result)
result = numbers2[:,1:3] # tüm satırları seç 1 ve 3 indexteki aralıktaki 1 ve 2 sütun gelir 
print(result)
result = numbers2[-1,:] # son satır tüm sutun alınır
print(result)
result = numbers2[:,-1] # son sütun tam satır alınır
print(result)

print("----------------------------------------------------")
arr1 = np.arange(0,10)
arr2 = arr1 # referans kopyalama - aynı adres ile tutulur
arr3 = arr1.copy()# farklı adreslerde tutlan veri kopyalaması
arr2[0] = 2 # değeri atanınca arr1[0] indexteki değerde değişir çünkü aynı adreste tutulan aynı veriyi değişiyoruz.
arr3[0] = 5
print(arr1)
print(arr2)
print(arr3)