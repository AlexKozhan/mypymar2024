import uuid


BASE_URL = "https://alexqa.netlify.app/.netlify/functions"
TOKEN = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQ"
         "iOiIxMDI4ODA4NjU4NzgwNzgzMzI5MzYiLCJpYXQiOjE3MjMx"
         "MzUzOTksImV4cCI6MTcyMzEzODk5OX0.98Gag50FX9p-BfdvUR"
         "2jbhS0nsm7JsbwxmdWmzJWDqM")

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

user_schema = {
    "type": "object",
    "properties": {
        "_id": {"type": "string"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "createdAt": {"type": "string"},
        "createdBy": {"type": ["integer", "string"]},
        "address": {"type": "string"},
        "age": {"type": "integer"},
        "phoneNumber": {"type": "string"},
        "role": {"type": "string"},
        "referralCode": {"type": "string"}
    },
    "required": ["_id", "name", "email", "createdAt", "createdBy",
                 "address", "age", "phoneNumber"]
}


def generate_unique_email():
    return f"{uuid.uuid4()}@example.com"


def user_payload():
    return {
        "name": "John Doe",
        "email": generate_unique_email(),
        "age": 30,
        "address": "123 Main St",
        "phoneNumber": "+375296789012",
        "role": "user",
        "referralCode": "ABCD1234"
    }
