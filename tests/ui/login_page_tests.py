import pytest
from faker import Faker

from src.config import Config
from src.ui.application import Application

fake = Faker()

invalid_login_test_data = [
    pytest.param(Config.TESTOMAT_USERNAME, fake.password(length=10), id="valid_email_invalid_pass"),
    pytest.param(fake.email(), fake.password(length=10), id="invalid_email_invalid_pass"),
    pytest.param("", "", id="empty_email_pass"),
    pytest.param("plaintext", fake.password(length=10), id="invalid_email_format_no_at"),
    pytest.param(Config.TESTOMAT_USERNAME, "", id="valid_email_empty_pass"),
    pytest.param("", fake.password(length=10), id="empty_email_valid_pass"),
    pytest.param("a@b.c", fake.password(length=10), id="min_valid_email_format"),
    pytest.param(fake.email(), "a", id="valid_email_min_length_pass"),
]


def test_navigation_to_login_page(app: Application):
    home_page = app.home_page.open().is_loaded()
    home_page.click_login_button()

    app.login_page.open().is_loaded()


@pytest.mark.smoke
@pytest.mark.parametrize("email, password", invalid_login_test_data)
def test_login_page(shared_app: Application, email, password):
    login_page = shared_app.login_page.open().is_loaded()
    login_page.login(email, password)
    login_page.verify_invalid_login_message()


@pytest.mark.smoke
def test_login_with_valid_creds(app: Application):
    login_page = app.login_page.open().is_loaded()
    login_page.login(Config.TESTOMAT_USERNAME, Config.TESTOMAT_PASSWORD)

    app.project_page.is_loaded()
