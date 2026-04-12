from typing import Self

from playwright.sync_api import Locator, Page, expect

from src.ui.components.demo_project_option import DemoProjectOption
from src.ui.components.project_type_option import ProjectTypeOption
from src.ui.models.checkbox_state import CheckboxState
from src.ui.models.project_type import ProjectType


class NewProjectPage:
    def __init__(self, page: Page):
        self._page = page

    def is_loaded(self) -> Self:
        expect(self.page_title).to_be_visible()
        expect(self.project_title_input).to_be_visible()
        return self

    # -------------------------
    # Header Elements
    # -------------------------

    @property
    def page_title(self) -> Locator:
        return self._page.locator(".common-page-header h2", has_text="New Project")

    @property
    def how_to_start_btn(self) -> Locator:
        return self._page.locator("a.common-btn-secondary[href*='getting-started']")

    # -------------------------
    # Project Type Selection
    # -------------------------

    @property
    def classical_option(self) -> ProjectTypeOption:
        return ProjectTypeOption(root=self._page.locator(ProjectType.CLASSICAL.locator))

    @property
    def bdd_option(self) -> ProjectTypeOption:
        return ProjectTypeOption(root=self._page.locator(ProjectType.BDD.locator))

    # -------------------------
    # New Project Form
    # -------------------------

    @property
    def project_title_input(self) -> Locator:
        return self._page.locator("#project_title")

    @property
    def fill_demo_data_checkbox(self) -> Locator:
        return self._page.locator("#demo-btn")

    @property
    def create_btn(self) -> Locator:
        return self._page.locator("#project-create-btn input[type='submit']")

    # -------------------------
    # Demo Section
    # -------------------------

    @property
    def demo_form_container(self) -> Locator:
        return self._page.locator("#demo-form")

    @property
    def create_demo_button(self) -> Locator:
        return self._page.locator("form[action='/projects/create_demo'] input[type='submit']")

    @property
    def _demo_option_elements(self) -> Locator:
        return self._page.locator("#demo-form .demo-list button")

    @property
    def demo_project_options(self) -> list[DemoProjectOption]:
        count = self._demo_option_elements.count()
        return [DemoProjectOption(self._demo_option_elements.nth(i)) for i in range(count)]

    def get_demo_option_by_name(self, name: str) -> DemoProjectOption:
        option_root = self._demo_option_elements.filter(has_text=name).first
        return DemoProjectOption(option_root)

    def is_demo_form_visible(self) -> bool:
        return "h-full" in (self.demo_form_container.get_attribute("class") or "")

    # -------------------------
    # Actions
    # -------------------------

    def select(self, project_type: ProjectType) -> None:
        ProjectTypeOption(root=self._page.locator(project_type.locator)).select()

    def fill_project_title(self, title: str) -> None:
        self.project_title_input.fill(title)

    def toggle_demo_data(self) -> None:
        self.fill_demo_data_checkbox.click()

    def submit_create_project(self) -> None:
        self.create_btn.click()

    def submit_create_demo_project(self) -> None:
        self.create_demo_button.click()

    # -------------------------
    # Verifications
    # -------------------------

    def verify_demo_data_state(self, state: CheckboxState) -> None:
        if state == CheckboxState.CHECKED:
            expect(self.fill_demo_data_checkbox).to_be_checked()
        else:
            expect(self.fill_demo_data_checkbox).not_to_be_checked()

    def verify_demo_form_visible(self) -> None:
        expect(self.demo_form_container).to_be_visible()

    def verify_demo_form_not_visible(self) -> None:
        expect(self.demo_form_container).not_to_be_visible()
