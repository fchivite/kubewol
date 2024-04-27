from webconsole import create_app
from flask_apscheduler import APScheduler
from webconsole import db
from webconsole.models import Wol
from wakeonlan import send_magic_packet
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app_port = 5000

app = create_app()
scheduler = APScheduler()

@scheduler.task('interval', id='get_monitors', seconds=60)
def get_monitors():
    with app.app_context():
        db_entries = db.session.execute(db.select(Wol).order_by(Wol.hostname)).scalars()
        for entry in db_entries:
            if entry.monitor == "https":
                status = requests.get(entry.address, verify=False)
                if status.status_code != 200:
                    send_magic_packet(entry.mac)
                    print(f"Sent Magic Packet to {entry.hostname} with MAC Address {entry.mac}")

if __name__ == "__main__":
    scheduler.init_app(app)
    scheduler.start()
    app.run(host="0.0.0.0", port=int(app_port), debug=True, use_reloader=False)
	
