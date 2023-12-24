#Object Oriented Programing(OOP)

#class => benzer veya aynı özelliklteki değişken,metot ,fonksiyonları bir arada tutan yapıya denir.

class Person:
    pass
   # class attributes
    address = 'Bilgi girilmedi.'

   #constructor(yapıcı metot)
   #self sınıfın kendisini temsil eder. Metotların birinci parametresi self olmalıdır.
    def __init__(self,name,year): # initilaze dan gelir. sınıftan  instance oluşturunca otomatik çalışıır. 
         #object attrıbutes 
        self.name = name
        self.year = year
        print('init metodu çalıştı.')
        
      

   # methods

# Person sınıfından bir örnek oluştur
#instance(Object) => örneklem classdan nesne oluşturma işlemine denir.
        #Kullanım 1
p1 = Person(name = 'Berna',year = 1998) 
        #Kullanım 2
p2 = Person('Banu',1997)

#instance lardaki veri değerleri değiştirme
p1.name = 'Lina'

#accessing object attributes
print(f'name : {p1.name} year : {p1.year}  adres : {p1.address}')
print(f'name : {p2.name} year : {p2.year}')
print(type(p1))


