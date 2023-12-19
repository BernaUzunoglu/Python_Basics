numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

val = min(numbers)
print(val)
val = max(numbers)
print(val)
val = max(letters)
print(val)

val = numbers[3:6]
print(val)

numbers[4] = 15
print(numbers)

numbers.append('49') # Liste sonuna eleman ekleme
print(numbers)

numbers.insert(3,78) # istenilen indexe eleman ekler
numbers.insert(-1,52)# en sona eleman ekler
print(numbers)

numbers.pop()# en sondaki elemanı siler
numbers.pop(2)# verilen indexteki elemanı kaldırır,siler
numbers.remove(9) # verilen değerdeki elemanı siler
print(numbers)


numbers.sort()#liste sıralanır
letters.sort()# liste alfabetik sıralanır.
numbers.reverse()#sıralandıktan sonra ters çevirdik.

print(len(numbers))#eleman sayısını verir

print(numbers.count(10))# listede verilen değerin kaçtane olduğunu sayar
print(letters.count('y'))

numbers.clear()# elemanları silme