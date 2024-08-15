import requests
from jsonschema import validate
import uuid
import logging


logging.basicConfig(level=logging.DEBUG)

BASE_URL = "https://alexqa.netlify.app/.netlify/functions"
TOKEN = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1"
         "c2VySWQiOiIxMDI4ODA4NjU4NzgwNzgzMzI5MzYiLC"
         "JpYXQiOjE3MjM3MTkxOTksImV4cCI6MTcyMzcyMjc5"
         "OX0.hAdT3bOHkIMpInfgcXt72XeJzgJyw97mgdXfGVzXTZg")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}


user_id = None

# JSON схема для проверки
user_schema = {
    "type": "object",
    "properties": {
        "_id": {"type": "string"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "createdAt": {"type": "string"},
        "createdBy": {
            "type": ["integer", "string"]
        },
        "address": {"type": "string"},
        "age": {"type": "integer"},
        "phoneNumber": {"type": "string"},
        "role": {"type": "string"},
        "referralCode": {"type": "string"}
    },
    "required": ["_id", "name", "email", "createdAt", "createdBy",
                 "address", "age", "phoneNumber"]
}


def log_response(response):
    logging.debug(f"Request URL: {response.request.url}")
    logging.debug(f"Request Headers: {response.request.headers}")
    logging.debug(f"Request Body: {response.request.body}")
    logging.debug(f"Response Status Code: {response.status_code}")
    logging.debug(f"Response Body: {response.text}")


def handle_response(response):
    """
        Handles the HTTP response, raising an exception
        if the status code indicates an error.

        Args:
            response (requests.Response): The HTTP response
            object to handle.

        Raises:
            Exception: If the response status code indicates
            an error (non-200).
        """
    if response.status_code >= 500:
        raise Exception(f"Server error: "
                        f"{response.status_code} - {response.text}")
    elif response.status_code == 404:
        raise Exception(f"Resource not found: {response.text}")
    elif response.status_code == 401:
        raise Exception(f"Unauthorized: {response.text}")
    elif response.status_code != 200:
        raise Exception(f"Unexpected status code: "
                        f"{response.status_code} - {response.text}")


def test_create_user():
    """
        Tests the creation of a new user by sending
        a POST request to the /createUser endpoint.

        This function generates a unique email,
        sends a POST request with the necessary user
        details, and handles the response. The
        created user's ID is stored globally for use
        in subsequent tests.

        Raises:
            Exception: If the user creation fails.
        """
    global user_id
    url = f"{BASE_URL}/createUser"
    unique_email = f"{uuid.uuid4()}@example.com"
    payload = {
        "name": "John Doe",
        "email": unique_email,
        "age": 30,
        "address": "123 Main St",
        "phoneNumber": "+375296789012",
        "role": "user",
        "referralCode": "ABCD1234"
    }

    response = requests.post(url, headers=headers, json=payload)
    log_response(response)
    handle_response(response)

    data = response.json()
    assert data.get("status") == "created"
    assert "id" in data

    user_id = data["id"]


def test_get_user():
    """
        Tests fetching user details by sending a GET
        request to the /getUser/<user_id> endpoint.

        This function verifies that a user ID was
        previously set, sends a GET request to retrieve
        the user's details, and validates the response
        against a predefined JSON schema.

        Raises:
            AssertionError: If the user ID is not set.
            jsonschema.exceptions.ValidationError:
            If the response does not match the expected schema.
        """
    global user_id
    assert user_id is not None, ("user_id должен быть установлен "
                                 "после создания пользователя")
    url = f"{BASE_URL}/getUser/{user_id}"
    response = requests.get(url, headers=headers)
    log_response(response)
    handle_response(response)

    data = response.json()
    validate(instance=data, schema=user_schema)


def test_update_user():
    """
            Tests updating an existing user's details by sending
            a PUT request to the /updateUser/<user_id> endpoint.

            This function verifies that a user ID was previously
            set, sends a PUT request with updated user details, and
            handles the response.

            Raises:
                AssertionError: If the user ID is not set.
                Exception: If the user update fails.
            """
    global user_id
    assert user_id is not None, ("user_id "
                                 "должен быть "
                                 "установлен после "
                                 "создания пользователя")
    url = f"{BASE_URL}/updateUser/{user_id}"
    payload = {
        "name": "John Smith",
        "email": f"{uuid.uuid4()}@example.com",
        "age": 31,
        "address": "456 Elm Stanciya Zavodskaya",
        "phoneNumber": "+375294578901"
    }

    response = requests.put(url, headers=headers, json=payload)
    log_response(response)
    handle_response(response)

    data = response.json()
    assert data.get("status") == "updated"


def test_delete_user():
    """
            Tests deleting an existing user by sending
            a DELETE request to the /deleteUser/<user_id> endpoint.

            This function verifies that a user ID was previously
            set, sends a DELETE request to remove the user, and
            handles the response.

            Raises:
                AssertionError: If the user ID is not set.
                Exception: If the user deletion fails.
            """
    global user_id
    assert user_id is not None, ("user_id должен быть "
                                 "установлен после создания "
                                 "пользователя")
    url = f"{BASE_URL}/deleteUser/{user_id}"
    response = requests.delete(url, headers=headers)
    log_response(response)
    handle_response(response)

    data = response.json()
    assert data.get("status") == "deleted"


def test_delete_nonexistent_user():
    """
            Tests the deletion of a nonexistent user by sending
            a DELETE request to the /deleteUser/<nonexistent_user_id>
            endpoint.

            This function attempts to delete a user that
            doesn't exist
            and verifies that the correct error is raised.

            Raises:
                AssertionError: If the error message does not match
                the expected "User not found".
            """
    url = f"{BASE_URL}/deleteUser/66a8b4aca70eafcc9d583f3e"
    response = requests.delete(url, headers=headers)
    log_response(response)
    try:
        handle_response(response)
    except Exception as e:
        assert "User not found" in str(e)


if __name__ == "__main__":
    try:
        test_create_user()
        test_get_user()
        test_update_user()
        test_delete_user()
        test_delete_nonexistent_user()
    except Exception as e:
        logging.error(f"Test failed: {e}")
