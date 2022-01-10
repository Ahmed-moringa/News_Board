from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/article/<article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('movie.html',id = article_id)