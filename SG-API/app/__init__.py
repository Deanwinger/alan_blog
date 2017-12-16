from flask import Flask
from app import resources
from config import config

from flask_restful import Api
from flask_mail import Mail


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    mail = Mail(app)
    api = Api(app)
    api.add_resource(resources.Index, '/')
    api.add_resource(resources.Email, '/emails')

    return app


