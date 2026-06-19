from playwright.sync_api import Page
from utils.base_page import BasePage
from utils.logger import logger


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def login(self, username, password):
        logger.info("Login process started")

        self.fill("[name='username']", username)
        self.fill("[name='password']", password)

        self.click("button[type='submit']")

        # Dashboard load hone ka wait
        self.page.wait_for_load_state("domcontentloaded")

        logger.info("Login process completed successfully")