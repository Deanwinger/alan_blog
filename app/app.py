from flask import Flask
from flask_restful import Api
from myapi.resources.users import Users


app = Flask(__name__)
api = Api(app)

api.add_resource(Users, '/Users', '/Users/<str:id>')
