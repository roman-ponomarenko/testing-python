from playwright.sync_api import Page

from src.ui.pages.empty_project_page import EmptyProjectPage
from src.ui.pages.home_page import HomePage
from src.ui.pages.login_page import LoginPage
from src.ui.pages.new_project_page import NewProjectPage
from src.ui.pages.project_page import ProjectPage


class Application:
    def __init__(self, page: Page):
        self._page = page
        self._home_page = HomePage(page)
        self._login_page = LoginPage(page)
        self._project_page = ProjectPage(page)
        self._new_project_page = NewProjectPage(page)
        self._empty_project_page = EmptyProjectPage(page)

    @property
    def home_page(self) -> HomePage:
        return self._home_page

    @property
    def login_page(self) -> LoginPage:
        return self._login_page

    @property
    def project_page(self) -> ProjectPage:
        return self._project_page

    @property
    def new_project_page(self) -> NewProjectPage:
        return self._new_project_page

    @property
    def empty_project_page(self) -> EmptyProjectPage:
        return self._empty_project_page
