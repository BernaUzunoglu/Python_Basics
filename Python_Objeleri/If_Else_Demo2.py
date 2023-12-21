
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

sayi = float(input('Sayı: '))

if (sayi > 0) and (sayi<=100):
    print('Sayı 0-100 arasında.')
else:
    print('Sayı 0-100 arasında değildir.')


# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

sayi = int(input('sayı: '))

if (sayi > 0):
    if (sayi % 2 ==0):
        print('Girilen sayı pozitif çift sayıdır.')
    else:
        print('Girilen sayı pozitif ancak sayı tek.')
else:
    print('Girilen sayı negatif sayıdır.')


# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 

email = 'bernauzunoglu58@gmail.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('password: ')

if (girilenEmail == email):
    if (girilenPassword == password): 
        print('Uygulamaya giriş başarılı.')
    else:
        print('Parolanız yanlış')
else:
    print('Email bilginiz yanlış')



# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if (a > b) and  (a > c):
    print(f'{a} en büyük sayıdır.')
elif (b > a) and (b > c):
    print(f'{b} en büyük sayıdır.')
elif (c > a) and (c > b):
    print(f'{c} en büyük sayıdır.')


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = float(input('Vize 1: '))
vize2 = float(input('Vize 2: '))
final = float(input('Final : '))

ortalama = ((vize1+vize2)/2) * 0.6 + (final * 0.4)

result = (ortalama >= 50) and (final >= 50)
result = (ortalama >= 50) or (final >= 70)

# ** durum-1

if (ortalama >= 50):
    if (final >= 50):  
        print(f'Öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
    else:
        print(f'Öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız. Finalden en az 50 almalısınız.')
else:
    print(f'Öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')

# ** durum-2

if (ortalama >= 50):
    print(f'Öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
else:
    if (final >= 70):
        print(f'Öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı. Finalden en az 70 aldığınız için geçtiniz.')
    else:
        print(f'Öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')




# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)



name = input('Adınız: ')
kg = float(input('Kilonuz: '))
hg = float(input('Boyunuz: '))

index = (kg) / (hg ** 2)

if (index >= 0) and (index <= 18.4):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf.')
elif (index > 18.4) and (index <= 24.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal.')
elif (index > 24.9) and (index <= 29.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu.')
elif (index >= 29.9) and (index <= 45.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez.')
else:
    print('bilgileriniz yanlış.')
