import pytest
from config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from utils.data_generator import generate_employee

@pytest.mark.regression
def test_add_employee(page):
    # Dynamic data
    employee = generate_employee()

    first_name = employee["first_name"]
    last_name = employee["last_name"]

    page.goto(
        BASE_URL,
        wait_until="domcontentloaded",
        timeout=90000
    )

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    pim = PIMPage(page)
    pim.open_pim()
    pim.click_add()

    pim.add_employee(first_name, last_name)

    print(f"Created Employee: {first_name} {last_name}")

    assert "viewPersonalDetails" in page.url