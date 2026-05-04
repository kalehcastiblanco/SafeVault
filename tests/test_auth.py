from auth.login import login

def test_login_success():
    assert login("admin", "Admin123") is not None

def test_login_fail():
    assert login("admin", "wrong") is None