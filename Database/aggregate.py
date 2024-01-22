import mysql.connector

def getProductInfo():
    connection = mysql.connector.connect(
        host = "localhost" ,# server adresi yazılır.
        user ="root",
        password = "1234",
        database = "node-app"
    )
    cursor = connection.cursor()

    # sql = "Select COUNT(*) From Products " # result : 7 
    # sql = "Select COUNT(name) From Products"
    # sql = "Select AVG(Price) From Products" #result : 4661.4286
    # sql = "Select SUM(Price) From Products"
    # sql = "Select MIN(Price) From Products"
    # sql = "Select MAX(Price) From Products"
    sql = "Select Name  From Products Where Price = (Select MAX(Price) From Products) " #result : Samsung j8 Prime 

    cursor.execute(sql)
    result = cursor.fetchone()
    print(f"result : {result[0]} ")

getProductInfo()