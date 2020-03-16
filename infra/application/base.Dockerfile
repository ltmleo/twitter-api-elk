#IMAGE BASE FOR APPLICATIONS
FROM python:3.7.7-slim

RUN pip3 install pymongo cryptography \
    tweepy python-logstash_async configparser \
    flask flask_restful
    

