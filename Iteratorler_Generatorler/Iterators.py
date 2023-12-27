liste = [1,2,3,4,5]#iterable bir obje

# for i in liste: # for döngüsü bir iterator oluşturuyor.
#     print(i)

iterator = iter(liste)
print(next(iterator)) # Sonraki elemana geçiriyor
print(next(iterator))
print(next(iterator))

iterator = iter(liste) # iterator oluşturuldu


while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration: # eleman sayısı bitince verilecek hata
        break


class MyNumbers:

    def __init__(self,start,stop):
        self.start = start
        self.stop = stop


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start +=1 
            return x
        else:
            raise StopIteration


print("*************************************************")        
list = MyNumbers(10,20)

# for x in list:
#     print(x)

#for döngüsü olmadan yazdıralım
myiter = iter(list)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
    