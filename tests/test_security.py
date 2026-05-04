from database.init_db import get_user_by_username

def test_sql_injection():
    malicious = "' OR 1=1 --"
    result = get_user_by_username(malicious)
    
    assert result is None