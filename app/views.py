from flask import render_template
from flask.helpers import get_root_path
from app import app
from .request import get_articles

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting categories
    buisness_articles = get_articles('buisness')
    sports_articles = get_articles('sports')
    general_articles = get_articles('general')
    message = 'Home - Welcome to fast reliable News Board'
    return render_template('index.html' ,message = message,buisness = buisness_articles,sports = sports_articles,general = general_articles)

@app.route('/article/<article_id>')
def article(article_id):
    '''
    View article page function that returns the article details page and its data
    '''
    title = f'You are viewing {article_id}'
    return render_template('article.html', title = title)