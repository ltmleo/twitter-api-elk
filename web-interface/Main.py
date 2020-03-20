from flask import Flask, Markup, render_template
import os, requests
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LoggingHandler

app = Flask(__name__)
apm = ElasticAPM(app, server_url='http://apm-server-apm-server:8200', service_name='web-interface', logging=True)


try:
    GET_TWEETS_API_ENDPOINT = os.environ["GET_TWEETS_API_ENDPOINT"]
except:
    GET_TWEETS_API_ENDPOINT = "http://localhost:8081"


colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/mostFolowed/<topic>/<int:number>')
def mostFollowed(topic, number):
    if topic == "all":
        topic = ""
        msg = ""
    else:
        msg = f"for #{topic}"
        topic = f"{topic}/"
    labels = []
    values = []
    data = list(requests.get(f"{GET_TWEETS_API_ENDPOINT}/mostFolowed/{topic}{number}").json())
    for i in data:
        labels.append(i["user"])
        values.append(i["followers"])
    return render_template('bar_chart.html', title=f'Number of Followers {msg}', max=max(values), labels=labels, values=values)

@app.route('/numTweets')
def numTweets():
    labels = []
    values = []
    data = dict(requests.get(f"{GET_TWEETS_API_ENDPOINT}/getByHour").json())
    for i in data:
        labels.append(i)
        values.append(data[i])
    return render_template('line_chart.html', title='Num de tweets por hora do dia', max=max(values), labels=labels, values=values)

@app.route("/getByCountry/<topic>")
def getByCountry(topic):
    if topic == "all":
        topic = ""
    else:
        topic = f"/{topic}"
    data = dict(requests.get(f"{GET_TWEETS_API_ENDPOINT}/getByCountry{topic}").json())
    return render_template('table.html',result=data)

@app.route("/getByLang/<topic>")
def getByLang(topic):
    if topic == "all":
        topic = ""
    else:
        topic = f"/{topic}"
    data = dict(requests.get(f"{GET_TWEETS_API_ENDPOINT}/getByLang{topic}").json())
    return render_template('table.html',result=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)