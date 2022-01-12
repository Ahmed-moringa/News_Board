from app import app
import urllib.request,json

from .models import article

Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

## Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(article_list):
    '''
    Function that processes the movie result and transform them to a list of Objects
    Args:
        article_list: A list of dictionaries that contain movie details
    Returns:
        article_results: A list of article objects
    '''

    article_results = []
    for article_item in article_list:
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage= article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        if urlToImage:
            article_object = Article(name,author,title,description,url,urlToImage,publishedAt)
            article_results.append(article_object)
    return article_results