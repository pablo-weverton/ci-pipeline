import json
from urllib.request import urlopen


def test_default_route(client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_all_users_route(client):
    resp = client.get('/users')
    assert resp.status_code == 200


def test_user_data_route(client):
    resp = client.get(f'/users/geralt')
    assert resp.status_code == 200


def test_users_data_property_route(client):
    resp = client.get('/users/lara_croft/description')
    assert resp.status_code == 200

