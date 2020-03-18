from src import Mongo, System
from flask import Flask, request, g
from flask_restplus import Resource, Api, fields
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LoggingHandler
import time, datetime

mdb = Mongo.Mongo("twitter", "twitter")
l = System.Log()

app = Flask(__name__)
api = Api(app, version='1.0', title='Get Tweets API',
    description='An API to get tweets',
)

apm = ElasticAPM(app, server_url='http://apm-server-apm-server:8200', service_name='get-tweets-api', logging=False)

@api.doc(params={'topic': 'An hashtag (without #)', "number": "size of response (default 5)"}, responses={ 200: 'List the most followed users per topic'})
class MostFolowed(Resource):
    def get(self, topic = {}, number = 5):
        g.curr_request = request
        if topic != {}:
            topic = {"hashtag": "#"+topic}
        return mdb.getMostFollowed(topic, number)

@api.doc(responses={ 200: 'list of hashtags in the database'})
class HashTags(Resource):
    def get(self):
        g.curr_request = request
        return mdb.getHashTags()

@api.doc(responses={ 200: 'object of number of publications per hour'})
class GetByHour(Resource):
    def get(self):
        g.curr_request = request
        return mdb.getByHour()

@api.doc(params={'hashtag': 'An hashtag (without #)'}, responses={ 200: 'object of number of publications per language'})
class GetByLang(Resource):
    def get(self, hashtag = "$hashtag"):
        g.curr_request = request
        if hashtag != "$hashtag":
            hashtag = f"#{hashtag}"
        return mdb.getByLang(hashtag)

@api.doc(params={'hashtag': 'An hashtag (without #)'}, responses={ 200: 'object of number of publications per country'})
class GetByCountry(Resource):
    def get(self, hashtag = "$hashtag"):
        g.curr_request = request
        if hashtag != "$hashtag":
            hashtag = f"#{hashtag}"
        return mdb.getByCountry(hashtag)

@api.doc(responses={ 200: 'ok'})        
class HealthCheck(Resource):
    def get(self):
        g.curr_request = request
        return {"Status": "ok"}, 200

@app.after_request
def log_the_status_code(response):
    try:
        diff = (time.time() - g.start_time)*1000
        obj = { "date": str(datetime.datetime.now()),
                "reponse-time": f"{diff} ms",
                "url": g.curr_request.url,
                "method": g.curr_request.method,
                "status": response.status}
    except:
        obj = { "date": str(datetime.datetime.now()),
                "error": "unknown",
                "status": response.status}
    if response.status.startswith("2"):
        l.info(obj)
    else:
        l.error(obj)
    return response

@app.before_request
def set_vars():
    g.start_time = time.time()


api.add_resource(MostFolowed, '/mostFolowed', '/mostFolowed/<topic>', '/mostFolowed/<int:number>', '/mostFolowed/<topic>/<int:number>')
api.add_resource(HashTags, '/hashTags')
api.add_resource(GetByHour, '/getByHour')
api.add_resource(GetByLang, '/getByLang', '/getByLang/<hashtag>')
api.add_resource(GetByCountry, '/getByCountry', '/getByCountry/<hashtag>')
api.add_resource(HealthCheck, '/healthcheck')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8081')