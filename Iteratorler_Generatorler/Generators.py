'''
Eğer oluşturulan değerler bir listede objede saklanması gerekmiyorsa sadece o elemanı o anda kullanıcaksak ve bir daha o elemana
ulaşmamız gerekmiyorsa (yieald her seferinde eleman anlık oluşturu)  bu durumda generators kullanılır.
'''

def cube():
    result = [] # bellek üzerinde yer tutuyor
    for i in range(5):
        result.append(i**3)
    return result

print(cube())

print("*******************GENERATORS*******************************")
#Bellek üzerinde yer tutmayan bir yapı generatör oluşturucaz. Sadece ekranda göstermelik bir değer bellekte tutmaya gerek var mı?

def cube():
    for i in range(5):
        yield i ** 3 # bu ifade bize bir değer üretiyor ve gbize gönderiyor daha sonra bu değer bir yerde saklanmıyor.İkinci kez ulaşamayız.


generaator = cube() # iterable bir obje gönderiyor iterable objeler üzerinde next ile dolaşabiliriz.Generator oluşturduk

iterator = iter(generaator) # iter fonk. generator objesini ıterator oluşturduk

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


print("Generatorü for ile direk yazdırma")
def cube():
    for i in range(5):
        yield i ** 3 

for i in cube():
    print(i)

print("************Liste Yaz ***********************")
liste = [i **3 for i in range(5)] #liste oluşturur
print(liste)

print("************Generator Yaz ***********************")

generaator = (i**3 for i in range(5)) #() parantezler ile yapınca generator olmuş olur - generator object
print(generaator)
print(next(generaator))
print(next(generaator))
print(next(generaator))