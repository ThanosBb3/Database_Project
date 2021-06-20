from flask import Blueprint, render_template, request, flash
from flask_mysqldb import MySQL
from .. import mysql
from datetime import date, timedelta

records = Blueprint('records', __name__)

@records.route('/service_records', methods=['GET', 'POST'])
def serv_rec():
    status=200
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        datefrom = request.form.get('datefrom')
        dateto = request.form.get('dateto')
        costfrom = request.form.get('costfrom')
        costto = request.form.get('costto')
        service_type = request.form.get('service_type')


        if not datefrom:
            datefrom = "1900-00-00"
        if not dateto:
            dateto = str(date.today() + timedelta(days=5))
        if not costfrom:
            costfrom = 0
        if not costto:
            costto = 99999            
        datefrom = datefrom + " 00:00:00"
        dateto = dateto + " 23:59:59"
        if service_type=="All":
            my_query = """SELECT A.NFC_ID, B.last_name, B.first_name, C.category, A.cost, D.enter_datetime, D.leave_datetime  
            FROM useService A, customers B, services C, visit D
            WHERE
                A.date_time >= '{}'
                AND A.date_time <= '{}'
                AND A.cost >= {}
                AND A.cost <= {}
                AND A.SERVICE_ID <> 1
                AND C.SERVICE_ID = A.SERVICE_ID
                AND A.NFC_ID = B.NFC_ID
                AND D.NFC_ID = A.NFC_ID
                AND D.enter_datetime <= A.date_time
                AND D.leave_datetime >= A.date_time                    
            GROUP BY A.date_time
            ORDER BY A.date_time DESC;
            """.format(datefrom, dateto, costfrom, costto)
                
        else:    
            my_query = """SELECT A.NFC_ID, B.last_name, B.first_name, C.category, A.cost, D.enter_datetime, D.leave_datetime  
            FROM useService A, customers B, services C, visit D
            WHERE
                A.date_time >= '{}'
                AND A.date_time <= '{}'
                AND A.cost >= {}
                AND A.cost <= {}
                AND A.SERVICE_ID = (SELECT SERVICE_ID
                                    FROM services
                                    WHERE category='{}')
                AND C.SERVICE_ID = A.SERVICE_ID
                AND A.NFC_ID = B.NFC_ID
                AND D.NFC_ID = A.NFC_ID
                AND D.enter_datetime <= A.date_time
                AND D.leave_datetime >= A.date_time                    
            ORDER BY D.leave_datetime DESC;
            """.format(datefrom, dateto, costfrom, costto, service_type)
        print(my_query)
        cur.execute(my_query)
        results = cur.fetchall()
        flash("Here are your results!", category='success')
        return render_template("serv_rec.html", results=results, service=service_type)

    return render_template("serv_rec.html")        