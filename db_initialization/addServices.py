import mysql.connector
import numpy as np
mydb = mysql.connector.connect(
    host = "localhost",
    user = "*****",
    passwd = "******",
    database = "HotelDB"
)

mycursor = mydb.cursor()

sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                VALUES ('{}','{}',{})""".format("Room","Renting Room for a given period of time",True)
mycursor.execute(sqlFormula)
mydb.commit()

sqlFormula = """INSERT INTO services_With_Register (SERVICE_ID) 
                VALUES ({})""".format(1)
mycursor.execute(sqlFormula)
mydb.commit()


sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                VALUES ('{}','{}',{})""".format("Gym","Gym subscription for a given period of time",True)
mycursor.execute(sqlFormula)
mydb.commit()

sqlFormula = """INSERT INTO services_With_Register (SERVICE_ID) 
                VALUES ({})""".format(2)
mycursor.execute(sqlFormula)
mydb.commit()


sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                VALUES ('{}','{}',{})""".format("Conference Room","Conference Room renting for a given period of time",True)
mycursor.execute(sqlFormula)
mydb.commit()

sqlFormula = """INSERT INTO services_With_Register (SERVICE_ID) 
                VALUES ({})""".format(3)
mycursor.execute(sqlFormula)
mydb.commit()


sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                VALUES ('{}','{}',{})""".format("Sauna","Sauna subscription for a given period of time",True)
mycursor.execute(sqlFormula)
mydb.commit()

sqlFormula = """INSERT INTO services_With_Register (SERVICE_ID) 
                VALUES ({})""".format(4)
mycursor.execute(sqlFormula)
mydb.commit()


sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                VALUES ('{}','{}',{})""".format("Hair Salon","Hair Styling at our Hair Salon",False)
mycursor.execute(sqlFormula)
mydb.commit()

sqlFormula = """INSERT INTO services_No_Register (SERVICE_ID) 
                VALUES ({})""".format(5)
mycursor.execute(sqlFormula)
mydb.commit()


sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                VALUES ('{}','{}',{})""".format("Bar","Drinks at the Bar",False)
mycursor.execute(sqlFormula)
mydb.commit()

sqlFormula = """INSERT INTO services_No_Register (SERVICE_ID) 
                VALUES ({})""".format(6)
mycursor.execute(sqlFormula)
mydb.commit()


sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                VALUES ('{}','{}',{})""".format("Restaurant","Dining at the Restaurant",False)
mycursor.execute(sqlFormula)
mydb.commit()

sqlFormula = """INSERT INTO services_No_Register (SERVICE_ID) 
                VALUES ({})""".format(7)
mycursor.execute(sqlFormula)
mydb.commit()
