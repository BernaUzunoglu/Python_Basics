import random
#rasgele sayılar üretmek için kullanılan bir modül

# result = dir(random)
# result = help(random)

result = random.random() # 0.0 - 1.0
print(result)
result = random.random() * 100
print(result)
result = int(random.uniform(10,100))
print(result)
result = random.randint(1,100)
print(result)

greeting = 'hello there'
names = ['ali','yağmur','deniz','cenk','ahmet','efe']
# result = names[random.randint(0,len(names)-1)]

result = random.choice(names)
print(result)
result = random.choice(greeting)
print(result)

liste = list(range(10))
random.shuffle(liste) #elemanları karışştırır
result = liste

liste = range(100)
result = random.sample(liste, 3) # listede istenilen kadar değer döndürür mesela rasgele 3 eleman verir
result = random.sample(names, 2)

print(result)