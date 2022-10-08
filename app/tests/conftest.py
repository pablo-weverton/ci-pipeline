import pytest
from app.main import app
from app import config


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

