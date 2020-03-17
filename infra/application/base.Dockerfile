#IMAGE BASE FOR APPLICATIONS
FROM python:3.7.7-slim

#TO APP SHOW UP LOGS IN KUBERNETES
ENV PYTHONUNBUFFERED=1 

RUN pip3 install pymongo cryptography \
    tweepy python-logstash_async configparser \
    flask flask_restful blinker elastic-apm
    

