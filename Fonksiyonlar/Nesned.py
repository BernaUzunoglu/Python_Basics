# İç içe fonksiyonlar

# def greeting(name):
#     print('Hello',name)


# sayHello = greeting
# print(sayHello) # 0x00000199C0A28A40
# print(greeting) #0x00000199C0A28A40

# del sayHello
# print(greeting)#0x00000199C0A28A40

#encapsulation 
def outher(num1):
    print('outer')
    def inner_increment(num1):
         print('inner')
         return num1 + 1
    num2 = inner_increment(num1)
    print(num1)
    print(num2)

outher(10)
#inner_increment(10) # 'inner_increment' is not defined hatası alırız çünkü fonk. dışardan erişilemez encapsulation fonk scope içerinde tanımlı

def factorial(number):
     if not isinstance(number,int): # bu fonksiyon verilen değerin ikinci parametredeki tipe uyup uymadığını kontrol ediyor.
          raise TypeError("Number must be an integer")
     if not number >= 0:
          raise ValueError("Number must be an integer")
     
     def inner_factorial(number):
          if number <= 1:
               return 1
          print(number)
          return number * inner_factorial(number - 1)
     return inner_factorial(number)

try:
     print(factorial("4"))
except Exception as ex:
     print(ex)

print(factorial(-5))