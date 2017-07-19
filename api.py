'''
Project SEROL

This is a set of test API endpoints
'''

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class BaseApi(Resource):
    def get(self):
        return {'status': 'ok'}


class ChallengeApi(Resource):
    def get(self):
        status =  {'mission':1,'id':3,'challenge':'Observe a galaxy','status':'done'}
        return status

class MissionApi(Resource):
    def get(self):
        status = {'id':1,'mission':'Beginner Level','progress':0.5}
        return status

class StickersApi(Resource):
    def get(self):
        status = {'stickers': [{'challenge':1, 'name':'First Observation', 'file':''},
                                {'challenge':2, 'name':'Observe a star cluster', 'file':''},
                                {'challenge':3, 'name':'Observe a galaxy', 'file':''}
                                ]}
        return status

class SerolApi(Resource):
    def get(self):
        status = {'status': 'ok'}
        return status

class RequestApi(Resource):
    def post(self):
        status = {'status': 'ok'}
        return status


api.add_resource(BaseApi, '/')
api.add_resource(MissionApi, '/mission/')
api.add_resource(StickersApi, '/stickers/')
api.add_resource(SerolApi, '/serol/')
api.add_resource(RequestApi, '/request/')

if __name__ == '__main__':
    app.run()
