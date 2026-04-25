from typing import Self

from playwright.sync_api import Locator, Page, expect

from src.ui.components.project_card import ProjectCard


class ProjectPage:
    def __init__(self, page: Page):
        self._page = page
        self._project_grid: Locator = self._page.locator(".tab-content#grid ul")

    def is_loaded(self) -> Self:
        expect(self.success_flash_message).to_be_visible()
        return self

    # -------------------------
    # Flash / Notifications
    # -------------------------

    @property
    def success_flash(self) -> Locator:
        return self._page.locator(".common-flash-success")

    @property
    def success_flash_message(self) -> Locator:
        return self.success_flash.locator(selector_or_locator="p", has_text="Signed in successfully")

    # -------------------------
    # Header Elements
    # -------------------------

    @property
    def page_title(self) -> Locator:
        return self._page.locator(".common-page-header h2")

    @property
    def company_selector(self) -> Locator:
        return self._page.locator("#company_id")

    @property
    def plan_badge(self) -> Locator:
        return self._page.locator(".tooltip-project-plan")

    @property
    def search_input(self) -> Locator:
        return self._page.locator("#search")

    @property
    def create_button(self) -> Locator:
        return self._page.locator("a.common-btn-primary[href='/projects/new']")

    @property
    def grid_view_btn(self) -> Locator:
        return self._page.locator("#grid-view")

    @property
    def table_view_btn(self) -> Locator:
        return self._page.locator("#table-view")

    # -------------------------
    # Project Grid
    # -------------------------

    @property
    def _project_card_elements(self) -> Locator:
        return self._project_grid.locator("li")

    @property
    def project_cards(self) -> list[ProjectCard]:
        return [ProjectCard(card) for card in self._project_card_elements.all()]

    def get_project_card_by_title(self, title: str) -> ProjectCard:
        card = self._project_card_elements.filter(has=self._page.locator("h3", has_text=title)).first
        return ProjectCard(card)

    # -------------------------
    # Actions
    # -------------------------

    def select_company(self, company_id: str) -> None:
        self.company_selector.select_option(value=company_id)

    def search_project(self, query: str) -> None:
        self.search_input.fill(query)

    def switch_to_grid_view(self) -> None:
        self.grid_view_btn.click()

    def switch_to_table_view(self) -> None:
        self.table_view_btn.click()

    def click_create_project(self) -> None:
        self.create_button.click()

    # -------------------------
    # Assertions (helper)
    # -------------------------

    def verify_selected_company(self, expected_value: str):
        expect(self.company_selector.locator("option[selected]")).to_have_text(expected_value)

    def verify_plan_badge_text(self, expected_text: str):
        expect(self.plan_badge).to_have_text(expected_text)

    def verify_count_of_project_visible(self, expected_count: int) -> None:
        expect(self._project_card_elements.filter(visible=True)).to_have_count(expected_count)

    def get_all_project_titles(self) -> list[str]:
        return [card.get_title_text() for card in self.project_cards]
