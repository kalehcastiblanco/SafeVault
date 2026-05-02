import re

def validate_username(username):
    if not username:
        return False
    return bool(re.match("^[a-zA-Z0-9_]{3,20}$", username))


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))


def sanitize_input(user_input):
    dangerous = ["<", ">", "'", "\"", ";", "--", "script"]
    for d in dangerous:
        user_input = user_input.replace(d, "")
    return user_input