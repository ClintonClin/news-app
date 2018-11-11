from flask import render_template
from flask import Flask
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'HOME- find all your news under one roof'
    return render_template('index.html', killer=title)

    
