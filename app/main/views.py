from flask import render_template,request,redirect,url_for,abort
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
# Getting popular news
    title = 'Home - Welcome to The Best news Review Website Online'
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('.search',news_name =search_news))
    else:
        return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news )

@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for(news_name)'
    return render_template('search.html',news = searched_news)
