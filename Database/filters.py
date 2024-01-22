import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "node-app"

)
cursor = connection.cursor()

def getProducts():
    cursor = connection.cursor()

    cursor.execute("Select * From Products Order By name, price")

    try:
        result = cursor.fetchall()    
        for product in result:
            print(f'id: {product[0]} name: {product[1]} price: {product[2]}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')


def getProductsById(id):
    sql = "Select * From Products Where id = %s"
    #cursor.execute("Select * From Products Where name LIKE '%Sam'")
    #cursor.execute("Select * From Products Where name LIKE '%Samsung%' and price = 3000")
    #cursor.execute("Select * From Products Where name LIKE '%Samsung%' or price >= 3000")
    # ---NOT : Parametre olarak tuple,dict veya list olmalı 
    params = (id,) # Virgül olunca demet-tuple tek elemanlı bir demet olduğunu ifade ediyor.

    cursor.execute(sql,params)
    result = cursor.fetchone()

    print(f'id : {result[0]} Name : {result[1]} Price : {result[2]}')

getProductsById(1)

def getProductsPrice(price):
    sql = "Select * From Products Where price = %s"
    params = (price,)
    cursor.execute(sql,params)
    result = cursor.fetchone()
    print(result)
getProductsPrice(2000)
getProducts()