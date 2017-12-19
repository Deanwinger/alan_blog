from flask_restful import Resource, reqparse
from flask_mail import Message
from flask import current_app
import app



class Email(Resource):
    def get(self):
        pass

    def post(self):
        recipients = []
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='name of the sender')
        parser.add_argument('email', type=str, help='email address of the sender')
        parser.add_argument('intro', type=str, help='brief introduction')
        args = parser.parse_args()
        recipients.append(args["email"])
        print(args)
        msg = Message("test subject",
                        sender='a541203951@163.com',
                        recipients=recipients) #尽是坑啊, 必须要以list形式
        msg.body = ''
        msg.html = args["intro"]
        apps = current_app._get_current_object()
        with apps.app_context():
            app.mail.send(msg)
        return {'msg': "succeed"}
        
