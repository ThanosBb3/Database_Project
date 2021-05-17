import mysql.connector
import numpy as np
import datetime
import random

mydb = mysql.connector.connect(
    host = "localhost",
    user = "*****",
    passwd = "*****",
    database = "HotelDB"
)

mycursor = mydb.cursor()

#Registers

for i in range(180):

    arrival = f"2021-5-{15+i//36} {9+4*((i%36)//12)}:00:00"

    sqlFormula = """INSERT INTO register (NFC_ID,SERVICE_ID,date_time) 
                    VALUES ({},{},'{}')""".format(i+1,1,arrival)
    mycursor.execute(sqlFormula)
    mydb.commit()


    if i%4==0:
        sqlFormula = """INSERT INTO register (NFC_ID,SERVICE_ID,date_time) 
                        VALUES ({},{},'{}')""".format(i+1,2,arrival)
        mycursor.execute(sqlFormula)
        mydb.commit()

    if i%9==0:
        sqlFormula = """INSERT INTO register (NFC_ID,SERVICE_ID,date_time) 
                        VALUES ({},{},'{}')""".format(i+1,4,arrival)
        mycursor.execute(sqlFormula)
        mydb.commit()

    if i%15==0:
        sqlFormula = """INSERT INTO register (NFC_ID,SERVICE_ID,date_time) 
                        VALUES ({},{},'{}')""".format(i+1,3,arrival)
        mycursor.execute(sqlFormula)
        mydb.commit()

#haveAccess

j=0
for i in range(100):

    arrival = f"2021-5-{15+j//36} {9+4*((j%36)//12)}:00:00"
    leave = f"2021-5-{15+j//36+random.randint(3,7)} 13:00:00"

    if i < 20 or (i > 59 and i <80):
        sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                        VALUES ({},{},'{}','{}')""".format(j+1,i+1,arrival,leave)
        mycursor.execute(sqlFormula)
        mydb.commit()

        if j%4==0:
            for l in range(446,450):
                sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                VALUES ({},{},'{}','{}')""".format(j+1,l,arrival,leave)
                mycursor.execute(sqlFormula)
                mydb.commit()

        if j%9==0:
            for l in range(450,460):
                sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                VALUES ({},{},'{}','{}')""".format(j+1,l,arrival,leave)
                mycursor.execute(sqlFormula)
                mydb.commit()

        if j%15==0:
            for l in range(436,446):
                sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                VALUES ({},{},'{}','{}')""".format(j+1,l,arrival,leave)
                mycursor.execute(sqlFormula)
                mydb.commit()
        j = j+1
    elif (i >= 20 and i < 40) or (i >=80 and i < 100):
        for l in range(2):
            sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                            VALUES ({},{},'{}','{}')""".format(j+1,i+1,arrival,leave)
            mycursor.execute(sqlFormula)
            mydb.commit()
            if j%4==0:
                for l in range(446,450):
                    sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                    VALUES ({},{},'{}','{}')""".format(j+1,l,arrival,leave)
                    mycursor.execute(sqlFormula)
                    mydb.commit()

            if j%9==0:
                for l in range(450,460):
                    sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                    VALUES ({},{},'{}','{}')""".format(j+1,l,arrival,leave)
                    mycursor.execute(sqlFormula)
                    mydb.commit()

            if j%15==0:
                for l in range(436,446):
                    sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                    VALUES ({},{},'{}','{}')""".format(j+1,l,arrival,leave)
                    mycursor.execute(sqlFormula)
                    mydb.commit()
            j = j+1
    else:
        for l in range(3):
            sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                            VALUES ({},{},'{}','{}')""".format(j+1,i+1,arrival,leave)
            mycursor.execute(sqlFormula)
            mydb.commit()
            if j%4==0:
                for l in range(446,450):
                    sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                    VALUES ({},{},'{}','{}')""".format(j+1,l,arrival,leave)
                    mycursor.execute(sqlFormula)
                    mydb.commit()

            if j%9==0:
                for l in range(450,460):
                    sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                    VALUES ({},{},'{}','{}')""".format(j+1,l,arrival,leave)
                    mycursor.execute(sqlFormula)
                    mydb.commit()

            if j%15==0:
                for l in range(436,446):
                    sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                    VALUES ({},{},'{}','{}')""".format(j+1,l,arrival,leave)
                    mycursor.execute(sqlFormula)
                    mydb.commit()
            j = j+1       



