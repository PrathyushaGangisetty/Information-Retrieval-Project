from gensim.summarization.textcleaner import split_sentences
import re
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

from gensim.summarization import summarize, keywords
from newsdataapi import NewsDataApiClient




@app.route('/')
def welcome():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(   language="en")
    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10) :
        if  response['results'][x]['language'] == 'english':
            content = response['results'][x]['content']
            a = summarize(content, word_count=50)

            arr[x][0] = response['results'][x]['title']
            arr[x][1] = a
            arr[x][2] = response['results'][x]['link']
            # print(a)
        else:
            x=x-1
    return render_template('index.html', result=arr)
    

@app.route('/home', methods=['POST'])
def home():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(timeframe=24, q="breakingnews",   language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize(content, word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        print(a)
    return render_template('index.html', result=arr)

    
@app.route('/search', methods=['POST','GET'])
def search():
    search = request.form['search']
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(timeframe=24, q=search,   language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(5):
        content = response['results'][x]['content']
        
        #a = summarize(content, word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = content
        arr[x][2] = response['results'][x]['link']
        #print(a)
    return render_template('index.html', result=arr)

@app.route('/business', methods=['POST'])
def business():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(category="business",  timeframe=24, language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        print('Virat')
        content = response['results'][x]['content']
        a = summarize(content, word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        # print(a)
    return render_template('index.html', result=arr)

@app.route('/politics', methods=['POST'])
def politics():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(category="politics",  timeframe=24, language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize(content, word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        # print(a)
    return render_template('index.html', result=arr)


@app.route('/technology',  methods=['POST'])
def technology():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(category="technology",  timeframe=24, language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize(content, word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        # print(a)
    return render_template('index.html', result=arr)

@app.route('/sports', methods=['POST'])
def sports():
    api = NewsDataApiClient(apikey="pub_28971750c14aae7b15ba9ff5ae4a26d509b56")
    response = api.news_api(category="sports",  timeframe=24, language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize(content, word_count=50)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        # print(a)
    return render_template('index.html', result=arr)




if __name__ == '__main__':
    app.run(debug=True)
