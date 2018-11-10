import urllib.request,json
from .models import Source
from .models import Article

# Source = source.Source
# Article = article.Article

# Getting api key
api_key = None

# Getting the news base url
base_url = None

def configure_request(app):
    global api_key, source_url, article_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_API_SOURCE_URL']
    article_url = app.config['NEWS_API_ARTICLE_URL']

def get_source(source):
    '''
    Function to get json to respond to url request
    '''

    the_url = source_url.format(source,api_key)
    # print(the_url)

    with urllib.request.urlopen(the_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)
            # print(source_results)

    return source_results

def process_results(source_results_list):
    '''
    This function processes the source results and transfers them to a list of objects

    Args:
        source_list: list of dictionaties that contain news_source details
    Returns:
        source_results: list of source objects
    '''
    source_results = []
    for source_item in source_results_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        new_stuff = Source(id, name, description, url, category, language, country)
        source_results.append(new_stuff)
        print(source_results)

    return source_results

def search_source(source_name):

    search_source_url = 'https://newsapi.org/v2/sources?category={}&apiKey={}'.format(api_key, source_name)
    with urllib.request.urlopen(search_source_url) as url:
        search_source_data = url.read()
        search_source_response = json.loads(search_source_data)

        search_source_results = None

        if search_source_response['sources']:
            search_source_list = search_source_response['sources']
            search_source_results = process_results (search_source_list)

    return search_source_results

def get_article(id):
    '''
    Function to get json to respond to url request
    '''
    get_article_url=article_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(article_results_list):
    '''
    This function processes the articles results and transfers them to a list of objects

    Args:
        article_list: dictionaties that contain article details
    Returns:
        article_results: article objects
    '''
    article_results = []
    for article_item in article_results_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if urlToImage:
            article_object = Article(id, name, author, title, description, url, urlToImage, publishedAt)
            article_results.append(article_object)

    return article_results  
