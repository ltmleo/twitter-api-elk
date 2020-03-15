from src import Mongo

mdb = Mongo.Mongo("twitter", "twitter")
for x in mdb.moreFollowers(10):
    print(x)
