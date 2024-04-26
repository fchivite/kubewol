from flask import Flask
import sqlite3
from os import path


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DemoDevKey-notProd'

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app

