from typing import Self

from playwright.sync_api import Locator, expect


class ReadmePanel:
    def __init__(self, root: Locator):
        self._root = root

    def is_loaded(self) -> Self:
        expect(self.content).to_be_visible()
        expect(self.edit_button).to_be_visible()
        expect(self.lets_start_button).to_be_visible()
        return self

    # -------------------------
    # Elements
    # -------------------------

    @property
    def close_button(self) -> Locator:
        return self._root.locator(".back button.third-btn")

    @property
    def breadcrumb(self) -> Locator:
        return self._root.locator(".detail-view-pwd span")

    @property
    def edit_button(self) -> Locator:
        return self._root.locator("a.secondary-btn", has_text="Edit")

    @property
    def header_close_button(self) -> Locator:
        return self._root.locator(".detail-view-actions button.third-btn")

    @property
    def content(self) -> Locator:
        return self._root.locator(".detail-view-content .markdown")

    @property
    def lets_start_button(self) -> Locator:
        return self._root.locator(".detail-view-content a.primary-btn", has_text="let's start")

    # -------------------------
    # Queries
    # -------------------------

    def get_breadcrumb_text(self) -> str:
        return self.breadcrumb.inner_text().strip()

    def get_content_text(self) -> str:
        return self.content.inner_text()

    def get_edit_href(self) -> str:
        return self.edit_button.get_attribute("href") or ""

    def get_lets_start_href(self) -> str:
        return self.lets_start_button.get_attribute("href") or ""

    def is_visible(self) -> bool:
        return self._root.is_visible()

    # -------------------------
    # Actions
    # -------------------------

    def close(self) -> None:
        self.close_button.click()

    def click_edit(self) -> None:
        self.edit_button.click()

    def click_lets_start(self) -> None:
        self.lets_start_button.click()
