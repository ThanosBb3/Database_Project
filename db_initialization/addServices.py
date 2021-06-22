
def add_services():
    from .connection import mydb, mycursor


    sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                    VALUES ('{}','{}',{})""".format("Room","Renting Room for a given period of time",True)
    mycursor.execute(sqlFormula)
    mydb.commit()


    sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                    VALUES ('{}','{}',{})""".format("Gym","Gym subscription for a given period of time",True)
    mycursor.execute(sqlFormula)
    mydb.commit()


    sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                    VALUES ('{}','{}',{})""".format("Conference Room","Conference Room renting for a given period of time",True)
    mycursor.execute(sqlFormula)
    mydb.commit()


    sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                    VALUES ('{}','{}',{})""".format("Sauna","Sauna subscription for a given period of time",True)
    mycursor.execute(sqlFormula)
    mydb.commit()


    sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                    VALUES ('{}','{}',{})""".format("Hair Salon","Hair Styling at our Hair Salon",False)
    mycursor.execute(sqlFormula)
    mydb.commit()


    sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                    VALUES ('{}','{}',{})""".format("Bar","Drinks at the Bar",False)
    mycursor.execute(sqlFormula)
    mydb.commit()


    sqlFormula = """INSERT INTO services (category,service_description,register_required) 
                    VALUES ('{}','{}',{})""".format("Restaurant","Dining at the Restaurant",False)
    mycursor.execute(sqlFormula)
    mydb.commit()

