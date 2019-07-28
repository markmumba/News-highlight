from flask import render_template
from app import app
from .request import get_news



@app.route('/')

def index():
    
    '''
    view root page func that returns index page an func
    '''
    return render_template('index.html')


@app.route('/news/<news_id>')
def news(news_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('news.html',id = news_id)


