from app.main import app


def test_app_is_created():
    assert app.name == 'app.main'


def test_request_returns_404(client):
    assert client.get("/url_that_doesn't_exist").status_code == 404
