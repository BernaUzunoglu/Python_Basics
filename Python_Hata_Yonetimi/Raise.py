 # Programcının belirli bir istisnanın gerçekleşmesini istediği durumşarda kullanılır.

# x = 10
# if x > 5:
#     raise Exception("x 5'den büyük değer alamaz")

def check_password(psw):
    import re #Regular expression modulü
    if len(psw) < 7:
        print(len(psw))
        raise Exception ("Parola en az 7 karekter olmalıdır.")
    elif not re.search("[a - z]",psw):
        raise Exception("Parola küçük harf içermelidir")
    elif not re.search("[A - Z]",psw):
        raise Exception("Parola büyük harf içermelidir")
    elif not re.search("[0 - 9]",psw):
        raise Exception("Parola rakam harf içermelidir")
    elif not re.search("[*-$]",psw):
        raise Exception("Parola alfa numerk karekter  içermelidir")
    elif re.search(r"\s",psw):
        raise Exception("Parola boşluk  içermemelidir")
    
password = "123aH7*"
try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Geçerli parola")
finally:
    print("validasyon tamamlandı")

class Person:
    def __init__(self,name,year):
        if len(name) > 10 :
            raise Exception("Name alanı 10 karekterden büyük olamaz ")
        else:
            self.name  = name

p = Person("Bernaaaaaaa",1998)
print(p.name)

        