import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost" ,# server adresi yazılır.
    user ="root",
    password = "1234",
    database = "mydatabase"
)

mycursor = mydb.cursor()#bir veritabanı bağlantısı üzerinde SQL sorgularını çalıştırmak için bir "imleç" (cursor) nesnesi oluşturur. 
# mycursor.execute("CREATE DATABASE MyDatabase") # ben MyDatabase şeklinde versem de mydatabase ile küçük harflerle oluşturuluyor.
# mycursor.execute("SHOW DATABASES")
# for x in mycursor: 
#     print(x)
# mycursor.execute("CREATE TABLE Customers(Name VARCHAR(255), Address VARCHAR(255))") #Tablo ve database isimleri küçük harflerle oluşturuluyor
# print(mydb)