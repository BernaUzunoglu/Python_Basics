# range
print("------------- RANGE -----------------")
for item in range(50,100,20):
    print(item)
print("------------- RANGE -----------------")
print(list(range(5,100,10)))

# enumerate => ile  indexli for döngüsü oluşturuyoruz. enumerate(iterable, start=0) 
print("----------- ENUMARATE1 ------------------")
isim = 'BERNA'
print(list(enumerate(isim))) # ÇIKTI = > [(0, 'B'), (1, 'E'), (2, 'R'), (3, 'N'), (4, 'A')]// Tuple
print("----------- ENUMARATE2 ------------------")
greeting = 'Hello'
for index, item in enumerate(greeting):
    print(f'index: {index} letter: {item}')

# zip = > verilen liste elemanlarını eşleştirir. ÇIKTI : 1 a 100 mesela
print("----------- ZIP -------------------")
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1, list2, list3)))
print("------------------------------")

for item in zip(list1, list2, list3):
    print(item)

print("------------------------------")
for a,b,c in zip(list1, list2, list3):
    print(a,b,c)
