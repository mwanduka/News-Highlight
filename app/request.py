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
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_source(language):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['results']:

            source_result_list = get_source_response['results']
            source_results = process_results(source_result_list)
            print(source_results)
    return source_results

def get_article(category):
    '''
    Function that gets the json response to our url request
    '''
    get__url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['results']:
            article_result_list = get_article_response['results']
            article_results = process_results(article_result_list)
            print(article_results)
    return article_results


def process_results(source_list):
    '''
    Function that processes the source result and transform them to a list of Objects

    Args:
        source_list:A list of dictionaries that contain source details

    Returns:
        source_list: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_details_response.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = category_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = source(id,title,authour,publishedAt,description)
            source_results.append(source_object)

    return source_results

def process_results(article_list):
    '''
    Function that processes the article result and transform them to a list of Objects

    Args:
        article_list:A list of dictionaries that contain article details

    Returns:
        article_list: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_details_response.get('id')
        authour = article_item.get('authour')
        title = article_details_response.get('original_title')
        description = article_item.get('description')
        url = url_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')


        if url:
            article_object = article(id,title,authour,publishedAt,description)
            article_results.append(article_object)

    return article_results
