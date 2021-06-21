
def add_areas():
    from .connection import mydb, mycursor

    orientations = ['N', 'W', 'E', 'S', 'NE', 'NW', 'SE', 'SW']

    for i in range(400):
        area_name = f"Room{i+1}"
        if i%60 < 20:
            beds = 1
        elif i%60 < 40:
            beds = 2
        else:
            beds = 3       
        area_floor = ((i%20)//4) + 1
        orientation = orientations[(i%4)]
        info = f"Room{i+1} with {beds} beds on floor {area_floor}"
        sqlFormula = """INSERT INTO areas (area_name,beds,area_floor,orientation,info) 
                        VALUES ('{}',{},{},'{}','{}')""".format(area_name,beds,area_floor,orientation,info)
        mycursor.execute(sqlFormula)
        mydb.commit()


    for i in range(20):
        area_name = f"Hall{i+1}"
        beds = 0
        area_floor = i//4 + 1
        orientation = orientations[i%4]
        info = f"Hall{i+1} on floor {area_floor} with {orientation} orientation"
        sqlFormula = """INSERT INTO areas (area_name,beds,area_floor,orientation,info) 
                        VALUES ('{}',{},{},'{}','{}')""".format(area_name,beds,area_floor,orientation,info)
        mycursor.execute(sqlFormula)
        mydb.commit()


    for i in range(5):
        area_name = f"Elevator{i+1}"
        beds = 0
        area_floor = 0
        sqlFormula = """INSERT INTO areas (area_name,beds,area_floor) 
                        VALUES ('{}',{},{})""".format(area_name,beds,area_floor)
        mycursor.execute(sqlFormula)
        mydb.commit()


    for i in range(6):
        area_name = f"Bar{i+1}"
        beds = 0
        area_floor = 0
        orientation = orientations[i]
        info = f"Bar{i+1} on ground floor with {orientation} orientation"
        sqlFormula = """INSERT INTO areas (area_name,beds,area_floor,orientation,info) 
                        VALUES ('{}',{},{},'{}','{}')""".format(area_name,beds,area_floor,orientation,info)
        mycursor.execute(sqlFormula)
        mydb.commit()


    for i in range(4):
        area_name = f"Restaurant{i+1}"
        beds = 0
        area_floor = 0
        orientation = orientations[i]
        info = f"Restaurant{i+1} on ground floor with {orientation} orientation"
        sqlFormula = """INSERT INTO areas (area_name,beds,area_floor,orientation,info) 
                        VALUES ('{}',{},{},'{}','{}')""".format(area_name,beds,area_floor,orientation,info)
        mycursor.execute(sqlFormula)
        mydb.commit()


    for i in range(10):
        area_name = f"Conference Room{i+1}"
        beds = 0
        area_floor = 0
        orientation = orientations[i%8]
        info = f"Conference Room{i+1} on ground floor with {orientation} orientation"
        sqlFormula = """INSERT INTO areas (area_name,beds,area_floor,orientation,info) 
                        VALUES ('{}',{},{},'{}','{}')""".format(area_name,beds,area_floor,orientation,info)
        mycursor.execute(sqlFormula)
        mydb.commit()


    for i in range(4):
        area_name = f"Gym{i+1}"
        beds = 0
        area_floor = 0
        orientation = orientations[7-i]
        info = f"Gym{i+1} on ground floor with {orientation} orientation"
        sqlFormula = """INSERT INTO areas (area_name,beds,area_floor,orientation,info) 
                        VALUES ('{}',{},{},'{}','{}')""".format(area_name,beds,area_floor,orientation,info)
        mycursor.execute(sqlFormula)
        mydb.commit()


    for i in range(10):
        area_name = f"Sauna{i+1}"
        beds = 0
        area_floor = 0
        orientation = orientations[i%8]
        info = f"Sauna{i+1} on ground floor with {orientation} orientation"
        sqlFormula = """INSERT INTO areas (area_name,beds,area_floor,orientation,info) 
                        VALUES ('{}',{},{},'{}','{}')""".format(area_name,beds,area_floor,orientation,info)
        mycursor.execute(sqlFormula)
        mydb.commit()


    sqlFormula = """INSERT INTO areas (area_name,beds,area_floor,orientation,info) 
                    VALUES ('{}',{},{},'{}','{}')""".format("Hair Salon",0,0,'W',"Hair Salon on ground floor with W orientation")
    mycursor.execute(sqlFormula)
    mydb.commit()

    sqlFormula = """INSERT INTO areas (area_name,beds,area_floor,orientation,info) 
                    VALUES ('{}',{},{},'{}','{}')""".format("Lobby",0,0,'S',"Lobby on ground floor with S orientation")
    mycursor.execute(sqlFormula)
    mydb.commit()
