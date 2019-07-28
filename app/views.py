from flask import render_template
from app import app
from .request import get_news,get_newss



@app.route('/')

def index():
    
    '''
    view root page func that returns index page an func
    '''
    return render_template('index.html')


@app.route('/news/<news_id>')
def news(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_newss(id)
    title =  '{news.title}'


    return render_template('news.html',title = title,news = news)


