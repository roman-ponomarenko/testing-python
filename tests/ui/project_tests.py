import pytest
from faker import Faker

from src.ui.application import Application
from src.ui.models.badge import Badge
from src.ui.models.checkbox_state import CheckboxState
from src.ui.models.project_type import ProjectType


@pytest.mark.regression
def test_verify_project_details_and_navigation_to_empty_project_page(logged_app: Application):
    project_name = "E-commerce"

    projects_page = logged_app.project_page.is_loaded()

    projects_page.verify_selected_company("QA Club Lviv")
    projects_page.verify_plan_badge_text("Enterprise plan")

    projects_page.search_project(project_name)

    projects_page.verify_count_of_project_visible(1)

    project_card = projects_page.get_project_card_by_title(project_name)

    project_card.verify_badge(Badge.Classical)
    project_card.verify_test_count(0)

    project_card.click()

    empty_project_page = logged_app.empty_project_page.is_loaded()
    empty_project_page.verify_project_title(project_name)


@pytest.mark.regression
def test_project_type_selection_flow(logged_app: Application):
    # Step 1: Navigate to Create Project page
    logged_app.project_page.is_loaded()
    logged_app.project_page.click_create_project()

    new_project_page = logged_app.new_project_page.is_loaded()

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


@pytest.mark.smoke
def test_create_new_classical_project(logged_app: Application, faker: Faker):
    project_name = faker.word().capitalize() + " project"

    # Step 1: Navigate to Create Project page
    projects_page = logged_app.project_page.is_loaded()
    projects_page.click_create_project()

    # Step 2: Create a Classical Project
    new_project_page = logged_app.new_project_page.is_loaded()
    new_project_page.select(ProjectType.CLASSICAL)
    new_project_page.fill_project_title(project_name)
    new_project_page.submit_create_project()

    # Step 3: Verify navigation to the Empty Project Page
    empty_project_page = logged_app.empty_project_page.is_loaded()
    empty_project_page.close_readme()

    empty_project_page.verify_project_title(project_name)


@pytest.mark.smoke
def test_create_demo_project_with_fill_demo_data(logged_app: Application):
    demo_project_name = "CodeceptJS Demo Project"

    # Step 1: Navigate to Create Project page
    projects_page = logged_app.project_page.is_loaded()
    projects_page.click_create_project()

    new_project_page = logged_app.new_project_page.is_loaded()

    # Step 2: Verify fill demo data is unchecked by default, then toggle it
    new_project_page.verify_demo_data_state(CheckboxState.UNCHECKED)
    new_project_page.toggle_demo_data()
    new_project_page.verify_demo_data_state(CheckboxState.CHECKED)
    new_project_page.verify_demo_form_visible()

    # Step 3: Select a demo project option and verify it is selected
    demo_option = new_project_page.get_demo_option_by_name(demo_project_name)
    demo_option.verify_is_not_selected()
    demo_option.select()
    demo_option.verify_is_selected()

    # Step 4: Create the demo project
    new_project_page.submit_create_demo_project()

    # Step 5: Verify navigation to the project tests page with correct project name
    project_tests_page = logged_app.project_tests_page.is_loaded()
    project_tests_page.verify_project_name(demo_project_name)


@pytest.mark.smoke
def test_create_new_bdd_project(logged_app: Application, faker: Faker):
    project_name = faker.word().capitalize() + " BDD project"

    # Step 1: Navigate to Create Project page
    projects_page = logged_app.project_page.is_loaded()
    projects_page.click_create_project()

    # Step 2: Create a BDD Project
    new_project_page = logged_app.new_project_page.is_loaded()
    new_project_page.select(ProjectType.BDD)
    new_project_page.fill_project_title(project_name)
    new_project_page.submit_create_project()

    # Step 3: Verify navigation to the Empty Project Page
    empty_project_page = logged_app.empty_project_page.is_loaded()
    empty_project_page.close_readme()

    empty_project_page.verify_project_title(project_name)
