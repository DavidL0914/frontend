from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import requests
import random

from model.quotes import *

quote_api = Blueprint('quote_api', __name__,
                   url_prefix='/api/quotes')

api = Api(quote_api)

class QuotesAPI:
    # Not implemented
    class _Create(Resource):
        def post(self, quote):
            pass

    # Get all quotes
    class _Read(Resource):
        def get(self):
            return jsonify(getQuotes())

    # Get a quote by ID
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getQuote(id))

    # Get a random quote
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomQuote())

    # Get the count of quotes
    class _ReadCount(Resource):
        def get(self):
            count = countQuotes()
            countMsg = {'count': count}
            return jsonify(countMsg)

# Define the addUpvoteQuote and addDownvoteQuote functions
def addUpvoteQuote(quote_id):
    quote = getQuote(quote_id)
    if quote:
        quote["upvotes"] += 1
    return quote

def addDownvoteQuote(quote_id):
    quote = getQuote(quote_id)
    if quote:
        quote["downvotes"] += 1
    return quote

# Add an upvote to a quote
class _UpdateLike(Resource):
    def put(self, id):
        upvoted_quote = addUpvoteQuote(id)
        return jsonify(upvoted_quote)

# Add a downvote to a quote
class _UpdateDislike(Resource):
    def put(self, id):
        downvoted_quote = addDownvoteQuote(id)
        return jsonify(downvoted_quote)


api.add_resource(QuotesAPI._Create, '/create/<string:quote>')
api.add_resource(QuotesAPI._Read, '/')
api.add_resource(QuotesAPI._ReadID, '/<int:id>')
api.add_resource(QuotesAPI._ReadRandom, '/random')
api.add_resource(QuotesAPI._ReadCount, '/count')
api.add_resource(QuotesAPI._UpdateLike, '/like/<int:id>')
api.add_resource(QuotesAPI._UpdateDislike, '/dislike/<int:id>')

if __name__ == "__main__":
    # Define the server URL
    server = 'https://your-server-url.com'  # Change to your server URL
    url = server + "/api/quotes"
    responses = []

    # Get the count of quotes on the server
    count_response = requests.get(url + "/count")
    count_json = count_response.json()
    count = count_json['count']

    # Test like and dislike operations
    num = str(random.randint(0, count - 1))
    responses.append(requests.get(url + "/" + num))
    responses.append(requests.put(url + "/like/" + num))
    responses.append(requests.put(url + "/dislike/" + num))

    # Get a random quote
    responses.append(requests.get(url + "/random"))

    # Cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")
