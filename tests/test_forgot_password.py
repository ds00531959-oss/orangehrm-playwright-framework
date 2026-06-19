import pytest
from config import BASE_URL

@pytest.mark.sanity
def test_forgot_password(page):
    page.goto(BASE_URL)

    page.get_by_text("Forgot your password?").click()

    page.locator("[name='username']").fill("Admin")

    page.get_by_role(
        "button",
        name="Reset Password"
    ).click(no_wait_after=True)

    page.wait_for_timeout(5000)

    print("Current URL:", page.url)