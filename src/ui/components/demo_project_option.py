import re

from playwright.sync_api import Locator, expect


class DemoProjectOption:
    def __init__(self, root: Locator):
        self._root = root

    @property
    def icon(self) -> Locator:
        return self._root.locator("img")

    def get_id(self) -> str:
        return self._root.get_attribute("id") or ""

    def get_name_text(self) -> str:
        return self._root.locator("img + div").inner_text().strip()

    def select(self) -> None:
        self._root.click()

    def verify_is_selected(self) -> None:
        expect(self.icon).to_have_attribute("src", re.compile(r"circle-tick.svg"))

    def verify_is_not_selected(self) -> None:
        expect(self.icon).to_have_attribute("src", re.compile(r"circle.svg"))
