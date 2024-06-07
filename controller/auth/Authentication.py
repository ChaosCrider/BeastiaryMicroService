from datetime import datetime
from config import db, app
from models.user import User
from models.plan import Plan

import jwt
import hashlib


key = "bdebGRAPE1256"
algo = "HS256"


def encode(payload):
    """
    Creates a token from a json sent to it.
    :param payload: JSON
    :return: An encoded token
    """
    date_time = datetime.now()
    expires = date_time.timestamp() # + 2629743
    encoded = jwt.encode({"exp": expires, "payload": payload}, key, algorithm=algo)
    return encoded


def decode(token):
    """
    Decode a token and return a json
    :param token: a JWT token with the proper algorythm
    :return: the original payload
    """
    try:
        decoded = jwt.decode(token, key, algorithms=algo)
        return decoded
    except jwt.ExpiredSignatureError as e:
        print("e:", e)
        return e


def hash_string(data):
    """
    takes in a string, and returns a corresponding hash.
    Intended to hash passwords.
    :param data:
    :return:
    """
    encoded_data = data.encode()
    hashed_data = hashlib.md5(encoded_data, usedforsecurity=True)
    return hashed_data.hexdigest()


def authorize_consume(token):
    pass

if __name__ == "__main__":
    test1 = encode({"name": "Bruno", "password": "bdeb", "id": "1"})
    print(test1)
    print(decode(test1))
    print(hash_string("Bruno"))
