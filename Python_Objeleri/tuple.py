#tuple ve  list aynı mantık ile kullanılıyor fakat tuple içindeki elemanlar değiştşriliemez.
 
list = [1,2,3]
tuple = (1,'iki',3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))

list = ['Ali', 'Veli']
tuple = ('Ayşe', 'Damla', 'Ayşe') # yeni bir tuple tanımladık

list[0] = 'Berna'
# tuple[0] = 'Lina'  #hata veriri support item assigment atama yapılamaz

print(tuple.count('Ayşe'))
print(tuple.index('Ayşe'))
print(list)
print(tuple)