from app.main import pretty_json
import json


def test_pretty_json(client):
    response = client.get('/')
    payload = {
        "current_uri": "/",
        "resources": {
            "users": "/users",
            "user": "/users/<username>",
        }
    }
    test = pretty_json(payload)
    assert json.loads(test.data) == payload
