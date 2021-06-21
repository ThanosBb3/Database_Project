import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "boftonelly",
        database = "HotelDB"
    )

mycursor = mydb.cursor()