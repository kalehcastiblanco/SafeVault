import hashlib

users_db = {
    "admin": {
        "password": hashlib.sha256("1234".encode()).hexdigest(),
        "role": "admin"
    },
    "user": {
        "password": hashlib.sha256("user".encode()).hexdigest(),
        "role": "user"
    }
}

def login(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()

    if username in users_db:
        if users_db[username]["password"] == hashed:
            return users_db[username]["role"]
    return None