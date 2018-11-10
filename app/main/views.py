from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_source, search_source,get_article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     #get sources
    general = get_source('general')
    technology = get_source('technology')
    business = get_source('business')
    entertainment = get_source('entertainment')
    sports = get_source('sports')

    title = 'Home - Welcome to the most informative news site online!!!'

    # search_source = request.args.get('search_query')

    return render_template('index.html', title = title, general = general, technology = technology, business = business, entertainment = entertainment, sports = sports)



@main.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display search results
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    title = f'search results for {source_name}'

    return render_template('search.html', sources = searched_sources)

    #get articles
    # article_general = get_article('general')
    # print(article_general)

    title = 'Home - Welcome to the most informative news site online!!!'
    return render_template('index.html', title = title, general = source_general)



@main.route('/source/<string:id>')
def source(id):

    '''
    View news page function that returns the news details page and its data
    '''
    source = get_article(id)
    print(source)

    return render_template('source.html',source = source)
