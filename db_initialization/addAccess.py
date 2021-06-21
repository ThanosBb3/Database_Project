import datetime
import random

def add_access():
    from .connection import mydb, mycursor
    #haveAccess

    j=0
    for i in range(100):

        #arrival = f"2021-5-{15+j//36} {9+4*((j%36)//12)}:00:00"
        #leave = f"2021-5-{15+j//36+random.randint(3,7)} 13:00:00"

        entry = datetime.datetime.now()-datetime.timedelta(days=(((44*7)+1)-22*(j//12)))
        arrival = entry.strftime("%Y-%m-%d %H:%M:%S")
        leave = (entry+datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")

        if i < 20 or (i > 59 and i <80):
            sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                            VALUES ({},{},'{}','{}')""".format(j+1,i+1,arrival,leave)
            mycursor.execute(sqlFormula)
            mydb.commit()

            sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                            VALUES ({},(SELECT AREA_ID FROM areas WHERE area_floor=(SELECT area_floor FROM areas WHERE AREA_ID={}) AND
                            orientation=(SELECT orientation FROM areas WHERE AREA_ID={}) AND beds=0),'{}','{}')""".format(j+1,i+1,i+1,arrival,leave)
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
            for k in range(2):
                sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                VALUES ({},{},'{}','{}')""".format(j+1,i+1,arrival,leave)
                mycursor.execute(sqlFormula)
                mydb.commit()

                sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                VALUES ({},(SELECT AREA_ID FROM areas WHERE area_floor=(SELECT area_floor FROM areas WHERE AREA_ID={}) AND
                                orientation=(SELECT orientation FROM areas WHERE AREA_ID={}) AND beds=0),'{}','{}')""".format(j+1,i+1,i+1,arrival,leave)
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
            for k in range(3):
                sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                VALUES ({},{},'{}','{}')""".format(j+1,i+1,arrival,leave)
                mycursor.execute(sqlFormula)
                mydb.commit()

                sqlFormula = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                VALUES ({},(SELECT AREA_ID FROM areas WHERE (area_floor=(SELECT area_floor FROM areas WHERE AREA_ID={}) AND
                                orientation=(SELECT orientation FROM areas WHERE AREA_ID={})) AND beds=0),'{}','{}')""".format(j+1,i+1,i+1,arrival,leave)
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