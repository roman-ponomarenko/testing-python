from typing import Self

from playwright.sync_api import Locator, Page, expect


class ProjectTestsPage:
    def __init__(self, page: Page):
        self._page = page

    def is_loaded(self) -> Self:
        expect(self.project_title_link).to_be_visible()
        return self

    @property
    def project_title_link(self) -> Locator:
        return self._page.locator(".breadcrumbs-page a.active")

    def verify_project_name(self, expected_name: str) -> None:
        expect(self.project_title_link).to_have_text(expected_name)
