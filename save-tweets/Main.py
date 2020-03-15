from src import Twitter, Mongo
import time

def main():
    tw = Twitter.Twitter()
    mdb = Mongo.Mongo("twitter", "twitter")

    hashTagsList = ["#openbanking", "#apifirst", "#devops", 
                    "#cloudfirst", "#microservices", "#apigateway", 
                    "#oauth", "#swagger", "#raml", "#openapis"]

    for hashTag in hashTagsList:
        print(f"Getting tweets for {hashTag}")
        mdb.insert(tw.getHashTag(hashTag))

while True:
    main()
    print("Sleeping for 1 hour")
    time.sleep(3600)

