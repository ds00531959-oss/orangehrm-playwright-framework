from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def type(self, locator: str, value: str):
        self.page.locator(locator).press("Control+A")
        self.page.locator(locator).fill(value)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).text_content()

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def wait_for_visible(self, locator: str, timeout: int = 10000):
        self.page.locator(locator).wait_for(
            state="visible",
            timeout=timeout
        )

    def screenshot(self, path: str):
        self.page.screenshot(
            path=path,
            full_page=True
        )