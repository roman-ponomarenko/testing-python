from dataclasses import dataclass

from decouple import config


@dataclass(frozen=True)
class Config:
    TESTOMAT_URL: str = config('TESTOMAT_URL')
    TESTOMAT_BASE_APP_URL: str = config('TESTOMAT_BASE_APP_URL')
    TESTOMAT_SIGN_IN_URL: str = f"{config('TESTOMAT_BASE_APP_URL')}/users/sign_in"
    TESTOMAT_USERNAME: str = config("TESTOMAT_USERNAME")
    TESTOMAT_PASSWORD: str = config("TESTOMAT_PASSWORD")

    PW_SLOWMO: int = config("PW_SLOWMO", default=100, cast=int)
    PW_TIMEOUT: int = config("PW_TIMEOUT", default=60_000, cast=int)
    PW_EXPECT_TIMEOUT: int = config("PW_EXPECT_TIMEOUT", default=20_000, cast=int)
    PW_HEADLESS: bool = config("PW_HEADLESS", default=False, cast=bool)
    PW_BROWSER: str = config("PW_BROWSER", default="chrome")
    PW_RATE_LIMIT_TIMEOUT: int = config("PW_RATE_LIMIT_TIMEOUT", default=3000, cast=int)
