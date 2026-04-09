import jwt
from pwdlib import PasswordHash
from datetime import timedelta, datetime, UTC

from config import settings


# uv add "pwdlib[argon2]" pydantic-settings pyjwt

# Why hashing and not encryption?
# Encryption is reversible, Hashing is not. even if db is stolen password can be recovered from hashes
# argon2 generates random salt for same password. each is unique. 

password_hasher = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hasher.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hasher.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:  # data = {"sub": str(user.id)}
    ''' Create a JWT access token. '''

    # in case expiry time is None
    if expires_delta:
        expires = datetime.now(UTC) + expires_delta
    else:
        expires = datetime.now(UTC) + timedelta(minutes=settings.access_token_expire_minutes)
    
    to_encode = data.copy()
    to_encode.update({"exp": expires})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key.get_secret_value(),
        algorithm=settings.algorithm,
    )

    return encoded_jwt


def verify_access_token(access_token: str) -> str | None:
    ''' Verifies a JWT token and returns the user id if it is valid '''

    try:
        payload = jwt.decode(
            access_token,
            settings.secret_key.get_secret_value(),
            algorithms=[settings.algorithm],
            options={"require": ["exp", "sub"]}   
        )
    except jwt.InvalidTokenError:
        return None
    else:
        payload.get("sub")
