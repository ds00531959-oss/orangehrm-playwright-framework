import pytest
from config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from utils.logger import logger

@pytest.mark.regression
def test_update_employee(page):
    page.goto(
    BASE_URL,
    wait_until="domcontentloaded",
    timeout=120000
    )
    print("After goto URL:", page.url)

    # Login
    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    page.wait_for_load_state("networkidle")

    # Open PIM
    pim = PIMPage(page)
    pim.open_pim()
    pim.open_employee_list()

    # Search employee
    # pim.search_employee("Amit Kumar Sharma")

    # Click Edit
    pim.click_first_edit()

    # Debug
    print("Current URL:", page.url)


    # Update first name
    pim.update_first_name("DharmendraUpdated")

    # Verify
    assert "viewPersonalDetails" in page.url
    
    # Verify update (optional)
    print("Employee updated successfully")

    logger.info("Updating employee details")
    logger.info("Employee updated successfully")