import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code == 302  # Redirect to login

def test_register_and_login(client):
    client.post('/register', data={
        'username': 'testuser',
        'password': 'TestPass123!',
        'role': 'user'
    })
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'TestPass123!'
    }, follow_redirects=True)
    assert b'Dashboard' in response.data
