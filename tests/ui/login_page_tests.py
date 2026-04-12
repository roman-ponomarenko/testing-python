from faker import Faker
from src.ui.application import Application

from src.config import Config


def test_login_page(app: Application, faker: Faker):
    home_page = app.home_page.open().is_loaded()
    home_page.click_login_button()

    login_page = app.login_page.open().is_loaded()
    login_page.login(Config.TESTOMAT_USERNAME, faker.password(length=10))
    login_page.invalid_login_message_should_be_visible()

def test_login_with_valid_creds(app: Application):
    login_page = app.login_page.open().is_loaded()
    login_page.login(Config.TESTOMAT_USERNAME, Config.TESTOMAT_PASSWORD)

    app.project_page.is_loaded()