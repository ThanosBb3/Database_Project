from flask import Flask, render_template, request
from flask_mysqldb import MySQL

mysql = MySQL()


def create_app():
    
    App = Flask(__name__, static_folder='./frontend/static', template_folder='./frontend/templates')
    App.config["MYSQL_USER"] = "root"
    App.config["MYSQL_PASSWORD"] = "boftonelly"
    App.config["MYSQL_HOST"] = "localhost"
    App.config["MYSQL_DB"] = "HotelDB"
    App.config['SECRET_KEY'] = 'super secret key'
    mysql.init_app(App)

    from app.backend import home, records, views, statistics, covid

    App.register_blueprint(home, url_prefix='/')
    App.register_blueprint(records, url_prefix='/records')
    App.register_blueprint(views, url_prefix='/')
    App.register_blueprint(covid, url_prefix='/')
    App.register_blueprint(statistics, url_prefix='/')

    return App
