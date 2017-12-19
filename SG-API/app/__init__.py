from flask import Flask
from app import resources
from config import config

from flask_restful import Api
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


mail = Mail()
# db = SQLAlchemy()
api = Api()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    mail.init_app(app)
    # db.init_app(app)

    api.add_resource(resources.Index, '/')
    api.add_resource(resources.Email, '/emails')
    api.init_app(app)

    return app


