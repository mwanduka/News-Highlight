import urllib.request,json
from .models import News

# News = news.News

# Getting api key
api_key = None

# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_result_list = get_news_response['results']
            news_results = process_results(news_result_list)
            print(news_results)
    return news_results

def process_results(news_list):
    '''
    Function that processes the news result and transform them to a list of Objects

    Args:
        news_list:A list of dictionaries that contain news details

    Returns:
        news_list: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_details_response.get('id')
        authour = news_item.get('authour')
        title = news_details_response.get('original_title')
        description = news_item.get('description')
        publishedAt = news_item.get('publishedAt')
        poster = news_item.get('poster_path')
        content = news_item.get('content')


        if poster:
            news_object = news(id,title,authour,publishedAt,description)
            news_results.append(news_object)/

    return news_results

def get_news(id):
    get_news_details_url = base_url.format(id,api_key)
    print()

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            authour = news_item.get('authour')
            title = news_details_response.get('original_title')
            description = news_item.get('description')
            publishedAt = news_item.get('publishedAt')
            poster = news_item.get('poster_path')


            news_object = news(id,title,authour,publishedAt,description)
        return news_object
