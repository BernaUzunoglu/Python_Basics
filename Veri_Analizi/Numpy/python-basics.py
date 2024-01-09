import numpy as np

print("********** Numpy kütüphanesi kullanımı ****************")
# print(numpy.version.version)
'''Büyük verileri numpy kütüphanesinin nesnelerine atarak daha kullanışlı hale getiriyoruz. Daha az yer kaplıyor, daha hızlı çalışıyor'''
py_list = [1,2,3,4,5,6,7,8,9]

#numpy arrray
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3) # çok boyutlu birdizi, matris

print(py_multi)
print(np_multi)

#ndim: Dizinin boyut sayısı veya eksen sayısıdır.
print(np_array.ndim)#1 boyutlu
print(np_multi.ndim)#2 boyutlu - satır x sutun

print(np_array.shape) #(9,)
print(np_multi.shape) #(3, 3)

