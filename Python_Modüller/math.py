import math 

# value = dir(math)
# value = help(math.factorial)


value = math.sqrt(49)
print(value)
value = math.factorial(5)
print(value)
value = math.floor(6.4)
print(value)
value = math.floor(6.7) #aşağı yuvarlama
print(value)
value = math.ceil(6.4) # yukarı yuvarlama
print(value)

import math as islem # as ile takma isim verdik

value = islem.sqrt(64)
print(value)

from math import * # bu şekilde modülün adı kullanılmadan iöerisindeki tüm işlemleri import etmiş olduk. Direk kullanılabilir.

value = factorial(5)
print(value)

def sqrt(x):
    print('x : '+ str(x)) # eğer aynı isiimde bir fonk. tanımlandı ise python yorumlayıcı bir dil olduğu için en son eklenen çalışacaktır.

from math import sqrt,floor # bu şekilde sadece istenilen metodları eklendi.