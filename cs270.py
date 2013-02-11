import os
from flask import Flask, redirect, url_for

# A Flask app instance
app = Flask(__name__)


# Route requests to the top level... say Hello
@app.route('/')
def index():
    return 'Hello, World'


# Assignment 1: A haphazard page showing the most common HTML tags
@app.route('/assignment-1')
def assignment_1():
    return redirect(url_for('static', filename='assignment-1.html'))

# A module runner to make our app go!
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
