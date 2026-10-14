import jwt
import tempfile
import os
from jwt_cracker.cracker import JWTCracker

def test_crack_token():
    target_secret = "super" + "secret"
    token = jwt.encode({"sub": "test"}, target_secret, algorithm="HS256")

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write("wrongpass\n123456\nsupersecret\n")
        f.seek(0)
        cracker = JWTCracker(token, f.name)
        found = cracker.crack()

    assert found == "supersecret"
