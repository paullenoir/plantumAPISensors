
from flask import Flask
from models import db

def create_app():
    app = Flask(__name__)

    # Database Google
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pl271088@34.132.189.10/plantumdb'
    # Database Wamp Test
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/plantumdb'
    
    # supprimer les log de mise a jour dans la console
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # Init db
    db.init_app(app)

    return app

