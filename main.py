from security.validation import validate_username, validate_email, sanitize_input
from auth.login import login
from security.sql_queries import get_user_by_username


def test_validation():
    print("\n=== VALIDATION TESTS ===")

    usernames = ["admin", "user_123", "<script>hack</script>"]
    emails = ["test@email.com", "bademail@", "user@domain.com"]

    for u in usernames:
        print(f"Username: {u} -> {validate_username(u)}")

    for e in emails:
        print(f"Email: {e} -> {validate_email(e)}")


def test_login():
    print("\n=== LOGIN TESTS ===")

    print(login("admin", "1234"))   # admin
    print(login("user", "user"))    # user
    print(login("hack", "123"))     # None


def test_sanitization():
    print("\n=== SANITIZATION TESTS ===")

    inputs = [
        "<script>alert('x')</script>",
        "' OR 1=1 --",
        "normal_input"
    ]

    for i in inputs:
        print(f"{i} -> {sanitize_input(i)}")


def test_database():
    print("\n=== DATABASE TEST ===")

    try:
        result = get_user_by_username("admin")
        print("DB Result:", result)
    except Exception as e:
        print("Database error (expected if DB not configured):", e)


def run_all_tests():
    test_validation()
    test_login()
    test_sanitization()
    test_database()


if __name__ == "__main__":
    print("SAFEVAULT - INTEGRATED TEST RUNNER")
    run_all_tests()