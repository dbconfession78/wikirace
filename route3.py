#!/usr/bin/python3
"Set up route for wiki race method"
from winki import start
from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def route(n):
    pass

@app.route('/<skeyword>/search', methods=["GET"], strict_slashes=False)
def search(skeyword):
    return (jsonify(start(skeyword)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
