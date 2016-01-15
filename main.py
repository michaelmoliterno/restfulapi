#!flask/bin/python
"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, jsonify, abort, request, make_response, url_for
# We will need this for writing to NDB
from google.appengine.ext import ndb


app = Flask(__name__, static_url_path = "")
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def hello():
    return 'You found me!'

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Endpoint not found'}), 404)

@app.route('/api/tweets', methods=['POST'])
def create_tweet():

    if not request.json or not 'tweet_id' in request.json:
        return make_response(jsonify({'error': 'Invalid JSON or missing tweet_id'}), 422)

    try:
        # Build the tweet (we may want to apply Models to enforce clean/valid tweets)
        tweet = {
            'tweet_id': request.json['tweet_id'],
            'tweet_text': request.json['tweet_text']
        }

        # Add code to insert into into NDB.
        # This will also need to deal with duplicates (if the tweet is already stored)
        # insert tweet into NDB where tweet_id not in NDB

        # This response doesn't necessarily need to return this much
        return make_response(jsonify({'success': 'Tweet %s inserted to NDB!'%tweet["tweet_id"]}), 201)

    except:
        return make_response(jsonify({'error': 'Bad request','post':request.json}), 400)


# This is dummy code -- we don't necessarily need GET functions, but we might want them
tasks = [
    {
        'id': 1,
        'title': u'Sink',
        'done': False
    },
    {
        'id': 2,
        'title': u'Drain',
        'done': False
    }
]

@app.route('/api/todo', methods = ['GET'])
def get_tasks():
    return make_response(jsonify( { 'tasks': tasks } ), 200)