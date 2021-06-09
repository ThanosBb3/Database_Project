from flask import Blueprint, render_template, request
from flask_mysqldb import MySQL
from .. import mysql

views = Blueprint('views', __name__)

@views.route('/views', methods=['GET', 'POST'])
def get_view():
    status=200
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        x = request.form.get("info")

        if x == 'Customer Info':
            my_query = """SELECT *
                FROM customers_info;
                """

        elif x == 'Service Sales':
            my_query = """SELECT *
                FROM services_sales;
                """

        print(my_query)
        cur.execute(my_query)
        results = cur.fetchall()
        return render_template("views.html", results=results, data=x)

        

    return render_template("views.html", results=None)