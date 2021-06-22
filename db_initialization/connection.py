import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "*****",
        passwd = "******",
        database = "HotelDB"
    )

mycursor = mydb.cursor()