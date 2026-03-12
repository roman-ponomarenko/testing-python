from playwright.sync_api import Page, expect

from config import Config


def test_login_with_invalid_creds(page: Page):
    page.goto(Config.TESTOMAT_URL)
    expect(page).to_have_title("AI Test Management Tool | Testomat.io")
    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()
    page.locator("[href*='sign_in'].login-item").click()
    page.locator("#content-desktop #user_email").fill(Config.TESTOMAT_USERNAME)
    page.locator("#content-desktop #user_password").fill("1111")
    page.get_by_role("button", name="Sign in").click()
    expect(page.locator("#content-desktop .common-flash-info")).to_have_text("Invalid Email or password.")

def test_login_with_valid_creds(page: Page):
    page.goto(Config.TESTOMAT_URL)
    expect(page).to_have_title("AI Test Management Tool | Testomat.io")
    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()
    page.locator("[href*='sign_in'].login-item").click()
    page.locator("#content-desktop #user_email").fill(Config.TESTOMAT_USERNAME)
    page.locator("#content-desktop #user_password").fill(Config.TESTOMAT_PASSWORD)
    page.get_by_role("button", name="Sign in").click()
    expect(page.locator(".common-flash-success p")).to_have_text("Signed in successfully")