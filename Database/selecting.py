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
    except mysql.connector.Error as err:
        print('Hata : ',err)
    finally:
        connection.close()
        print('Database bağlantısı kapatıldı.')


def getProducts():
    try:
        connection = mysql.connector.connect(
            host = "localhost" ,# server adresi yazılır.
            user ="root",
            password = "1234",
            database = "node-app"
        )
        cursor = connection.cursor()
        # cursor.execute('Select * from Products')
        cursor.execute('Select name,price from Products')
        result = cursor.fetchall() # birden fazla kayıt alınca fetchall
        #result = cursor.fetchone() # bulduğu ilk kaydı getirir
        # print(result)
        for product in result:
            # print(product)
            # print(f'Name:{product[1]} Price : {product[2]}')# Select * From olunca
            print(f'Name:{product[0]} Price : {product[1]}')
    except mysql.connector.Error as err:
        print(f"Hata: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

getProducts()