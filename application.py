from flask import Flask, render_template, request
from flask import redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

from flask import session as login_session
import random
import string

#import httplib2
import json
from flask import make_response
import requests

application = Flask(__name__)
application.secret_key = 'super_secret_key'

# Connect to MySQL and create session
engine = create_engine('mysql+pymysql://mbpdbuser:Macron2020!@mbpdb.cs31k7t8tcwk.us-east-2.rds.amazonaws.com:3306/mbpdb')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@application.route('/')
def showHome():
    return render_template('main.html') #'Hola! I am working on Flask'


# Show categories
@application.route('/category')
def showCategory():
    category = session.query(Category)
    item = session.query(Item)
    return render_template('categories.html', category=category, item=item)



# Create a category
@application.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Category(name=['Tennis'], user_id=['2'])
        session.add(newCategory)
        flash('New Category %s Successfully created' % newCategory.name)
        session.commit()
        return '<p>Category created</p>'
    else:
        return '<p>Hola! No categoria</p>'

        
# === Old code === #
# print a nice greeting.
#def say_hello(username = "World"):
#    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
#header_text = '''
#    <html>\n<head> <title>EB Flask Testing</title> </head>\n<body>'''
#instructions = '''
#    <p><em>Hint</em>: This is a RESTful web service test! say hola...
#    someone specific.</p>\n'''
#home_link = '<p><a href="/">Back</a></p>\n'
#footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
#application = Flask(__name__)

# add a rule for the index page.
#application.add_url_rule('/', 'index', (lambda: header_text +
#    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
#application.add_url_rule('/<username>', 'hello', (lambda username:
#    header_text + say_hello(username) + home_link + footer_text))
# === End Old Code === #


# Run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
