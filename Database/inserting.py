import mysql.connector

def insertProduct(name,price,imageUrl,description):
    connection = mysql.connector.connect(
         host = "localhost" ,# server adresi yazılır.
        user ="root",
        password = "1234",
        database = "node-app"
    )
    cursor = connection.cursor()
    sql = "INSERT INTO Products (Name,Price,imageUrl,Description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)
    cursor.execute(sql,values)
    try:
        connection.commit()#database gönderme işlemi
        print(f'{cursor.rowcount} tane kayıt eklendi') # rowcount ile kaç kayıt eklendiğini
        print(f'son eklenen kaydın id: {cursor.lastrowid}')# don id yi alıyoruz
    except mysql.connection.Error as err:
        print('Hata : ',err)
    finally:
        connection.close()
        print('Database bağlantısı kapatıldı.')



def insertProducts(list):
    connection = mysql.connector.connect(
         host = "localhost" ,# server adresi yazılır.
        user ="root",
        password = "1234",
        database = "node-app"
    )
    cursor = connection.cursor()
    sql = "INSERT INTO Products (Name,Price,imageUrl,Description) VALUES (%s,%s,%s,%s)"
    values = list
    cursor.executemany(sql,values) # çoğul bir ekleme  işlemi yapıyoruz
    try:
        connection.commit()#database gönderme işlemi
        print(f'{cursor.rowcount} tane kayıt eklendi') # rowcount ile kaç kayıt eklendiğini
        print(f'son eklenen kaydın id: {cursor.lastrowid}')# don id yi alıyoruz
    except mysql.connection.Error as err:
        print('Hata : ',err)
    finally:
        connection.close()
        print('Database bağlantısı kapatıldı.')

list = []
while True:
    name = input("Ürün Adı : ")
    price = float(input("Ürün Fiyatı : "))
    imageUrl = input("Ürün Resmi : ")
    description = input("Ürün Tanımı : ")

    list.append((name, price, imageUrl, description)) #  tuple listesi şeklinde ekliyoruz.Tuple içindeki elemanlar değiştşriliemez
    result = input('Devam etmek istiyor musunuz? (E/H)')
    if result == "H" or result == "h":
        print('Kayıtlarınız veritabanına aktarılıyor...')
        print(list)
        #kayıt
        insertProducts(list)
        break
    

# insertProduct(name,price,imageUrl,description)
