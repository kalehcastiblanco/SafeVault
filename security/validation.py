import re
import html

def validate_username(username):
    return re.match(r"^[a-zA-Z0-9_]{3,20}$", username)

def validate_password(password):
    return len(password) >= 8

def sanitize_output(data):
    return html.escape(data)