import requests
from jsonschema import validate
from test_data import BASE_URL, HEADERS, user_schema, user_payload
from utils import log_response, handle_response

user_id = None


def test_create_user():
    global user_id
    url = f"{BASE_URL}/createUser"
    payload = user_payload()

    response = requests.post(url, headers=HEADERS, json=payload)
    log_response(response)
    handle_response(response)

    data = response.json()
    assert data.get("status") == "created"
    assert "id" in data

    user_id = data["id"]


def test_get_user():
    global user_id
    assert user_id is not None, "user_id должен быть установлен после создания пользователя"
    url = f"{BASE_URL}/getUser/{user_id}"

    response = requests.get(url, headers=HEADERS)
    log_response(response)
    handle_response(response)

    data = response.json()
    validate(instance=data, schema=user_schema)


def test_update_user():
    global user_id
    assert user_id is not None, "user_id должен быть установлен после создания пользователя"
    url = f"{BASE_URL}/updateUser/{user_id}"
    payload = user_payload()
    payload["name"] = "John Smith"
    payload["age"] = 31
    payload["address"] = "456 Elm Stanciya Zavodskaya"
    payload["phoneNumber"] = "+375294578901"

    response = requests.put(url, headers=HEADERS, json=payload)
    log_response(response)
    handle_response(response)

    data = response.json()
    assert data.get("status") == "updated"


def test_delete_user():
    global user_id
    assert user_id is not None, "user_id должен быть установлен после создания пользователя"
    url = f"{BASE_URL}/deleteUser/{user_id}"

    response = requests.delete(url, headers=HEADERS)
    log_response(response)
    handle_response(response)

    data = response.json()
    assert data.get("status") == "deleted"


def test_delete_nonexistent_user():
    url = f"{BASE_URL}/deleteUser/66a8b4aca70eafcc9d583f3e"

    response = requests.delete(url, headers=HEADERS)
    log_response(response)
    try:
        handle_response(response)
    except Exception as e:
        assert "User not found" in str(e)
