from typing import Self

from playwright.sync_api import Page, expect

from src.config import Config


class LoginPage:
    def __init__(self, page: Page):
        self._page = page

    def open(self) -> Self:
        self._page.goto(Config.TESTOMAT_SIGN_IN_URL)
        return self

    def is_loaded(self) -> Self:
        expect(self._page.locator("#content-desktop #new_user")).to_be_visible()
        return self

    def login(self, email: str, password: str) -> None:
        self._page.locator("#content-desktop #user_email").fill(email)
        self._page.locator("#content-desktop #user_password").fill(password)
        self._page.get_by_role(role="button", name="Sign in").click()

    def verify_invalid_login_message(self) -> None:
        expect(self._page.locator("#content-desktop p:has-text('Invalid Email or password.')")).to_be_visible()
