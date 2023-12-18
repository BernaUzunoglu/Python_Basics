website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result = len(course)
length = len(website)
print(result)
print(length)

# 2- 'website' içinden www karakterlerini alın.
result = website[7:10]
print(result)

# 3- 'website' içinden com karakterlerini alın.
result = website[22:25]
result = website[length-3:length]
print(result)

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result = course[0:15]
print(result)
result = course[:15]
print(result)
result = course[-15:]
print(result)

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result = course[::-1]
print(result)

name, surname, age, job = 'Berna','Uzunoglu', 25, 'Yazılım Mühendisi' 

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Berna Uzunoğlu, Yaşım 25 ve mesleğim Yazılım Mühendisi.' 

result = "Benim adım "+ name+ " " + surname+ ", Yaşım "+ str(age) + " ve mesleğim "+ job
print(result)
result = "Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.".format(name,surname,age,job) 
print(result)
result = f'Benim adım {name} {surname}, Yaşım {age} ve "mesleğim" {job}.'
print(result)

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s[0:6] + 'W'+ s[-4:]

print(s)
# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result = 'abc ' * 3

print(result)