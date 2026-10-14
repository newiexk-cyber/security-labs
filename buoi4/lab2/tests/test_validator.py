import jwt
import datetime
from jwt_validator.validator import JWTValidator

def generate_token(sign_key):
    now = datetime.datetime.now(datetime.timezone.utc)
    payload = {"sub": "test", "exp": now + datetime.timedelta(minutes=5)}
    return jwt.encode(payload, sign_key, algorithm="HS256")

def test_valid_token():
    v_key = "secret" + "123"
    token = generate_token(v_key)
    validator = JWTValidator(v_key)
    result = validator.validate(token)
    assert result["valid"] is True
    assert result["payload"]["sub"] == "test"

def test_invalid_signature():
    token = generate_token("wrong" + "secret")
    validator = JWTValidator("correct" + "secret")
    result = validator.validate(token)
    assert result["valid"] is False
