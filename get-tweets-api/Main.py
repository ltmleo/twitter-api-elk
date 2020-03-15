from src import Mongo

mdb = Mongo.Mongo("twitter", "twitter")
topic= {"hashtag": "#VTNC102"}

print(mdb.getHashTags())
for x in mdb.getMostFollowed(topic, 10):
    print(x)
