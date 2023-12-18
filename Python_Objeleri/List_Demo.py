# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']

# 2-  Liste Kaç elemanlıdır ?
print(len(cars))

# 3-  Listenin ilk ve son elemanı nedir ?
print('Listenin ilk elemanı :' + cars[0])
print('Listenin son elemanı :' + cars[-1])
print('Listenin son elemanı :' + cars[len(cars)-1])

# 4-  Mazda değerini Toyota ile değiştirin.
# arabalar[-1]= 'Toyota'
cars[len(cars)-1] = 'Toyota'
print(cars)

# 5-  Mercedes listenin bir elemanı mıdır ?
print('Mercedes' in cars)

# 6-  Listenin -2 indeksindeki değer nedir ?
print(cars[-2])

# 7-  Listenin ilk 3 elemanını alın.
print(cars[0:3])
print(cars[:3])

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
cars[-2] = 'Renault','Toyata' #çıktı : ['Bmw', 'Mercedes', ('Renault', 'Toyata'), 'Toyota']
cars[-2] = ['Toyota','Renault']
print(cars)

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
cars.append('Audi')
cars.append('Nissan')
print(cars)

result = cars + ['Audi', 'Nissan']
print(result)

# 10- Listenin son elemanını silin.
cars.pop(-1)
print(cars)

result.remove('Toyota')
print(result)

del result[-1]
print(result)


# 11- Liste elemanlarını tersten yazdırınız.
result = cars[::-1]
print(result)

# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA = ['Yiğit', 'Bilgi','2010','(70,60,70)']
studentB = ['Sena', 'Turan','1999','(80,80,70)']
studentC = ['Ahmet', 'Turan','1998','(80,70,90)']

studentsAll = studentA + studentB + studentC

# 13- Liste elemanlarını ekrana yazdırınız.
print(studentA)
print(studentB)
print(studentC)
print(studentsAll)


