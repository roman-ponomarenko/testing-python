from typing import Self

from playwright.sync_api import Locator, Page, expect

from src.config import Config


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.login_button: Locator = self.page.locator("[href*='sign_in'].login-item")

    def open(self) -> Self:
        self.page.goto(Config.TESTOMAT_URL, wait_until="networkidle")
        return self

    def is_loaded(self) -> Self:
        expect(self.login_button).to_be_visible()
        return self

    def click_login_button(self):
        self.login_button.click()
