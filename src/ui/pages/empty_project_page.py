from typing import Self

from playwright.sync_api import expect, Page, Locator

from src.ui.components.readme_panel import ReadmePanel


class EmptyProjectPage:

    def __init__(self, page: Page):
        self._page = page

    def is_loaded(self) -> Self:
        expect(self.project_title).to_be_visible()
        expect(self.onboarding_heading).to_be_visible()
        return self

    @property
    def project_title(self) -> Locator:
        return self._page.locator(".sticky-header h2")

    @property
    def readme_button(self) -> Locator:
        return self._page.locator(".sticky-header a.ember-view")

    @property
    def more_options_button(self) -> Locator:
        return self._page.locator(
            ".ember-basic-dropdown-trigger.btn-only-icon"
        )

    @property
    def onboarding_heading(self) -> Locator:
        return self._page.locator(".my-2.p-8.text-center h2", has_text="🪄 Let's do some testing!")

    # -------------------------
    # README Panel
    # -------------------------

    @property
    def readme_panel(self) -> ReadmePanel:
        return ReadmePanel(
            self._page.locator(".detail.detail-view-resizable")
        )

    def open_readme(self) -> ReadmePanel:
        self.readme_button.click()
        return self.readme_panel.is_loaded()

    def is_readme_panel_open(self) -> bool:
        return self.readme_panel.is_visible()

    # -------------------------
    # Verifications
    # -------------------------

    def verify_project_title(self, expected_title: str) -> None:
        expect(self.project_title).to_have_text(expected_title)
