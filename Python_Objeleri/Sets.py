#Set; sırasız ve indexlenmemiş bir dizidir. Dizi elemanlarının tekrarlamasına izin vermez. Bir elemandan bir dizide bir tane olur.

fruits = {'orange','apple','banana'}

for x in fruits:
    print(x)


fruits.add('chery')
fruits.update(['mango','grape','apple']) # apple var olduğu için iki kere eklemez
print(fruits)

myList = [1,2,3,4,5,5,6,7,7]
print(set(myList)) # set tipine convert edildiği zaman tekrar eden değerleri bir kere yazar

print('*'*50)
print(fruits)
fruits.remove('mango')
fruits.discard('apple')
print(fruits)

fruits.pop() # pop yapınca rasgele bir eleman silinebilir sırasız olduğu için aslında son elemanı siler Set dizileri indexlenmediği için hangi elemanın silindiği önceden bilinemez.
print(fruits)
