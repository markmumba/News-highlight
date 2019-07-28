from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,get_newss




@app.route('/')

def index():
    
    '''
    view root page func that returns index page an func
    '''
    general = get_news('general')
    business = get_news('business')
    technology = get_news('technology')
    health = get_news('health')
    science = get_news('science')
    sports = get_news('sports')
    
    title = 'The best news Highlits In The World'
    
    search_news_source =request.args.get('news_query')


    if search_news_source:
        return redirect(url_for('main.index',news_name = search_news_source))
    else:
        return render_template('index.html',title = title,general = general ,business = business, technology = technology,health=health,science=science,sports=sports)





    return render_template('index.html')


@app.route('/news/<news_id>')
def news(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_newss(id)
    title =  '{news.title}'


    return render_template('news.html',title = title,news = news)


