from flask import Blueprint, render_template, request
from .models import Wol
from . import db
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import json

views = Blueprint('views', __name__)

@views.route('/')
def home():
    db_entries = db.session.execute(db.select(Wol).order_by(Wol.hostname)).scalars()
    wols = [ line.replace("WOL;","",1).split(';') for line in open('instance/wol.log') if line.startswith("WOL;")]
    return render_template("dashboard.html", dashboard_content=db_entries, wols=wols)


@views.route('/dashboard')
def dashboard():
    return home()


@views.route('/add-wol', methods=['GET', 'POST'])
def add_wol():
    if request.method == 'POST':
        mac = request.form.get('mac').upper()
        hostname = request.form.get('hostname')
        monitor = str(request.form.get('monitor'))
        address = request.form.get('address')
        if monitor != 'ping' and (not address.startswith(monitor)):
            address = f'{monitor}://{address}'

        new_wol = Wol(mac=mac.upper(), hostname=hostname, monitor=monitor, address=address)
        try:
            db.session.add(new_wol)
            db.session.commit()
        except IntegrityError as e:
            print(f"Error occurred: MAC Address {mac} already exists.")
        return dashboard()
    
    return render_template("addwol.html")


@views.route('/delete')
def delte():
    mac = request.args.get('mac')
    entry = db.session.execute(db.select(Wol).filter_by(mac=mac)).scalars().first()
    db.session.delete(entry)
    db.session.commit()
    return dashboard()
