import re
import re
from playwright.sync_api import expect
from src.ui.application import Application
from faker import Faker

from src.config import Config
from src.ui.models.badge import Badge
from src.ui.models.checkbox_state import CheckboxState
from src.ui.models.project_type import ProjectType


def test_verify_project_details_and_navigation_to_empty_project_page(app: Application):
    project_name = 'E-commerce'

    login_page = app.login_page.open().is_loaded()
    login_page.login(Config.TESTOMAT_USERNAME, Config.TESTOMAT_PASSWORD)

    projects_page = app.project_page.is_loaded()

    projects_page.verify_selected_company('QA Club Lviv')
    projects_page.verify_plan_badge_text('Enterprise plan')

    projects_page.search_project(project_name)

    projects_page.verify_count_of_project_visible(1)

    project_card = projects_page.get_project_card_by_title(project_name)

    project_card.verify_badge(Badge.Classical)
    project_card.verify_test_count(0)

    project_card.click()

    empty_project_page = app.empty_project_page.is_loaded()
    empty_project_page.verify_project_title(project_name)

def test_project_type_selection_flow(app: Application):
    # Step 1: Login and navigate to Create Project page
    app.login_page.open().is_loaded()
    app.login_page.login(Config.TESTOMAT_USERNAME, Config.TESTOMAT_PASSWORD)

    app.project_page.is_loaded()
    app.project_page.click_create_project()

    new_project_page = app.new_project_page.is_loaded()

    # Step 2: Select Classical and verify
    new_project_page.select(ProjectType.CLASSICAL)
    new_project_page.classical_option.verify_is_selected()
    new_project_page.bdd_option.verify_is_not_selected()
    new_project_page.verify_demo_data_state(CheckboxState.UNCHECKED)
    new_project_page.verify_demo_form_not_visible()

    # Step 3: Select BDD and verify
    new_project_page.select(ProjectType.BDD)
    new_project_page.bdd_option.verify_is_selected()
    new_project_page.classical_option.verify_is_not_selected()
    new_project_page.verify_demo_data_state(CheckboxState.UNCHECKED)
    new_project_page.verify_demo_form_not_visible()

    # Step 4: Select Classical again and verify
    new_project_page.select(ProjectType.CLASSICAL)
    new_project_page.classical_option.verify_is_selected()
    new_project_page.bdd_option.verify_is_not_selected()
    new_project_page.verify_demo_data_state(CheckboxState.UNCHECKED)
    new_project_page.verify_demo_form_not_visible()

    # Step 5: Pick demo checkbox and verify demo form visibility
    new_project_page.verify_demo_data_state(CheckboxState.UNCHECKED)
    new_project_page.toggle_demo_data()
    new_project_page.verify_demo_data_state(CheckboxState.CHECKED)
    new_project_page.verify_demo_form_visible()

def test_create_new_classical_project(app: Application, faker: Faker):
    project_name = faker.word().capitalize() + " project"

    # Step 1: Login
    login_page = app.login_page.open().is_loaded()
    login_page.login(Config.TESTOMAT_USERNAME, Config.TESTOMAT_PASSWORD)

    # Step 2: Navigate to Create Project page
    projects_page = app.project_page.is_loaded()
    projects_page.click_create_project()

    # Step 3: Create a Classical Project
    new_project_page = app.new_project_page.is_loaded()
    new_project_page.select(ProjectType.CLASSICAL)
    new_project_page.fill_project_title(project_name)
    new_project_page.submit_create_project()

    # Step 4: Verify navigation to the Empty Project Page
    empty_project_page = app.empty_project_page.is_loaded()
    empty_project_page.readme_panel.is_loaded().close()

    empty_project_page.verify_project_title(project_name)

def test_create_new_bdd_project(app: Application, faker: Faker):
    project_name = faker.word().capitalize() + " BDD project"

    # Step 1: Login
    login_page = app.login_page.open().is_loaded()
    login_page.login(Config.TESTOMAT_USERNAME, Config.TESTOMAT_PASSWORD)

    # Step 2: Navigate to Create Project page
    projects_page = app.project_page.is_loaded()
    projects_page.click_create_project()

    # Step 3: Create a BDD Project
    new_project_page = app.new_project_page.is_loaded()
    new_project_page.select(ProjectType.BDD)
    new_project_page.fill_project_title(project_name)
    new_project_page.submit_create_project()

    # Step 4: Verify navigation to the Empty Project Page
    empty_project_page = app.empty_project_page.is_loaded()
    empty_project_page.readme_panel.is_loaded().close()

    empty_project_page.verify_project_title(project_name)
