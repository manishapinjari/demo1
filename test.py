import pytest
from app import app
from werkzeug.urls import url_quote

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_app_is_working(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello CI CD World!" in response.data
