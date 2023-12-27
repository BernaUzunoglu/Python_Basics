# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("hello", name)

# sayHello("ali")
import math
import time

#Decorator func
def calculate_time(func):
    def inner(*args,**kwargs):#keywordergs        
        start = time.time()# ne kadar sürede işlem yaptı
        time.sleep(1) # bir saniye uyut-bekle
        func(*args,**kwargs)        
        finish = time.time()
        print("fonksiyon "+func.__name__ +" " + str(finish-start) + " saniye sürdü.")
    return inner

@calculate_time # zaman hesaplama decoratorünü çağırdık. tekrarlayan kod blokklaı olmadı
def usalma(a,b):
    print(math.pow(a,b))   

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(4)
toplama(10,20)
