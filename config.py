from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    # checks 1. system env variable, if not found, 2. .env file, 3. default value set here
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    # generate a secret key: "python3 -c "import secrets; print(secrets.token_hex(32))""
    secret_key: SecretStr   # # SecretStr wont leak the value in logs or when printed. TO get value - get_secret_value() 
    access_token_expire_minutes: int = 30   # even if it is a str in .env pydantic willl automatically typecast it
    algorithm: str = "HS256"


settings = Settings()   # Loads from the .env file
