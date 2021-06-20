import numpy as np
import datetime
import random

def add_register():
    from .connection import mydb, mycursor

    #Registers
    for i in range(180):

        #arrival = f"2021-5-{15+i//36} {9+4*((i%36)//12)}:00:00"
        arrival = (datetime.datetime.now()-datetime.timedelta(days=(44*7+1)-22*(i//12))).strftime("%Y-%m-%d %H:%M:%S")

        sqlFormula = """INSERT INTO register (NFC_ID,SERVICE_ID,date_time) 
                        VALUES ({},{},'{}')""".format(i+1,1,arrival)
        mycursor.execute(sqlFormula)
        mydb.commit()

        sqlFormula = """INSERT INTO useService (NFC_ID,SERVICE_ID,date_time,cost) 
                        VALUES ({},{},'{}',{})""".format(i+1,1,arrival,90)
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

