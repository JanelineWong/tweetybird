
# app.py
from flask import Flask, request, jsonify
from tweettweet import get_tweets_by_name, get_tweets_by_word

app = Flask(__name__)

@app.route('/handle')
def respond():
    handle = request.args.get('name')
    return jsonify(get_tweets_by_name(handle))

@app.route('/search')
def lookfor():
    look = request.args.get('word')
    return jsonify(get_tweets_by_word(look))

# A welcome message to test our server
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
<head>
   <title>Endpoint</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
</head>
<body style="width: 880px; margin: auto;">  
    <h1>Welcome to a kid-friendly zone</h1>
    <p>This is our endpoint for GET requests</p>
    <p>And here's an image:</p>
    <a href="https://www.flickr.com/photos/81191171@N04/8402256318">
        <img src="https://live.staticflickr.com/8189/8402256318_775f7567b9_z.jpg" alt="Oh how cute">
    </a>
</body>
"""

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
