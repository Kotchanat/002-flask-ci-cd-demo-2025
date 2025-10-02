import pytest
from app import app as flask_app   # import ตัวแปร app มาเป็น flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Hello World!'
    assert data['status'] == 'running'

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'database' in data
    assert 'redis' in data

def test_math_operations():
    assert 1 + 1 == 2
    assert 2 * 3 == 6
