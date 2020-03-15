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

    def mostFollowed(self, number):
        mostFollowed = []
        auxList = [] #The user can gain followers
        for x in list(self.mycol.find({}).sort("followers", pymongo.DESCENDING)):
            if (len(mostFollowed) < number) and x["user"] not in auxList:
                auxList.append(x["user"])
                mostFollowed.append({"user": x["user"], "followers": x["followers"]})
            elif(len(mostFollowed) >= number):
                break
        return mostFollowed
