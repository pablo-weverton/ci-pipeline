#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import make_response
from loguru import logger

import json
from werkzeug.exceptions import NotFound
from collections import OrderedDict

app = Flask(__name__)

with open("app/users.json", "r") as f:
    users = json.load(f)


@app.route("/", methods=['GET'])
def index():
    return pretty_json({
        "resources": {
            "users": "/users",
            "user": "/users/<username>",
        },
        "current_uri": "/"
    })


@app.route("/users", methods=['GET'])
def all_users():
    formatted_data = OrderedDict(sorted(users.items()))
    for key, value in formatted_data.items():
        if 'id' in value:
            value.pop('id')
    return pretty_json(formatted_data)


@app.route("/users/<username>", methods=['GET'])
def user_data(username):
    if username not in users:
        raise NotFound(username)

    return pretty_json(users[username])


@app.route("/users/<username>/<something>", methods=['GET'])
def user_something(username, something):
    if something not in users[username]:
        raise NotFound
    return pretty_json(users[username][something])


def pretty_json(arg):
    response = make_response(json.dumps(arg, sort_keys=True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response


if __name__ == "__main__":
    app.run(port=5000)
