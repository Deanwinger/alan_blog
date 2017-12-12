from flask import Flask
from flask_restful import Api
from app.resources import Email
from flask_mail import Mail
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    mail = Mail(app)
    api = Api(app)
    api.add_resource(Email, '/emails')

    return app


