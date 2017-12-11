from flask import Flask
from flask_restful import Api
from app.resources import Email


app = Flask(__name__)
api = Api(app)
api.add_resource(Email, '/emails')
    
if __name__ == '__main__':
    app.run(debug=True)