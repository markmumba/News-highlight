class Article:
    '''
    news_Article class to define news_Article Objects
    
    '''

    def __init__(self,article_id,title,description,articleurl,content):
        self.article_id = article_id
        self.title = title
        self.description = description
        self.articleurl = articleurl
        self.content = content