import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )

        context = browser.new_context(
            viewport={"width": 1920, "height": 1080}
        )

        page = context.new_page()

        page.set_default_timeout(60000)
        page.set_default_navigation_timeout(60000)

        yield page

        # Screenshot only on failure
        if (
            hasattr(request.node, "rep_call")
            and request.node.rep_call.failed
        ):
            os.makedirs("screenshots", exist_ok=True)

            page.screenshot(
                path=f"screenshots/{request.node.name}.png",
                full_page=True
            )

        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)