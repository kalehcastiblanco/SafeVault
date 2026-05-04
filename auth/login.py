import hashlib
from database.init_db import get_user_by_username

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(username, password):
    user = get_user_by_username(username)

    if not user:
        return None

    db_user, db_pass, role = user

    if hash_password(password) == db_pass:
        return {
            "username": db_user,
            "role": role
        }

    return None