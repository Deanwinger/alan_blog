from flask_restful import Resource
from flask_restful import reqparse





class Email(Resource):
    def get(self):
        pass

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='name of the sender')
        parser.add_argument('username', type=str, help='Rate to charge for this resource')
        parser.add_argument('age', type=int, help='Rate to charge for this resource')
        parser.add_argument('intro', type=str, help='Rate to charge for this resource')
        args = parser.parse_args()
        print(args)
        return {'msg': "succeed"}
        
