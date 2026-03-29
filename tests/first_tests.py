import pytest
from playwright.sync_api import Page, expect

from src.config import Config
from src.constants import PageTitles


@pytest.fixture(scope="function")
def login(page: Page):
    page.goto(Config.TESTOMAT_SIGN_IN_URL)
    expect(page).to_have_title(PageTitles.SIGNIN_TITLE)
    login_user(page, Config.TESTOMAT_USERNAME, Config.TESTOMAT_PASSWORD)


def test_login_with_invalid_creds(page: Page, faker):
    page.goto(Config.TESTOMAT_URL)

    expect(page).to_have_title(PageTitles.HP_TITLE)

    click_sign_in_button(page)

    login_user(page, Config.TESTOMAT_USERNAME, faker.password(length=10))

    expect(
        page.locator("#content-desktop p:has-text('Invalid Email or password.')")
    ).to_be_visible()


def test_login_with_valid_creds(page: Page):
    page.goto(Config.TESTOMAT_URL)

    expect(page).to_have_title(PageTitles.HP_TITLE)

    click_sign_in_button(page)

    login_user(page, Config.TESTOMAT_USERNAME, Config.TESTOMAT_PASSWORD)

    expect(page.locator(".common-flash-success p")).to_have_text(
        "Signed in successfully"
    )


def test_search_project_in_company(page: Page, login):
    target_project = "Grocery, Outdoors & Shoes"

    search_for_project(page, target_project)

    expect(page.locator(f"#grid ul li > a[title='{target_project}']")).to_be_visible()


def test_should_be_possible_to_open_free_project(page: Page, login):
    project_name = "Free Projects"
    target_project = "Grocery, Outdoors & Shoes"

    page.locator("#company_id").select_option(project_name)

    expect(page.get_by_text("You have not created any projects yet")).to_be_visible()
    expect(
        page.locator("a.common-btn-primary:has-text('Create project')")
    ).to_be_visible()

    search_for_project(page, target_project)

    expect(page.get_by_text("You have not created any projects yet")).to_be_visible()
    expect(
        page.locator("a.common-btn-primary:has-text('Create project')")
    ).to_be_visible()


def click_sign_in_button(page: Page):
    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()
    page.locator("[href*='sign_in'].login-item").click()


def login_user(page: Page, email: str, password: str):
    page.locator("#content-desktop #user_email").fill(email)
    page.locator("#content-desktop #user_password").fill(password)
    page.get_by_role(role="button", name="Sign in").click()


def search_for_project(page: Page, target_project: str):
    expect(page.get_by_role(role="searchbox", name="Search")).to_be_visible()
    page.locator("#content-desktop #search").fill(target_project)
