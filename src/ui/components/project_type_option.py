import re

from playwright.sync_api import Locator, expect


class ProjectTypeOption:
    def __init__(self, root: Locator):
        self._root = root

    @property
    def icon(self) -> Locator:
        return self._root.locator("img")

    @property
    def name(self) -> Locator:
        return self._root.locator("div.ml-4 > span")

    @property
    def description(self) -> Locator:
        return self._root.locator("div.ml-4 > div")

    def get_name_text(self) -> str:
        return self.name.inner_text()

    def get_description(self) -> str:
        return self.description.inner_text()

    def select(self) -> None:
        self._root.click()

    def verify_is_selected(self) -> None:
        expect(self.icon).to_have_attribute("src", re.compile(r"circle-tick.svg"))


    def verify_is_not_selected(self) -> None:
        expect(self.icon).to_have_attribute("src", re.compile(r"circle.svg"))