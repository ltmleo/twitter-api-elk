import pymongo

class Mongo:
    def __init__(self, dbName, colName):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
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
            return x.inserted_ids
        else:
            return {"status": "duplicated"}

    def query(self, myquery):
        #myquery = { "address": "Park Lane 38" }
        return self.mycol.find(myquery)

    def moreFollowers(self, number):
        all = list(self.mycol.find({}).sort("followers", pymongo.DESCENDING).limit(5))
        print(all)