import urllib.request,json
from .models import News


# getting api_key
api_key =None
# getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):

    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_respose = json.loads(get_news_data)

        news_results = None

        if get_news_respose['sources']:
            news_results_list = get_news_respose['sources']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):

        
    news_results = []

    for new_item in news_list:
        id = new_item.get('id')
        author = new_item.get('author')
        title = new_item.get('title')
        description = new_item.get('description')
        url = new_item.get('url')
        urlToImage = new_item.get('urlToImage')
        publishedAt = new_item.get('publishedAt')
        content = new_item.get('content')

        news_object = (id, author, title, description, url,
                       urlToImage, publishedAt, content)

        news_results.append(news_object)

    return news_results


def get_newss(source):
    get_news_source_url = base_url.format(source, api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_source_results = None

        if get_news_source_response['sources']:
            news_source_results_list = get_news_source_response['sources']
            news_source_results = process_results(news_source_results_list)

    return news_source_results
