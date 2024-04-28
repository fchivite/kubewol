from webconsole import create_app
from webconsole.logger import Logger
from apscheduler.schedulers.background import BackgroundScheduler
from webconsole import db
from webconsole.models import Wol
from wakeonlan import send_magic_packet
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from datetime import datetime

app_port = 5000

app = create_app()
scheduler = BackgroundScheduler()

def get_monitors():
    with app.app_context():
        db_entries = db.session.execute(db.select(Wol).order_by(Wol.hostname)).scalars()
        for entry in db_entries:
            if entry.monitor == "https":
                try:
                    requests.get(entry.address, verify=False, timeout=5)
                    entry.healthy = True
                    db.session.commit()
                except:
                    send_magic_packet(entry.mac)
                    Logger.write(f"Sent Magic Packet to {entry.hostname} with MAC Address {entry.mac}")
                    Logger.wol(entry.hostname)
                    entry.last_execution = datetime.today()
                    entry.healthy = False
                    db.session.commit()
                    

if __name__ == "__main__":
    scheduler.add_job(func=get_monitors, trigger="interval", seconds=60)
    scheduler.start()
    app.run(host="0.0.0.0", port=int(app_port), debug=True, use_reloader=False)
	
