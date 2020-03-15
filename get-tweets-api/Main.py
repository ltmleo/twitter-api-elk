from src import Mongo

mdb = Mongo.Mongo("twitter", "twitter")
for x in mdb.mostFollowed(10):
    print(x)
