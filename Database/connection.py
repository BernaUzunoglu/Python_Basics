import mysql.connector

connection = mysql.connector.connect(
    host = "localhost" ,# server adresi yazılır.
    user ="root",
    password = "1234",
    database = "schooldb"
)