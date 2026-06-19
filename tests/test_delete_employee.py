import pytest
from config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

@pytest.mark.regression
def test_delete_employee(page):
    page.goto(
        BASE_URL,
        wait_until="load",
        timeout=120000
    )

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    # Login verify
    page.wait_for_url("**/dashboard/**", timeout=60000)

    pim = PIMPage(page)
    pim.open_pim()
    pim.open_employee_list()

    # Existing employee search
    # pim.search_employee("Amit Kumar Sharma")

    # Delete employee
    pim.delete_first_employee()