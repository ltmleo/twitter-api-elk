from src import Mongo, System
from flask import Flask, request
from flask_restful import Resource, Api
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LoggingHandler

mdb = Mongo.Mongo("twitter", "twitter")
#l = System.Log()

app = Flask(__name__)
api = Api(app)
apm = ElasticAPM(app, server_url='http://apm-server-apm-server:8200', service_name='get-tweets-api', logging=False)
class MostFolowed(Resource):
    def get(self, topic = {}, number = 5):
        if topic != {}:
            topic = {"hashtag": "#"+topic}
        print(request.method + " " + request.url + " " + "200")
        return mdb.getMostFollowed(topic, number)

class HashTags(Resource):
    def get(self):
        return mdb.getHashTags()

class GetByHour(Resource):
    def get(self):
        return mdb.getByHour()

class GetByLang(Resource):
    def get(self, hashtag = "$hashtag"):
        if hashtag != "$hashtag":
            hashtag = f"#{hashtag}"
        return mdb.getByLang(hashtag)
class GetByCountry(Resource):
    def get(self, hashtag = "$hashtag"):
        if hashtag != "$hashtag":
            hashtag = f"#{hashtag}"
        return mdb.getByCountry(hashtag)
class HealthCheck(Resource):
    def get(self):
        return {"Status": "ok"}, 200

api.add_resource(MostFolowed, '/mostFolowed', '/mostFolowed/<topic>', '/mostFolowed/<int:number>', '/mostFolowed/<topic>/<int:number>')
api.add_resource(HashTags, '/hashTags')
api.add_resource(GetByHour, '/getByHour')
api.add_resource(GetByLang, '/getByLang', '/getByLang/<hashtag>')
api.add_resource(GetByCountry, '/getByCountry', '/getByCountry/<hashtag>')
api.add_resource(HealthCheck, '/healthcheck')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8081')