import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "Thanos",
        passwd = "thanos21",
        database = "HotelDB"
    )

mycursor = mydb.cursor()