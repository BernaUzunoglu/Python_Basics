message = 'Hello There. My name is Berna UZUNOĞLU'

message = message.upper()
print(message)

message = message.lower()
print(message)
message = message.title() #Her kelimenin baş harfini büyük yapar
print(message)
message = message.capitalize() #SAdece ilk harf büyük olur 
print(message)

message1 = ' Hello There. My name is Berna UZUNOĞLU'
print(message1)
message1 = message1.strip() # baştaki ve sondaki boşluk kareketerini kaldırır.
print(message1)

message = message.split() #Her bir kelimeyi boşluklardan parçalara ayırır.Dizi yapar. Parantez içine verilen değer ile ayırır.
print(message)
print(message[2])

message = ' '.join(message) # Boşlukalar ile birleştirir.
print(message)

index = message.find('berna')
print(index)

result = message.index('berna')
print(result)

isFound = message.startswith('H') # H ile mi başlıyor bool değer döndürür.
print(isFound)

isFound1 = message.endswith('y') # y ile mi bitiyor bool değer döndürür.
print(isFound1)


message = message.replace('berna', 'Lina') # Berna kelimesini bulur ve yerine Lina ile değişir.
print(message)

message = message.replace('Lina',' Berna').replace('uz','Uz').replace('my','My')
print(message)

message2= 'Deneme 123456'
message2 = message2.center(50,'*') # 50 karekter de olacak şekilde stringi ortalıyor
print(message2)

message2= 'Deneme 234'
message2 = message2.ljust(50,'*') # 50 karekter de olacak şekilde stringi sola ekliyor sonra yıldız
print(message2)

message2= 'Deneme 456'
message2= message2.rjust(50,'*') # 50 karekter de olacak şekilde stringi sağa ekliyor sonra yıldız
print(message2)

result = message2.isalpha() # Alfabetik mi 
print(result)

message3 = 'Isalpha'
result = message3.isalpha() # Alfabetik mi  Isalpha ozel karekterleride kontrol ediyor. Nokta boşluk
print(result)

result = '123'.isdigit()
print('Sayısal')
print(result)



