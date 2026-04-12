import pytest
from faker import Faker
from playwright.sync_api import Page
from src.ui.application import Application


@pytest.fixture(scope="session")
def faker() -> Faker:
    return Faker()

@pytest.fixture(scope="function")
def app(page: Page) -> Application:
    return Application(page)
