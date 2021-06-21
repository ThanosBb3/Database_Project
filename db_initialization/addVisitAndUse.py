import numpy as np
import datetime
import random

def add_visit_use():
    from .connection import mydb, mycursor
    # Visit

    for i in range(180):

        entry = datetime.datetime.now()-datetime.timedelta(days=(44*7+1)-22*(i//12))
        arrival = entry.strftime("%Y-%m-%d %H:%M:%S")

        exit = entry+datetime.timedelta(days=3)
        leave = (entry+datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")

        start = entry
        finish = min(exit, datetime.datetime.now())

        while start < finish:
            
            #endtask = start + datetime.timedelta(minutes=random.randint(10,120))

            x = random.randint(1,100)
            if x <= 60:
                area = np.random.choice(['Hall', 'Elevator', 'Lobby'])
                endtask = start + datetime.timedelta(minutes=random.randint(2,8))
                if endtask < finish:
                    if area=='Hall':
                        sqlFormula = """INSERT INTO visit (NFC_ID,AREA_ID,enter_datetime,leave_datetime) 
                                        VALUES ({},(SELECT AREA_ID FROM haveAccess WHERE (NFC_ID={} AND AREA_ID>400 AND AREA_ID<421)),'{}','{}')""".format(i+1,i+1,start.strftime("%Y-%m-%d %H:%M:%S"),endtask.strftime("%Y-%m-%d %H:%M:%S"))
                        mycursor.execute(sqlFormula)
                        mydb.commit()
                        start = endtask

                    elif area=='Elevator':
                        sqlFormula = """INSERT INTO visit (NFC_ID,AREA_ID,enter_datetime,leave_datetime) 
                                        VALUES ({},{},'{}','{}')""".format(i+1,random.randint(421,425),start.strftime("%Y-%m-%d %H:%M:%S"),endtask.strftime("%Y-%m-%d %H:%M:%S"))
                        mycursor.execute(sqlFormula)
                        mydb.commit()
                        start = endtask
                    else:
                        sqlFormula = """INSERT INTO visit (NFC_ID,AREA_ID,enter_datetime,leave_datetime) 
                                        VALUES ({},{},'{}','{}')""".format(i+1,461,start.strftime("%Y-%m-%d %H:%M:%S"),endtask.strftime("%Y-%m-%d %H:%M:%S"))
                        mycursor.execute(sqlFormula)
                        mydb.commit()
                        start = endtask + datetime.timedelta(hours=random.randint(6,12))

            elif x>85:
                area = np.random.choice(['Bar', 'Bar', 'Bar', 'Restaurant', 'Restaurant', 'Restaurant','Restaurant', 'HairSalon'])
                endtask = start + datetime.timedelta(hours=random.randint(1,3))
                if endtask < finish:
                    if area=='Bar':
                        sqlFormula = """INSERT INTO visit (NFC_ID,AREA_ID,enter_datetime,leave_datetime) 
                                        VALUES ({},{},'{}','{}')""".format(i+1,random.randint(426,431),start.strftime("%Y-%m-%d %H:%M:%S"),endtask.strftime("%Y-%m-%d %H:%M:%S"))
                        mycursor.execute(sqlFormula)
                        mydb.commit()

                        sqlFormula = """INSERT INTO useService (NFC_ID,SERVICE_ID,date_time,cost) 
                                        VALUES ({},{},'{}',{})""".format(i+1,6,(endtask-datetime.timedelta(minutes=random.randint(5,15))).strftime("%Y-%m-%d %H:%M:%S"),round(random.uniform(8,50),2))
                        mycursor.execute(sqlFormula)
                        mydb.commit()

                    elif area=='Restaurant':
                        sqlFormula = """INSERT INTO visit (NFC_ID,AREA_ID,enter_datetime,leave_datetime) 
                                        VALUES ({},{},'{}','{}')""".format(i+1,random.randint(432,435),start.strftime("%Y-%m-%d %H:%M:%S"),endtask.strftime("%Y-%m-%d %H:%M:%S"))
                        mycursor.execute(sqlFormula)
                        mydb.commit()

                        sqlFormula = """INSERT INTO useService (NFC_ID,SERVICE_ID,date_time,cost) 
                                        VALUES ({},{},'{}',{})""".format(i+1,7,(endtask-datetime.timedelta(minutes=random.randint(5,15))).strftime("%Y-%m-%d %H:%M:%S"),round(random.uniform(20,45),2))
                        mycursor.execute(sqlFormula)
                        mydb.commit()

                    else:
                        sqlFormula = """INSERT INTO visit (NFC_ID,AREA_ID,enter_datetime,leave_datetime) 
                                        VALUES ({},{},'{}','{}')""".format(i+1,460,start.strftime("%Y-%m-%d %H:%M:%S"),endtask.strftime("%Y-%m-%d %H:%M:%S"))
                        mycursor.execute(sqlFormula)
                        mydb.commit() 

                        sqlFormula = """INSERT INTO useService (NFC_ID,SERVICE_ID,date_time,cost) 
                                        VALUES ({},{},'{}',{})""".format(i+1,5,(endtask-datetime.timedelta(minutes=random.randint(5,15))).strftime("%Y-%m-%d %H:%M:%S"),round(random.uniform(15,60),2))
                        mycursor.execute(sqlFormula)
                        mydb.commit()

                start = endtask
            else:
                sqlFormula = """SELECT AREA_ID FROM haveAccess WHERE NFC_ID={} AND (AREA_ID<401 OR AREA_ID>420)""".format(i+1)
                mycursor.execute(sqlFormula)

                rooms = [item[0] for item in mycursor.fetchall()]

                area_id = np.random.choice(rooms)
                if area_id<401:
                    endtask = start + datetime.timedelta(hours=random.randint(4,9))
                else:
                    endtask = start + datetime.timedelta(hours=random.randint(1,4))
                if endtask<finish:
                    sqlFormula = """INSERT INTO visit (NFC_ID,AREA_ID,enter_datetime,leave_datetime) 
                                    VALUES ({},{},'{}','{}')""".format(i+1,area_id,start.strftime("%Y-%m-%d %H:%M:%S"),endtask.strftime("%Y-%m-%d %H:%M:%S"))
                    mycursor.execute(sqlFormula)
                    mydb.commit()

                if area_id in range(446,450):
                    sqlFormula = """INSERT INTO useService (NFC_ID,SERVICE_ID,date_time,cost) 
                                    VALUES ({},{},'{}',{})""".format(i+1,2,(endtask-datetime.timedelta(minutes=random.randint(5,15))).strftime("%Y-%m-%d %H:%M:%S"),round(random.uniform(6,15),2))
                    mycursor.execute(sqlFormula)
                    mydb.commit()

                elif area_id in range(436,446):
                    sqlFormula = """INSERT INTO useService (NFC_ID,SERVICE_ID,date_time,cost) 
                                    VALUES ({},{},'{}',{})""".format(i+1,3,(endtask-datetime.timedelta(minutes=random.randint(5,15))).strftime("%Y-%m-%d %H:%M:%S"),round(random.uniform(15,30),2))
                    mycursor.execute(sqlFormula)
                    mydb.commit()

                elif area_id in range(450,460):
                    sqlFormula = """INSERT INTO useService (NFC_ID,SERVICE_ID,date_time,cost) 
                                    VALUES ({},{},'{}',{})""".format(i+1,4,(endtask-datetime.timedelta(minutes=random.randint(5,15))).strftime("%Y-%m-%d %H:%M:%S"),round(random.uniform(5,15),2))
                    mycursor.execute(sqlFormula)
                    mydb.commit()

                start = endtask    





