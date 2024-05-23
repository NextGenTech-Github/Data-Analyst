import requests

def test_get_users(base_url):
    url = f"{base_url}/users"
    response = requests.get(url)
    
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for user in data:
        assert "id" in user
        assert "name" in user
        assert "email" in user

def test_get_user_by_id(base_url):
    user_id = 1
    url = f"{base_url}/users/{user_id}"
    response = requests.get(url)
    
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    
    user = response.json()
    assert user["id"] == user_id
    assert "name" in user
    assert "email" in user

def test_create_user(base_url, headers):
    url = f"{base_url}/users"
    payload = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com"
    }
    response = requests.post(url, headers=headers, json=payload)
    
    assert response.status_code == 201
    user = response.json()
    assert user["name"] == "John Doe"
    assert user["username"] == "johndoe"
    assert user["email"] == "johndoe@example.com"
