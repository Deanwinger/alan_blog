from flask import Flask
from flask_restful import Api
from app.resources import Email
from flask_mail import Mail


app = Flask(__name__)
mail = Mail(app)
api = Api(app)
api.add_resource(Email, '/emails')
    
if __name__ == '__main__':
    app.run(debug=True)