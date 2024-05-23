import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    """Fixture for the base URL of the API."""
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def auth_token():
    """Fixture to get an authentication token (if required)."""
    url = "https://example.com/api/auth"
    data = {"username": "user", "password": "pass"}
    response = requests.post(url, data=data)
    return response.json()["token"]

@pytest.fixture
def headers(auth_token):
    """Fixture to provide headers including the auth token."""
    return {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
