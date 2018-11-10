import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_API_ARTICLE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
