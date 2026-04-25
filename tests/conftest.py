
from collections.abc import Generator

import pytest
from faker import Faker
from playwright.sync_api import Browser, Page, sync_playwright, expect

from src.config import Config
from src.ui.application import Application

BROWSER_ARGS: dict = {
    "channel": Config.PW_BROWSER,
    "headless": Config.PW_HEADLESS,
    "slow_mo": Config.PW_SLOWMO,
    "timeout": Config.PW_TIMEOUT,
}

CONTEXT_ARGS: dict = {
    "base_url": Config.TESTOMAT_BASE_APP_URL,
    "viewport": {"width": 1366, "height": 768},
    "locale": "uk-UA",
    "timezone_id": "Europe/Kyiv",
    "record_video_dir": "videos/",
    "permissions": ["geolocation"],
}


@pytest.fixture(scope="session")
def faker() -> Faker:
    return Faker()


@pytest.fixture(scope="session")
def browser_instance() -> Generator[Browser]:
    print(f"Running tests in {'headless' if Config.PW_HEADLESS else 'headed'} mode")
    print(f"Slowing down by {Config.PW_SLOWMO}ms")

    expect.set_options(timeout=Config.PW_EXPECT_TIMEOUT)

    with sync_playwright() as p:
        browser = p.chromium.launch(**BROWSER_ARGS)
        yield browser
        browser.close()


@pytest.fixture(scope="module")
def shared_browser(browser_instance: Browser) -> Generator[Page]:
    context = browser_instance.new_context(**CONTEXT_ARGS)
    page = context.new_page()
    yield page
    page.close()
    context.close()


@pytest.fixture(scope="function")
def shared_app(shared_browser: Page) -> Generator[Application]:
    # Wait to avoid rate limiting by Testomat.io (configurable via PW_RATE_LIMIT_TIMEOUT)
    shared_browser.wait_for_timeout(Config.PW_RATE_LIMIT_TIMEOUT)
    yield Application(shared_browser)


@pytest.fixture(scope="function")
def app(browser_instance: Browser) -> Generator[Application]:
    context = browser_instance.new_context(**CONTEXT_ARGS)
    page = context.new_page()
    yield Application(page)
    page.close()
    context.close()


@pytest.fixture(scope="function")
def logged_app(browser_instance: Browser) -> Generator[Application]:
    context = browser_instance.new_context(**CONTEXT_ARGS)
    page = context.new_page()
    app = Application(page)
    login_page = app.login_page.open().is_loaded()
    login_page.login(Config.TESTOMAT_USERNAME, Config.TESTOMAT_PASSWORD)
    yield Application(page)
    page.close()
    context.close()
