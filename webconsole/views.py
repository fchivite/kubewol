from flask import Blueprint, render_template, request
from datetime import datetime
import sqlite3

views = Blueprint('views', __name__)

@views.route('/')
def home():
    try:
        connection = sqlite3.connect('wol.db')
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        query = "SELECT mac,hostname,last_execution from wakeonlan"
        exec = cursor.execute(query)
        result = exec.fetchall()
    except sqlite3.OperationalError as e:
            print(e)
            return render_template("error.html")
    return render_template("dashboard.html", dashboard_content=result)


@views.route('/dashboard')
def dashboard():
    return home()


@views.route('/add-wol', methods=['GET', 'POST'])
def add_wol():
    if request.method == 'POST':
        mac = request.form.get('mac')
        hostname = request.form.get('hostname')
        heartbeat = request.form.get('heartbeat')
        monitor = request.form.get('monitor')
        address = request.form.get('address')

        try:
            connection = sqlite3.connect('wol.db')
            cursor = connection.cursor()
            query = f"INSERT INTO wakeonlan (mac,hostname,heartbeat,monitor,address)VALUES('{mac}', '{hostname}',{heartbeat},'{monitor}','{address}')"
            cursor.execute(query)
            connection.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error occurred: MAC Address {mac} already exists.")
        except sqlite3.OperationalError as e:
            print(e)
    
    return render_template("addwol.html")