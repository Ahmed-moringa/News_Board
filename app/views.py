from flask import render_template, request, redirect
from app import app
from .request import get_sources ,get_articles

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting categories
    message = 'Home - Welcome to fast reliable News Board'
    news_sources = get_sources()
    return render_template('index.html' ,message = message,news_sources = news_sources)

@app.route('/articles/<source_id>')
def articles(source_id):
    '''
    View article page function that returns the article details page and its data
    '''
    title = f"{source_id} page"
    articles = get_articles(source_id)
    return render_template('articles.html', articles = articles)