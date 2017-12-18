from flask_restful import Resource
from flask_restful import reqparse
from flask_mail import Message
from config import config





class Email(Resource):
    def get(self):
        pass

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='name of the sender')
        parser.add_argument('email', type=str, help='email address of the sender')
        parser.add_argument('intro', type=str, help='brief introduction')
        args = parser.parse_args()
        print(args)
        msg = Message("很高兴收到您的来信，我会尽快跟您联系",
                        sender=config['FLASKY_MAIL_SENDER'], 
                        recipients=config['FLASKY_ADMIN'])
        msg.send(msg)        
        return {'msg': "succeed"}
        
