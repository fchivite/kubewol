from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DemoDevKey-notProd'

    from .views import views
    from .dashboard import dashboard

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(dashboard, url_prefix='/')
    return app