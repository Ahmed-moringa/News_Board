from flask import render_template
from app import app
from .request import get_articles

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    popular_articles = get_articles('popular')
    message = 'Home - Welcome to fast reliable News Board'
    return render_template('index.html' ,message = message,popular = popular_articles)

@app.route('/article/<article_id>')
def article(article_id):
    '''
    View article page function that returns the article details page and its data
    '''
    title = f'You are viewing {article_id}'
    return render_template('article.html', title = title)