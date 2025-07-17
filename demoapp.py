from newsdataapi import NewsDataApiClient
from gensim.summarization import summarize, keywords
from gensim.summarization.textcleaner import split_sentences
import re
from gensim.models import Word2Vec as w2v

from googletrans import Translator

translator = Translator()
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)


@app.route('/')
def welcome():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(timeframe=24, category='top',language='en')
    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        if response['results'][x]['language'] == 'english':
            content = response['results'][x]['content']
            # content = translator.translate(content)
            a = summarize(str(content), word_count=50)

            arr[x][0] = response['results'][x]['title']
            arr[x][1] = a
            arr[x][2] = response['results'][x]['link']
            # print(a)
        else:
            x = x-1
    return render_template('demo.html', result=arr)


@app.route('/home', methods=['POST'])
def home():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(timeframe=6, q="breakingnews",   language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize(str(content), word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        print(a)
    return render_template('demo.html', result=arr)


@app.route('/search', methods=['POST', 'GET'])
def search():
    search = request.form['search']
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(timeframe=24, q=search,   language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']

        a = summarize(str(content), word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        # print(a)
    return render_template('demo.html', result=arr)


@app.route('/business', methods=['POST'])
def business():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(category="business",  timeframe=24, language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        print('Virat')
        content = response['results'][x]['content']
        a = summarize(str(content), word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        # print(a)
    return render_template('demo.html', result=arr)


@app.route('/politics', methods=['POST'])
def politics():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(category="politics",  timeframe=24, language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize(str(content), word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        # print(a)
    return render_template('demo.html', result=arr)


@app.route('/technology',  methods=['POST'])
def technology():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(category="technology", timeframe=24, language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize(str(content), word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        # print(a)
    return render_template('demo.html', result=arr)


@app.route('/sports', methods=['POST'])
def sports():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(category="sports",  timeframe=24, language="en")

    

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        
        print(len(content.split()))
        if (len(content.split()) < 50):
            a = content
        else:
            a = summarize(str(content), word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        # print(a)
    return render_template('demo.html', result=arr)

@app.route('/entertainment', methods=['POST'])
def entertainment():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(category="entertainment",  timeframe=24, language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize(str(content), word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        # print(a)
    return render_template('demo.html', result=arr)

@app.route('/world', methods=['POST'])
def world():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(category="world",  timeframe=24, language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize(str(content), word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        # print(a)
    return render_template('demo.html', result=arr)


if __name__ == '__main__':
    app.run(debug=True)
