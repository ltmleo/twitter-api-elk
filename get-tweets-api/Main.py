from src import Mongo

mdb = Mongo.Mongo("twitter", "twitter")

print(mdb.getHashTags())
print(mdb.getByLang())