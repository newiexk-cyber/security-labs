import jwt
from token_manager.manager import TokenManager

def test_token_creation_and_refresh():
    tm_key = "key" + "123"
    manager = TokenManager(tm_key)
    access, refresh = manager.generate_tokens("user1")

    payload = jwt.decode(access, tm_key, algorithms=["HS256"])
    assert payload["sub"] == "user1"
    assert payload["type"] == "access"

    new_access = manager.refresh_access_token(refresh)
    assert new_access is not None
