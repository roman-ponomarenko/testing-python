import functools
import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@functools.cache
def get_env(key: str) -> str:
    """Get the required environment variable or raise ValueError if missing."""
    value = os.getenv(key)
    if not value:  # Handles both None and empty string
        raise ValueError(f"Required environment variable '{key}' is missing")
    return value


@dataclass(frozen=True)
class Config:
    TESTOMAT_URL: str = get_env("TESTOMAT_URL")
    TESTOMAT_SIGN_IN_URL: str = f"{get_env('TESTOMAT_BASE_APP_URL')}/users/sign_in"
    TESTOMAT_USERNAME: str = get_env("TESTOMAT_USERNAME")
    TESTOMAT_PASSWORD: str = get_env("TESTOMAT_PASSWORD")
