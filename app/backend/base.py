from flask import Blueprint, render_template

base = Blueprint('base', __name__)

@base.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")