from flask import Blueprint, render_template, request, jsonify
from .models import Wol
from . import db
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import json

views = Blueprint('views', __name__)

@views.route('/')
def home():
    db_entries = db.session.execute(db.select(Wol).order_by(Wol.hostname)).scalars()
    return render_template("dashboard.html", dashboard_content=db_entries)


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
        #last_execution = datetime.today()

        new_wol = Wol(mac=mac.upper(), hostname=hostname, heartbeat=heartbeat, monitor=monitor, address=address)
        try:
            db.session.add(new_wol)
            db.session.commit()
        except IntegrityError as e:
            print(f"Error occurred: MAC Address {mac} already exists.")
    
    return render_template("addwol.html")