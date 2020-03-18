from flask import Flask, Markup, render_template
import os, requests

app = Flask(__name__)

try:
    os.environ["GET_TWEETS_API_ENDPOINT"]
except:
    GET_TWEETS_API_ENDPOINT = "http://localhost:8081"


colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Bitcoin Monthly Price in USD', max=max(values), labels=bar_labels, values=bar_values)

@app.route('/numTweets')
def numTweets():
    labels = []
    values = []
    data = dict(requests.get(f"{GET_TWEETS_API_ENDPOINT}/getByHour").json())
    for i in data:
        labels.append(i)
        values.append(data[i])
    return render_template('line_chart.html', title='Num de tweets por hora do dia', max=max(values), labels=labels, values=values)

@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Bitcoin Monthly Price in USD', max=max(values), set=zip(values, labels, colors))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)