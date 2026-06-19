import pytest
from config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

@pytest.mark.sanity
@pytest.mark.regression
def test_search_employee(page):
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    # Dashboard load hone ka wait
    page.wait_for_load_state("networkidle")

    pim = PIMPage(page)
    pim.open_pim()
    pim.open_employee_list()

   # Verify Employee List page opened
    assert "viewEmployeeList" in page.url