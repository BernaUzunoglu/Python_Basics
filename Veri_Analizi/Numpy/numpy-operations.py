import numpy as np

numbers1 = np.random.randint(10,100,6)#10-100 arasında 6 tane değer
numbers2 = np.random.randint(10,100,6)
print(numbers1)
print(numbers2)
print("-------------------------")
result = numbers1 + numbers2
print(result)
result = numbers1 + 10 #her elemana 10 ekler
print(result)
result = numbers1 -2
print(result)
result = numbers1 * numbers2
print(result)
result = numbers2 * 10
print(result)
result = numbers1 / numbers2
print(result)
result = numbers2 / 10
print(result)
result = np.sin(numbers1)
print(result)
result = np.cos(numbers2)
print(result)
result = np.sqrt(numbers2)
print(result)
result = np.log(numbers2)
print(result)
print("--------------------------------------")

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)
print(mnumbers1)
print(mnumbers2)
print("********************")
result = np.vstack((mnumbers1,mnumbers2))#Dizileri dikey olarak (satır bazında) sırayla birleştiriyor
print(result)
result = np.hstack((mnumbers1,mnumbers2))#Dizileri yatay olarak (sütun bazında) sırayla birleştiriyor
print(result)

result = mnumbers1 >= 50
print(result)

print(mnumbers1)
result = mnumbers1 % 3 == 0
print(mnumbers1[result])