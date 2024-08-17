import logging

logging.basicConfig(level=logging.DEBUG)


def log_response(response):
    logging.debug(f"Request URL: {response.request.url}")
    logging.debug(f"Request Headers: {response.request.headers}")
    logging.debug(f"Request Body: {response.request.body}")
    logging.debug(f"Response Status Code: {response.status_code}")
    logging.debug(f"Response Body: {response.text}")


def handle_response(response):
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
