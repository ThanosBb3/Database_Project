from flask import Flask, render_template, request
from flask_mysqldb import MySQL

mysql = MySQL()


def create_app():
    
    App = Flask(__name__, static_folder='./frontend/static', template_folder='./frontend/templates')
    App.config['SECRET_KEY'] = 'hjshjhdjh'
    App.config["MYSQL_USER"] = "*******"
    App.config["MYSQL_PASSWORD"] = "*******"
    App.config["MYSQL_HOST"] = "*******"
    App.config["MYSQL_DB"] = "HotelDB"
    mysql.init_app(App)

    from app.backend import base, records, views, covid

    App.register_blueprint(base, url_prefix='/')
    App.register_blueprint(records, url_prefix='/records')
    App.register_blueprint(views, url_prefix='/')
    App.register_blueprint(covid, url_prefix='/')

    return App