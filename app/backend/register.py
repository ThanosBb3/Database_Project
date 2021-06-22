from flask import Blueprint, render_template, request, flash
from flask_mysqldb import MySQL
import mysql.connector as ddb
import datetime

register = Blueprint('register', __name__)

@register.route('/register', methods=['GET', 'POST'])
def register_fun():
    status=200

    mydb = ddb.connect(
        host = "localhost",
        user = "Thanos",
        passwd = "thanos21",
        database = "HotelDB"
    )

    cur = mydb.cursor()
    cur2 = mydb.cursor()
    cur3 = mydb.cursor()
    cur4 = mydb.cursor()
    cur5 = mydb.cursor()
    cur6 = mydb.cursor()
    cur7 = mydb.cursor()

    availables = """ SELECT C.area_name FROM areas C WHERE  C.AREA_ID<401 AND ((SELECT COUNT(B.NFC_ID) FROM haveAccess B WHERE B.AREA_ID=C.AREA_ID AND B.end_datetime>'{}') < C.beds)""".format(datetime.datetime.now())
    cur3.execute(availables)
    av_rooms = cur3.fetchall()

    taken = """ SELECT M.area_name FROM areas M WHERE M.AREA_ID<401 AND M.area_name NOT IN (SELECT C.area_name FROM areas C WHERE  C.AREA_ID<401 AND ((SELECT COUNT(B.NFC_ID) FROM haveAccess B WHERE B.AREA_ID=C.AREA_ID AND B.end_datetime>'{}') < C.beds))""".format(datetime.datetime.now())
    cur6.execute(taken)
    tk_rooms = cur6.fetchall()


    if request.method == 'POST':

        nfc_id = request.form.get('NFC_ID')
        service_name = request.form.get('service_name')
        room = request.form.get('room')
        room2 = request.form.get('room2')
        days1 = request.form.get('days')
        

        if request.form.get("register"):

            my_query1 = """SELECT MAX(NFC_ID) FROM customers;"""

            print(my_query1)
            cur.execute(my_query1)
            result = cur.fetchall()

            if not (nfc_id and service_name):
                flash('Please input an NFC_ID and a provided service', category="error")
                status=400
                return render_template("register.html", x=av_rooms, y=tk_rooms)

            elif (not nfc_id.isnumeric()) or (not days1.isnumeric()):
                flash('Please insert a valid NFC_ID and days duration', category="error")
                status=400
                return render_template("register.html", x=av_rooms, y=tk_rooms)

            elif int(nfc_id)<1 or int(nfc_id)>result[0][0]:
                flash('Please insert a valid NFC_ID', category="error")
                status=400
                return render_template("register.html", x=av_rooms, y=tk_rooms)        

            else:

                query22 = """SELECT EXISTS (SELECT * FROM register WHERE NFC_ID={} AND SERVICE_ID=(SELECT SERVICE_ID FROM services WHERE category='{}'));
                 """.format(nfc_id, service_name)
                print(query22)
                cur5.execute(query22)
                check = cur5.fetchall() 

                if check[0][0]==True:
                    flash('Customer with NFC ID {} is already registered at {}!'.format(nfc_id, service_name), category="error")
                    return render_template("register.html", x=av_rooms, y=tk_rooms)

                else:
                    if service_name=="Room":
                        my_query2 = """INSERT INTO register(NFC_ID, SERVICE_ID, date_time)
                                    VALUES ({}, 1, '{}');
                            """.format(nfc_id, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                        print(my_query2)
                        cur.execute(my_query2)
                        mydb.commit()

                        my_query3 = """INSERT INTO haveAccess(NFC_ID, AREA_ID, start_datetime, end_datetime)
                                    VALUES ({}, (SELECT AREA_ID FROM areas WHERE area_name='{}'), '{}', '{}');
                            """.format(nfc_id, room, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (datetime.datetime.now()+datetime.timedelta(days=int(days1))).strftime("%Y-%m-%d %H:%M:%S"))

                        print(my_query3)
                        cur.execute(my_query3)
                        mydb.commit()

                        my_query4 = """INSERT INTO useService(NFC_ID, SERVICE_ID, date_time, cost)
                                    VALUES ({}, 1, '{}', {});
                            """.format(nfc_id, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 30*int(days1))

                        print(my_query4)
                        cur.execute(my_query4)
                        mydb.commit()

                        for i in range(421,436):
                            my_query5 = """INSERT INTO haveAccess(NFC_ID, AREA_ID, start_datetime, end_datetime)
                                    VALUES ({}, {}, '{}', '{}');
                            """.format(nfc_id, i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (datetime.datetime.now()+datetime.timedelta(days=int(days1))).strftime("%Y-%m-%d %H:%M:%S"))

                            print(my_query5)
                            cur.execute(my_query5)
                            mydb.commit()

                        my_query6 = """INSERT INTO haveAccess(NFC_ID, AREA_ID, start_datetime, end_datetime)
                                    VALUES ({}, 460, '{}', '{}');
                            """.format(nfc_id, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (datetime.datetime.now()+datetime.timedelta(days=int(days1))).strftime("%Y-%m-%d %H:%M:%S"))

                        print(my_query6)
                        cur.execute(my_query6)
                        mydb.commit()

                        my_query6 = """INSERT INTO haveAccess(NFC_ID, AREA_ID, start_datetime, end_datetime)
                                    VALUES ({}, 461, '{}', '{}');
                            """.format(nfc_id, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (datetime.datetime.now()+datetime.timedelta(days=int(days1))).strftime("%Y-%m-%d %H:%M:%S"))

                        print(my_query6)
                        cur.execute(my_query6)
                        mydb.commit()

                        my_query7 = """INSERT INTO haveAccess (NFC_ID,AREA_ID,start_datetime,end_datetime) 
                                VALUES ({},(SELECT AREA_ID FROM areas WHERE area_floor=(SELECT area_floor FROM areas WHERE AREA_ID=(SELECT AREA_ID FROM areas WHERE area_name='{}')) AND
                                orientation=(SELECT orientation FROM areas WHERE AREA_ID=(SELECT AREA_ID FROM areas WHERE area_name='{}')) AND beds=0),'{}','{}')""".format(nfc_id,room,room,datetime.datetime.now(), (datetime.datetime.now()+datetime.timedelta(days=int(days1))).strftime("%Y-%m-%d %H:%M:%S"))
                        print(my_query7)
                        cur.execute(my_query7)
                        mydb.commit()

                        availables = """ SELECT C.area_name FROM areas C WHERE  C.AREA_ID<401 AND ((SELECT COUNT(B.NFC_ID) FROM haveAccess B WHERE B.AREA_ID=C.AREA_ID AND B.end_datetime>'{}') < C.beds)""".format(datetime.datetime.now())
                        cur4.execute(availables)
                        av_rooms = cur4.fetchall()

                        taken = """ SELECT M.area_name FROM areas M WHERE M.AREA_ID<401 AND M.area_name NOT IN (SELECT C.area_name FROM areas C WHERE  C.AREA_ID<401 AND ((SELECT COUNT(B.NFC_ID) FROM haveAccess B WHERE B.AREA_ID=C.AREA_ID AND B.end_datetime>'{}') < C.beds))""".format(datetime.datetime.now())
                        cur7.execute(taken)
                        tk_rooms = cur7.fetchall()


                        flash('Customer with NFC ID {} renting {}!'.format(nfc_id, room))
                        return render_template("register.html", x=av_rooms, y=tk_rooms)

                    else:    


                        my_query2 = """INSERT INTO register(NFC_ID, SERVICE_ID, date_time)
                                    VALUES ({}, (SELECT SERVICE_ID FROM services WHERE category='{}'), '{}');
                            """.format(nfc_id, service_name, datetime.datetime.now())

                        print(my_query2)
                        cur.execute(my_query2)
                        mydb.commit()    

                        my_query11 = """SELECT AREA_ID FROM provide WHERE SERVICE_ID=(SELECT SERVICE_ID FROM services WHERE category='{}');""".format(service_name)

                        print(my_query11)
                        cur2.execute(my_query11)
                        result1 = cur2.fetchall()

                        for item in result1:
                            my_query2 = """INSERT INTO haveAccess(NFC_ID, AREA_ID, start_datetime, end_datetime)
                                    VALUES ({}, {}, '{}', '{}');
                            """.format(nfc_id, item[0], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (datetime.datetime.now()+datetime.timedelta(days=int(days1))).strftime("%Y-%m-%d %H:%M:%S"))

                            print(my_query2)
                            cur.execute(my_query2)
                            mydb.commit()

                    flash('Customer with NFC ID {} registered successfully at {}!'.format(nfc_id, service_name))
                    return render_template("register.html", x=av_rooms, y=tk_rooms)                       

        elif request.form.get('unregister'):
            my_query1 = """SELECT MAX(NFC_ID) FROM customers;"""

            print(my_query1)
            cur.execute(my_query1)
            result = cur.fetchall()

            if not (nfc_id and service_name):
                flash('Please input an NFC_ID and a provided service', category="error")
                status=400
                return render_template("register.html", x=av_rooms, y=tk_rooms)

            elif (not nfc_id.isnumeric()):
                flash('Please insert a valid NFC_ID', category="error")
                status=400
                return render_template("register.html", x=av_rooms, y=tk_rooms)

            elif int(nfc_id)<1 or int(nfc_id)>result[0][0]:
                flash('Please insert a valid NFC_ID', category="error")
                status=400
                return render_template("register.html", x=av_rooms, y=tk_rooms)        

            else:
                query22 = """SELECT EXISTS (SELECT * FROM register WHERE NFC_ID={} AND SERVICE_ID=(SELECT SERVICE_ID FROM services WHERE category='{}'));
                 """.format(nfc_id, service_name)
                print(query22)
                cur5.execute(query22)
                check = cur5.fetchall() 

                if check[0][0]==False:
                    flash('Customer with NFC ID {} is not registered at {}!'.format(nfc_id, service_name), category="error")
                    return render_template("register.html", x=av_rooms, y=tk_rooms)

                else:    

                    if service_name=="Room":

                        myquery33 = """SELECT EXISTS (SELECT * FROM haveAccess WHERE NFC_ID={} AND AREA_ID=(SELECT AREA_ID FROM areas WHERE area_name='{}'));
                        """.format(nfc_id, room2)
                        print(myquery33)
                        cur2.execute(myquery33)
                        check2 = cur2.fetchall()

                        if check2[0][0]==False:
                            flash('Customer with NFC ID {} was not linked with {}!'.format(nfc_id, room2), category="error")
                            return render_template("register.html", x=av_rooms, y=tk_rooms)

                        else:
                            my_query2 = """DELETE FROM register WHERE NFC_ID={} AND SERVICE_ID=(SELECT SERVICE_ID FROM services WHERE category='{}');
                                """.format(nfc_id, service_name)

                            print(my_query2)
                            cur.execute(my_query2)
                            mydb.commit()

                            my_query3 = """DELETE FROM haveAccess WHERE NFC_ID={} AND AREA_ID=(SELECT AREA_ID FROM areas WHERE area_name='{}');
                                """.format(nfc_id, room2)

                            print(my_query3)
                            cur.execute(my_query3)
                            mydb.commit()

                            for i in range(421,436):
                                my_query5 = """DELETE FROM haveAccess WHERE NFC_ID={} AND AREA_ID={};
                                """.format(nfc_id, i)

                                print(my_query5)
                                cur.execute(my_query5)
                                mydb.commit()

                            my_query6 = """DELETE FROM haveAccess WHERE NFC_ID={} AND AREA_ID=460;
                                """.format(nfc_id)

                            print(my_query6)
                            cur.execute(my_query6)
                            mydb.commit()

                            my_query6 = """DELETE FROM haveAccess WHERE NFC_ID={} AND AREA_ID=461;
                                """.format(nfc_id)

                            print(my_query6)
                            cur.execute(my_query6)
                            mydb.commit()

                            my_query7 = """DELETE FROM haveAccess WHERE NFC_ID={} AND AREA_ID=(SELECT AREA_ID FROM areas WHERE area_floor=(SELECT area_floor FROM areas WHERE AREA_ID=(SELECT AREA_ID FROM areas WHERE area_name='{}')) AND
                                    orientation=(SELECT orientation FROM areas WHERE AREA_ID=(SELECT AREA_ID FROM areas WHERE area_name='{}')) AND beds=0)""".format(nfc_id,room,room2)
                            print(my_query7)
                            cur.execute(my_query7)
                            mydb.commit()

                            availables = """ SELECT C.area_name FROM areas C WHERE  C.AREA_ID<401 AND ((SELECT COUNT(B.NFC_ID) FROM haveAccess B WHERE B.AREA_ID=C.AREA_ID AND B.end_datetime>'{}') < C.beds)""".format(datetime.datetime.now())
                            cur4.execute(availables)
                            av_rooms = cur4.fetchall()

                            taken = """ SELECT M.area_name FROM areas M WHERE M.AREA_ID<401 AND M.area_name NOT IN (SELECT C.area_name FROM areas C WHERE  C.AREA_ID<401 AND ((SELECT COUNT(B.NFC_ID) FROM haveAccess B WHERE B.AREA_ID=C.AREA_ID AND B.end_datetime>'{}') < C.beds))""".format(datetime.datetime.now())
                            cur7.execute(taken)
                            tk_rooms = cur7.fetchall()


                            flash('Customer with NFC ID {} unregistered from {}!'.format(nfc_id, room2))
                            return render_template("register.html", x=av_rooms, y=tk_rooms)

                    else:    

                        my_query2 = """DELETE FROM register WHERE NFC_ID={} AND SERVICE_ID=(SELECT SERVICE_ID FROM services WHERE category='{}');
                            """.format(nfc_id, service_name)

                        print(my_query2)
                        cur.execute(my_query2)
                        mydb.commit()    

                        my_query11 = """SELECT AREA_ID FROM provide WHERE SERVICE_ID=(SELECT SERVICE_ID FROM services WHERE category='{}');""".format(service_name)

                        print(my_query11)
                        cur2.execute(my_query11)
                        result1 = cur2.fetchall()

                        for item in result1:
                            my_query2 = """DELETE FROM haveAccess WHERE NFC_ID={} AND AREA_ID={};
                            """.format(nfc_id, item[0])

                            print(my_query2)
                            cur.execute(my_query2)
                            mydb.commit()

                    flash('Customer with NFC ID {} unregistered successfully from {}!'.format(nfc_id, service_name))
                    return render_template("register.html", x=av_rooms, y=tk_rooms)    

    return render_template("register.html", x=av_rooms, y=tk_rooms)