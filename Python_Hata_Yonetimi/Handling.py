#error handling = > Hata yönetimi

'''Normalde sıfıra bölünemez hatası vermesi gerekirken try - except ile programda verilen hatayı yönettik.'''

try:
    x = int(input('x : '))
    y = int(input('y : '))
    print(x/y)

except ZeroDivisionError: # sıfıra bölme hatası 
    print('y için 0 girilemez')
except ValueError as e : #hatayı e adında bir objede tutyoruz
    print('X ve Y için sayısal değer girmeniz gerekli')
    print(e)

while True: #hata varsa kullanıcıya gösterir yoksa devam eder
    try:
        x = int(input('x : '))
        y = int(input('y : '))
        print(x/y)

    except Exception as ex : # sıfıra bölme hatası 
        print('y için 0 girilemez',ex)
    except ValueError as e : #hatayı e adında bir objede tutyoruz
        print('X ve Y için sayısal değer girmeniz gerekli')
        print(e)

    else:
        break

    finally:
        #dosya açtın kapat vs gibi sonlanması gereken işlemleri burda sonlandırıyoruz.
        print('Try-except sonlandı')



