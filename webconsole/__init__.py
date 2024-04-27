from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from os import path

db = SQLAlchemy()
DB_NAME = "wol_db.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DemoDevKey-notProd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    with app.app_context():
        db.create_all()

    return app


def create_database(app):
    if not path.exists('webconsole/' + DB_NAME):
        db.create_all(app=app)
        print('WOL database created.')