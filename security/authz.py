def authorize(user, required_role):
    if not user:
        return False
    
    return user["role"] == required_role