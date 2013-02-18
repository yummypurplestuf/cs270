import os
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect(url_for('static', filename='index.html'))

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


# Assignment 1: A haphazard page showing the most common HTML tags
@app.route('/assignment-1')
def assignment_1():
    return redirect(url_for('static', filename='assignment-1.html'))

@app.route('/assignment-2')
def assignment_1():
    return redirect(url_for('static', filename='assignment-2.html'))

@app.route('/assignment-3')
def assignment_1():
    return redirect(url_for('static', filename='assignment-3.html'))

# A module runner to make our app go!
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
