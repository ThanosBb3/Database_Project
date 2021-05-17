import numpy as np
import datetime
import random

def add_provide():
    from .connection import mydb, mycursor
    #Provide

    for i in range(400):
        sqlFormula = """INSERT INTO provide (AREA_ID, SERVICE_ID) 
                        VALUES ({},{})""".format(i+1,1)
        mycursor.execute(sqlFormula)
        mydb.commit()

    for i in range(446,450):
        sqlFormula = """INSERT INTO provide (AREA_ID, SERVICE_ID) 
                        VALUES ({},{})""".format(i,2)
        mycursor.execute(sqlFormula)
        mydb.commit()

    for i in range(436,446):
        sqlFormula = """INSERT INTO provide (AREA_ID, SERVICE_ID) 
                        VALUES ({},{})""".format(i,3)
        mycursor.execute(sqlFormula)
        mydb.commit()      

    for i in range(450,460):
        sqlFormula = """INSERT INTO provide (AREA_ID, SERVICE_ID) 
                        VALUES ({},{})""".format(i,4)
        mycursor.execute(sqlFormula)
        mydb.commit()

    sqlFormula = """INSERT INTO provide (AREA_ID, SERVICE_ID) 
                        VALUES ({},{})""".format(460,5)
    mycursor.execute(sqlFormula)
    mydb.commit()

    for i in range(426,432):
        sqlFormula = """INSERT INTO provide (AREA_ID, SERVICE_ID) 
                        VALUES ({},{})""".format(i,6)
        mycursor.execute(sqlFormula)
        mydb.commit()

    for i in range(432,436):
        sqlFormula = """INSERT INTO provide (AREA_ID, SERVICE_ID) 
                        VALUES ({},{})""".format(i,7)
        mycursor.execute(sqlFormula)
        mydb.commit()
        