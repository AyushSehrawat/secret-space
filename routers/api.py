import hmac
import hashlib
from datetime import datetime
from fastapi import APIRouter, Request, Response

router = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)


def sign(secret: str, message: str, version: str) -> str:
    unix_timestamp = str(int(datetime.utcnow().timestamp()))
    return hmac.new(
        secret.encode("utf-8"),
        f"{version}"
        f"\n{message}"
        f"\n{unix_timestamp}".encode("utf-8"),
        hashlib.sha256
    ).hexdigest()


def hashpass(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

@router.get("/sign/{username}/{password}")
def sign_message(request : Request, response : Response, username : str, password : str):
    if "auth-cookie" in request.cookies:
        return {"message": "You are already signed in"}

    max_age = 3600 * 24 * 7

    auth_cookie = sign("secret", username, "v0")
    response.set_cookie(
        key="auth-cookie",
        value=auth_cookie,
        max_age=max_age,
        expires=max_age,
        httponly=True,
    )

    return {
        "Logged in as": username,
        "auth-cookie": auth_cookie,
        "password": hashpass(password)
    }