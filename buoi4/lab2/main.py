import os
from api_gateway.gateway import APIGateway
from token_manager.manager import TokenManager

if __name__ == "__main__":
    jwt_secret = os.getenv("JWT_SECRET", "super" + "secret")
    manager = TokenManager(jwt_secret)
    access_token, refresh_token = manager.generate_tokens("phuoc")

    print("Access Token:", access_token)
    print("Refresh Token:", refresh_token)

    gateway = APIGateway(jwt_secret)
    gateway.run()
