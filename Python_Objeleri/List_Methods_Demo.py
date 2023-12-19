names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
names.append('Berna')
print(names)

# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0,'Sena')
print(names)


# 3-  "Deniz" ismini listeden siliniz.
names.remove('Deniz') # verilen string değeri listeden kaldırır
#names.pop(4) # verilen int index teki değeri kaldırır.
print(names)


# 4-  "Berna" isminin indeksi nedir ?
index = names.index('Berna')
print(index)

# 5-  "Ali" listenin bir elemanı mıdır ?
isEleman = 'Ali' in names
print(isEleman)

# 6-  Liste elemanlarını ters çevirin.
names.reverse()
print(names)
years.reverse()
print(years)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
result = str.split(',')
print(result)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
print(max(years))
print(min(years))

# 11- years dizisinde kaç tane 1998 değeri vardır ?
count = years.count(1998)
print(count)

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []
marka1 = input('İlk marka bilgisini giriniz : ')
markalar.append(marka1)
marka2 = input('İkinci marka bilgisini giriniz : ')
markalar.append(marka2)
marka3 = input('Üçüncü marka bilgisini giriniz : ')
markalar.append(marka3)

print(markalar)

