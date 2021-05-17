import pandas as pd
import numpy as np

def add_customers():
    from .connection import mydb, mycursor

    People = pd.read_csv("./db_initialization/RandomPeople.csv")

    for i in range(len(People)-20):
        first_name = People['firstname'][i].replace("'","")
        last_name = People['lastname'][i].replace("'","")
        id = People['ID_Number'][i]
        id_type = People['ID_Type'][i]
        id_issue = People['ID_Issue'][i]
        birth_date = People['birthdate'][i]
        
        sqlFormula = """INSERT INTO customers (first_name,last_name,birth_date,id,id_type,id_issue) 
                        VALUES ('{}','{}','{}',{},'{}','{}')""".format(first_name,last_name,birth_date,id,id_type,id_issue)
        mycursor.execute(sqlFormula)
        mydb.commit() 
        sqlFormula = """INSERT INTO customer_phones (NFC_ID,phone_number)
                        VALUES ({},{})""".format(i+1,People['phone'][i])
        mycursor.execute(sqlFormula)
        mydb.commit() 
        if i % 5 == 0:
            sqlFormula = """INSERT INTO customer_phones (NFC_ID,phone_number)
                    VALUES ({},{})""".format(i+1,People['phone2'][i])
            mycursor.execute(sqlFormula)
            mydb.commit() 

        
        sqlFormula = """INSERT INTO customer_emails (NFC_ID,email_address)
                        VALUES ({},'{}')""".format(i+1,People['email'][i].replace("'",""))
        mycursor.execute(sqlFormula)
        mydb.commit() 
        if i % 7 == 0:
            sqlFormula = """INSERT INTO customer_emails (NFC_ID,email_address)
                    VALUES ({},'{}')""".format(i+1,People['email2'][i].replace("'",""))
            mycursor.execute(sqlFormula)
            mydb.commit() 

