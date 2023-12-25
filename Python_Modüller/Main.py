import Mod 
'''aynı dizin içeriisnde olduğu için Mod modülünü bulup ekliyor eğer Python klasöründe lib 
içerisine eklenirse dizin içerisinde olmasa da import ile eklenebilir'''

# result = help(Mod)
# result = help(Mod.func)

result = Mod.number
print(result)
result = Mod.numbers
print(result)
result = Mod.person["name"]
print(result)
result = Mod.person['age']
print(result)
result = Mod.func(10)
print(result)

p = Mod.Person()
p.speak()