from flask import Blueprint, render_template, request, flash
from flask_mysqldb import MySQL
import mysql.connector as ddb

home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
def home_fun():
    status=200

    mydb = ddb.connect(
        host = "localhost",
        user = "Thanos",
        passwd = "thanos21",
        database = "HotelDB"
    )

    cur = mydb.cursor()
    cur2 = mydb.cursor()

    if request.method == 'POST':

        phones = []
        emails = []

        nfc_id = request.form.get('NFC_ID')
        last_name = request.form.get('last_name')
        first_name = request.form.get('first_name')
        birth_date = request.form.get('birth_date')
        id = request.form.get('id')
        id_type = request.form.get('id_type')
        id_issue = request.form.get('id_issue')
        phone1 = request.form.get('phone1')
        if phone1:
            phones.append(phone1)
        phone2 = request.form.get('phone2')
        if phone2:
            phones.append(phone2)
        phone3 = request.form.get('phone3')
        if phone3:
            phones.append(phone3)
        email1 = request.form.get('email1')
        if email1:
            emails.append(email1)
        email2 = request.form.get('email2')
        if email2:
            emails.append(email2)
        email3 = request.form.get('email3')
        if email3:
            emails.append(email3)

        if request.form.get("new"):
            if not (last_name and first_name and birth_date and id and id_type and id_issue and (phone1 or phone2 or phone3) and (email1 or email2 or email3)):
                flash('Please complete every field (at least 1 phone and 1 e-mail), except NFC_ID, to add a new customer', category="error")
                status=400
                return render_template("home.html")

            elif not (id.isnumeric() and (phone1.isnumeric() or phone2.isnumeric() or phone3.isnumeric())):
                flash('Please insert only numbers in identification and phone fields', category="error")
                status=400
                return render_template("home.html")    

            else:

                phones = list(set(phones))
                emails = list(set(emails))


                my_query1 = """INSERT INTO customers(last_name, first_name, birth_date, id, id_type, id_issue)
                            VALUES ('{}', '{}', '{}', {}, '{}', '{}');
                    """.format(last_name, first_name, birth_date, id, id_type, id_issue)

                print(my_query1)
                cur.execute(my_query1)
                mydb.commit()    

                my_query11 = """SELECT MAX(NFC_ID) FROM customers;"""

                print(my_query11)
                cur2.execute(my_query11)
                result1 = cur2.fetchall()

                for item in phones:
                    my_query2 = """INSERT INTO customer_phones(NFC_ID, phone_number)
                                VALUES ((SELECT MAX(NFC_ID) FROM customers), {});
                        """.format(item)

                    print(my_query2)
                    cur.execute(my_query2)
                    mydb.commit()

                for item in emails:
                    my_query3 = """INSERT INTO customer_emails(NFC_ID, email_address)
                                VALUES ((SELECT MAX(NFC_ID) FROM customers), '{}');
                        """.format(item)

                    print(my_query3)
                    cur.execute(my_query3)
                    mydb.commit()

                flash('Customer added successfully with NFC ID {} !'.format(result1[0][0]))
                return render_template("home.html")  

        elif request.form.get("modify"):

            my_query1 = """SELECT MAX(NFC_ID) FROM customers;"""

            print(my_query1)
            cur.execute(my_query1)
            result = cur.fetchall()

            if not (nfc_id and nfc_id.isnumeric() and ((phone1 and phone1.isnumeric()) or (phone2 and phone2.isnumeric()) or (phone3 and phone3.isnumeric()) or email1 or email2 or email3)):
                flash('Please provide a valid NFC_ID and at least 1 phone or 1 e-mail', category="error")
                status=400
                return render_template("home.html")

            elif int(nfc_id)<=0 or int(nfc_id)>result[0][0]:
                flash('Please provide a valid NFC_ID and at least 1 phone or 1 e-mail', category="error")
                status=400
                return render_template("home.html")    

            else:

                phones = list(set(phones))
                emails = list(set(emails))


                if len(phones):
                    my_query4 = """DELETE FROM customer_phones WHERE NFC_ID={};""".format(nfc_id)
                    print(my_query4)
                    cur.execute(my_query4)
                    mydb.commit()

                if len(emails):
                    my_query5 = """DELETE FROM customer_emails WHERE NFC_ID={};""".format(nfc_id)
                    print(my_query5)
                    cur.execute(my_query5)
                    mydb.commit()

                for item in phones:

                    my_query2 = """INSERT INTO customer_phones(NFC_ID, phone_number)
                                VALUES ({}, {});
                        """.format(nfc_id, item)

                    print(my_query2)
                    cur.execute(my_query2)
                    mydb.commit()

                for item in emails:
                    my_query3 = """INSERT INTO customer_emails(NFC_ID, email_address)
                                VALUES ({}, '{}');
                        """.format(nfc_id, item)

                    print(my_query3)
                    cur.execute(my_query3)
                    mydb.commit()

                flash('Information of customer updated successfully!')
                return render_template("home.html")

        elif request.form.get("delete"):

            my_query1 = """SELECT MAX(NFC_ID) FROM customers;"""

            print(my_query1)
            cur.execute(my_query1)
            result = cur.fetchall()

            if not (nfc_id and nfc_id.isnumeric()) or int(nfc_id)<=0 or int(nfc_id)>result[0][0]:
                flash('Please provide a valid NFC_ID for deletion', category="error")
                status=400
                return render_template("home.html")

            else:

                my_query2 = """DELETE FROM customers WHERE NFC_ID={};""".format(nfc_id)
                print(my_query2)
                cur.execute(my_query2)
                mydb.commit()

                flash('Customer deleted successfully!')
                return render_template("home.html")                       

    return render_template("home.html")