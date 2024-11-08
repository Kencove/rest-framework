import time

from base64 import b64encode

import requests
from jose import jwt

# /usr/bin/env python3
import time

import requests
from jose import jwt
import json

#######################################################
#######################################################

token = jwt.encode(
    {
        "aud": "auth_jwt_test_api",
        "iss": "theissuer",
        "exp": time.time() + 60,
        "email": "mark.brown23@example.com",
    },
    key="thesecret",
    algorithm=jwt.ALGORITHMS.HS256,
)
r = requests.get(
    "http://localhost:8069/auth_jwt_model/whoami",
    headers={"Authorization": f"Bearer {token}"},
)
r.raise_for_status()
print("Who am I test: ===>")
print(r.json())

#######################################################
#######################################################

token = jwt.encode(
    {
        "aud": "auth_jwt_test_api",
        "iss": "theissuer",
        "exp": time.time() + 60,
        "email": "mark.brown23@example.com",
    },
    key="thesecret",
    algorithm=jwt.ALGORITHMS.HS256,
)
r = requests.get(
    "http://localhost:8069/fastapi_auth_jwt_model/whoami",
    headers={"Authorization": f"Bearer {token}"},
)
r.raise_for_status()
print("Who am I API: ===>")
print(r.json())

#######################################################
#######################################################

token = jwt.encode(
    {
        "aud": "auth_jwt_test_api",
        "iss": "theissuer",
        "exp": time.time() + 60,
        "email": "mark.brown23@example.com",
    },
    key="thesecret",
    algorithm=jwt.ALGORITHMS.HS256,
)
r = requests.get(
    "http://localhost:8069/fastapi_auth_jwt_model/whoami-public-or-jwt",
    headers={"Authorization": f"Bearer {token}"},
)
r.raise_for_status()
print("Who am I public or JWT API: ===>")
print(r.json())

#######################################################
#######################################################

print("\n", "\n", "\n")

token = jwt.encode(
    {
        "aud": "auth_jwt_test_api",
        "iss": "theissuer",
        "exp": time.time() + 60,
        "email": "mark.brown23@example.com",
    },
    key="thesecret",
    algorithm=jwt.ALGORITHMS.HS256,
)
r = requests.get(
    "http://localhost:8069/fastapi_auth_jwt_model/customer",
    headers={"Authorization": f"Bearer {token}"},
)
r.raise_for_status()
print("Customer Get Mobile Info API: ===>")
print(r.json(), end="\n")

#######################################################
#######################################################

token = jwt.encode(
    {
        "aud": "auth_jwt_test_api",
        "iss": "theissuer",
        "exp": time.time() + 60,
        "email": "mark.brown23@example.com",
    },
    key="thesecret",
    algorithm=jwt.ALGORITHMS.HS256,
)
content=json.dumps(
    {
        "mobile": "123456",
    }
)
r = requests.post(
    "http://localhost:8069/fastapi_auth_jwt_model/customer",
    headers={"Authorization": f"Bearer {token}"},
    data=content,
)
r.raise_for_status()
print("Customer Update Mobile Info API: ===>")
print(r.json(), end="\n")

#######################################################
#######################################################

token = jwt.encode(
    {
        "aud": "auth_jwt_test_api",
        "iss": "theissuer",
        "exp": time.time() + 60,
        "email": "mark.brown23@example.com",
    },
    key="thesecret",
    algorithm=jwt.ALGORITHMS.HS256,
)
content=json.dumps(
    {
        "mobile": None,
    }
)
r = requests.post(
    "http://localhost:8069/fastapi_auth_jwt_model/customer",
    headers={"Authorization": f"Bearer {token}"},
    data=content,
)
r.raise_for_status()
print("Customer Reset Mobile Info API: ===>")
print(r.json(), end="\n")
