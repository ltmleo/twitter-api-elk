import pymongo, os
from src import System
l = System.Log()
class Mongo:
    def __init__(self, dbName, colName):
        mongoAddress = f"{os.environ["MONGO_HOST"]}:{os.environ["MONGO_PORT"]}"
        l.info(f"Connecting to {mongoAddress}")
        myclient = pymongo.MongoClient(mongoAddress)
        mydb = myclient[dbName]
        self.mycol = mydb[colName]

    def __avoidDuplication(self, mylist):
        for obj in mylist:
            if self.query(obj).count() != 0:
                return False
            else:
                return True

    def insert(self, mylist):
        if self.__avoidDuplication(mylist):
            x = self.mycol.insert_many(mylist)
            l.info(f"{len(mylist)} objects inserted")
            return x.inserted_ids
        else:
            l.info(f"{len(mylist)} objects duplicated")
            return {"status": "duplicated"}

    def query(self, myquery):
        #myquery = { "address": "Park Lane 38" }
        return self.mycol.find(myquery)