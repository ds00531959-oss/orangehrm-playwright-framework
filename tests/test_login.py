import pytest
from config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.smoke
@pytest.mark.regression
def test_login(page):
    page.goto(BASE_URL)

    login = LoginPage(page)
    login.login(USERNAME, PASSWORD)

    dashboard = DashboardPage(page)

    # Dashboard verify
    dashboard.verify_dashboard()


    # Screenshot
    page.screenshot(
        path="screenshots/after_login.png",
        full_page=True
    )

    # Logout
    dashboard.logout()