username = 'bernauzunoglu'
password = '12345'

isLogin = (username == 'bernauzunoglu') and(password == '12345')

if isLogin:
    print('Hoş Geldiniz')
else:
    print('username yada parola yanlış')


if (username == 'bernauzunogluy'):
    if(password == '12345'):
        print('Hoş Geldiniz')
    else:
        print('Parolanız yanlış')
else:
    print('Kullamıcı adı yanlış')


    #if - elif komutu

    x = int(input ('x değerini giriniz : '))
    y = int(input ('y değerini giriniz : '))

    if x > y:
        print('X büyüktür y den')
    elif x == y :
        print('x eşittir y')
    else:
        print('y büyüktür x den')


    num = int(input(' sayı : '))

    if num < 0:
        print(f'{num} sayısı negatif bir sayıdır.')
    
    elif num > 0:
        print(f'{num} sayısı pozptpf bir sayısır')
    else:
        print(f'{num} sayısı 0 a eşittir.')