import os
from flask import Flask, redirect, url_for

# A Flask app instance
app = Flask(__name__)


# Route requests to the top level... say Hello



# Assignment 1: A haphazard page showing the most common HTML tags
@app.route('/', '/assignment-1', '/assignment-2', '/assignment-3')

def index():
    return redirect(url_for('/', filename='/'))

def assignment_1():
    return redirect(url_for('static', filename='assignment-1.html'))
    <a href="/static/assignment-1.html">assignment-1</a>

def assignment_1():
    return redirect(url_for('static', filename='assignment-1.html'))
    <a href="/static/assignment-2.html">assignment-2</a>

def assignment_1():
    return redirect(url_for('static', filename='assignment-1.html'))
    <a href="/static/assignment-3.html">assignment-3</a>

# A module runner to make our app go!
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
