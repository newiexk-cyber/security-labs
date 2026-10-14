import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError, InvalidSignatureError

class JWTValidator:
    def __init__(self, secret, algorithms=None):
        self.secret = secret
        self.algorithms = algorithms or ["HS256"]

    def validate(self, token: str):
        try:
            payload = jwt.decode(token, self.secret, algorithms=self.algorithms)
            return {"valid": True, "payload": payload}
        except ExpiredSignatureError:
            return {"valid": False, "reason": "Token expired"}
        except InvalidSignatureError:
            return {"valid": False, "reason": "Invalid signature"}
        except InvalidTokenError as e:
            return {"valid": False, "reason": str(e)}
