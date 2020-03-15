from src import Mongo
from flask import Flask, request
from flask_restful import Resource, Api

mdb = Mongo.Mongo("twitter", "twitter")


app = Flask(__name__)
api = Api(app)
class MostFolowed(Resource):
    def get(self, topic = {}, number = 5):
        if topic != {}:
            topic = {"hashtag": "#"+topic}
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

api.add_resource(MostFolowed, '/mostFolowed', '/mostFolowed/<topic>', '/mostFolowed/<int:number>', '/mostFolowed/<topic>/<int:number>')
api.add_resource(HashTags, '/hashTags')
api.add_resource(GetByHour, '/getByHour')
api.add_resource(GetByLang, '/getByLang', '/getByLang/<hashtag>')
api.add_resource(GetByCountry, '/getByCountry', '/getByCountry/<hashtag>')

if __name__ == '__main__':
    app.run(port='5002')