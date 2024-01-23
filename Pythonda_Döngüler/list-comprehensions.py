
'''
Python'da manuel olarak liste oluşturabileceğiniz gibi otomatik olarak listeler de oluşturabiliriz. Python'da buna
 "List Comprehension" denir.
'''

numbers = []
for x in range(10):
    numbers.append(x)

print(numbers)  

print("------------------------------")
numbers = [x for x in range(10)]
print(numbers)

print("------------------------------")
for x in range(10):
    print(x**2)


print("------------------------------")
numbers = [x**2 for x in range(10)]    
print(numbers)


print("------------------------------")
numbers = [x*x for x in range(10) if x%3==0]
print(numbers)

print("------------------------------")
# dizileri ile yeni diziler oluşturulabilmek
myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)
print(myList)


print("------------------------------")
myList = [letter for letter in myString] # List comprehensions
print(myList)


print("----------- Age Example-------------------")
years = [1983, 1999, 2008, 1956, 1986]
ages = [2024-year for year in years] # years listesinde dolaşıyor her bir elemanı 2024 çıkarıp sonucu ages listesine atıp yeni bir liste oluşturuyor.
print(ages)


print("------------------------------")
results = [x if x%2==0 else 'TEK' for x in range(1, 10)]
print(results)



print("------------------------------")
result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)


print("------------------------------")
numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)