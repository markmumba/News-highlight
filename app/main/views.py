from flask import render_template,request,redirect,url_for
from ..request import get_news,get_newss
from ..models import Article
from . import main




@main.route('/')

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


@main.route('/news/<news_id>')
def news(id):

    '''
    View movie page function that returns the movie details page and its data
    '''

    source = get_newss(id)
    newsid = id.capitalize()
    title = f'{newsid}'
    details = id.capitalize()
    content = f'{details}'
    return render_template('news_source.html',  title = title, id = newsid ,source = source ,content = content)


