import pytest
from playwright.sync_api import expect
from config import BASE_URL
from pages.login_page import LoginPage


@pytest.mark.sanity
@pytest.mark.regression
def test_invalid_login(page):
    page.goto(BASE_URL)

    login = LoginPage(page)
    login.login("Admin", "wrongpassword")

    # Verify error message
    expect(
        page.locator(".oxd-alert-content-text")
    ).to_have_text("Invalid credentials")