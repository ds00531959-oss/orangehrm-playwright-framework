from playwright.sync_api import Page, expect

class DashboardPage:

    def __init__(self, page: Page):
        self.page = page

    def verify_dashboard(self):
        expect(self.page).to_have_url(
    "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        )

    def logout(self):
        self.page.locator(".oxd-userdropdown-tab").click()
        self.page.get_by_text("Logout").click()