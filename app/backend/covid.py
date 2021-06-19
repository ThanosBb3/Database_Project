from flask import Blueprint, render_template, request
from flask_mysqldb import MySQL
from .. import mysql

covid = Blueprint('covid', __name__)

@covid.route('/covid', methods=['GET', 'POST'])
def covid_check():
    status=200
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        person = request.form.get("person")
        if request.form.get("areas"):
            my_query = """SELECT A.AREA_ID, B.area_name, A.enter_datetime, A.leave_datetime
                FROM visit A, areas B
                WHERE A.AREA_ID=B.AREA_ID AND NFC_ID={}
                ORDER BY leave_datetime DESC;
                """.format(person)
            x =  0   

        elif request.form.get("contacts"):
            my_query = """SELECT A.NFC_ID, A.last_name, A.first_name, GROUP_CONCAT(distinct customer_phones.phone_number), GROUP_CONCAT(distinct customer_emails.email_address)
                FROM customers A, customer_phones, customer_emails, visit B, visit C
                WHERE A.NFC_ID<>{} AND
                    A.NFC_ID=customer_phones.NFC_ID AND A.NFC_ID=customer_emails.NFC_ID AND
                    B.NFC_ID={} AND C.NFC_ID=A.NFC_ID AND B.AREA_ID=C.AREA_ID AND
                    C.leave_datetime > B.enter_datetime AND C.enter_datetime < CONVERT(ADDTIME(STR_TO_DATE(B.leave_datetime,'%Y-%m-%d %H:%i:%s'),'1:0:0'), CHAR)
                GROUP BY A.NFC_ID
                ORDER BY A.NFC_ID DESC
                """.format(person, person)
            x = 1    

        print(my_query)
        cur.execute(my_query)
        results = cur.fetchall()
        return render_template("covid.html", results=results, pick=x)

        

    return render_template("covid.html", results=None, pick=None)