from . import db

class Wol(db.Model):
    __tablename__ = 'wakeonlan'
    mac = db.Column(db.String(17), primary_key=True)
    hostname = db.Column(db.String(17))
    last_execution = db.Column(db.DateTime)
    monitor = db.Column(db.String(5))
    address = db.Column(db.String(100))
    healthy = db.Column(db.Boolean, default=False)