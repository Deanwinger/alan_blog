from flask_restful import Resource, reqparse
from flask import request
from app.public import decorate_resource
from flask_cors import cross_origin


class Index(Resource):
    @decorate_resource()
    # @cross_origin()
    def get(self):
        return {'msg': 'Got your message %s' % request.method}

    def post(self):
        return {'msg': 'Got your message %s' % request.method}