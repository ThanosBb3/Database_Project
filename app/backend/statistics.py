from flask import Blueprint, render_template, request, flash
from flask_mysqldb import MySQL
from .. import mysql
import datetime

statistics = Blueprint('statistics', __name__)

@statistics.route('/statistics', methods=['GET', 'POST'])
def stats():
    status=200
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        age_group = request.form.get("age_group")
        if age_group == "20-40":
            age_from = 20
            age_to = 40
        elif age_group == "41-60":
            age_from = 41
            age_to = 60
        else:
            age_from = 61
            age_to = 1000

        time_period = request.form.get("time_period")
        if time_period == "Last Year":
            date_from = (datetime.datetime.now()-datetime.timedelta(days=365)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            date_from = (datetime.datetime.now()-datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")

        if request.form.get("areas"):
            my_query = """SELECT B.area_name, count(A.AREA_ID) AS visit 
            FROM visit A, areas B, customers C 
            WHERE A.AREA_ID=B.AREA_ID AND A.AREA_ID>400 AND A.NFC_ID=C.NFC_ID 
                AND C.birth_date<='{}-12-31' AND C.birth_date>='{}-01-01'
                AND A.enter_datetime>='{}'
            GROUP BY A.AREA_ID 
            ORDER BY visit DESC LIMIT 15;
                """.format(datetime.datetime.now().year-age_from, datetime.datetime.now().year-age_to, date_from)
            x =  0   

        elif request.form.get("services"):
            my_query = """SELECT B.category, count(A.SERVICE_ID) AS useService 
            FROM useService A, services B, customers C 
            WHERE A.SERVICE_ID=B.SERVICE_ID AND A.SERVICE_ID>1 AND A.NFC_ID=C.NFC_ID 
                AND C.birth_date<='{}-12-31' AND C.birth_date>='{}-01-01'
                AND A.date_time>='{}'
            GROUP BY A.SERVICE_ID 
            ORDER BY useService DESC;
                """.format(datetime.datetime.now().year-age_from, datetime.datetime.now().year-age_to, date_from)
            x = 1    

        elif request.form.get("popular_services"):
            my_query = """SELECT B.category, count(DISTINCT A.NFC_ID) AS useService 
            FROM useService A, services B, customers C 
            WHERE A.SERVICE_ID=B.SERVICE_ID AND A.SERVICE_ID>1 AND A.NFC_ID=C.NFC_ID 
                AND C.birth_date<='{}-12-31' AND C.birth_date>='{}-01-01'
                AND A.date_time>='{}'
            GROUP BY A.SERVICE_ID 
            ORDER BY useService DESC;
                """.format(datetime.datetime.now().year-age_from, datetime.datetime.now().year-age_to, date_from)
            x = 2

        print(my_query)
        cur.execute(my_query)
        results = cur.fetchall()
        flash("Here are your results!", category='success')
        return render_template("statistics.html", results=results, pick=x, y=age_group, t=time_period)

        
    return render_template("statistics.html")