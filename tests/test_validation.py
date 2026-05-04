from security.validation import validate_username

def test_valid_username():
    assert validate_username("user123")

def test_invalid_username():
    assert not validate_username("user<script>")