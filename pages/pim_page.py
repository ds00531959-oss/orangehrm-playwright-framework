import time
from playwright.sync_api import Page
from utils.logger import logger


class PIMPage:
    def __init__(self, page: Page):
        self.page = page

    # =========================
    # Navigation
    # =========================

    def open_pim(self):
        logger.info("Opening PIM module")
        self.page.get_by_role("link", name="PIM").click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_employee_list(self):
        logger.info("Opening Employee List")
        self.page.get_by_role("link", name="Employee List").click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_add(self):
        logger.info("Opening Add Employee page")
        self.page.get_by_role("button", name="Add").click()
        self.page.wait_for_load_state("domcontentloaded")

    # =========================
    # Add Employee
    # =========================

    def add_employee(self, first_name, last_name):
        logger.info(f"Adding employee: {first_name} {last_name}")

        self.page.wait_for_load_state("domcontentloaded")

        self.page.locator("input[name='firstName']").fill(first_name)
        self.page.locator("input[name='middleName']").fill("")
        self.page.locator("input[name='lastName']").fill(last_name)

        employee_id = str(int(time.time()))[-6:]

        emp_id = self.page.locator(
            "//label[text()='Employee Id']/ancestor::div[contains(@class,'oxd-input-group')]//input"
        )

        emp_id.click()
        emp_id.press("Control+A")
        emp_id.fill(employee_id)

        logger.info(f"First Name: {first_name}")
        logger.info(f"Last Name: {last_name}")
        logger.info(f"Employee ID: {employee_id}")

        logger.info("Clicking Save button")
        self.page.get_by_role("button", name="Save").click()

        self.page.wait_for_url(
            "**/viewPersonalDetails/**",
            timeout=20000
        )

        logger.info("Employee added successfully")

        return employee_id

    # =========================
    # Search Employee
    # =========================

    def search_employee(self, employee_name):
        logger.info(f"Searching employee: {employee_name}")

        employee_input = self.page.locator(
            "input[placeholder='Type for hints...']"
        ).first

        employee_input.fill(employee_name)

        suggestion = self.page.locator(".oxd-autocomplete-option").first
        suggestion.wait_for(timeout=10000)
        suggestion.click()

        self.page.get_by_role("button", name="Search").click()

        self.page.locator(".oxd-table-body").wait_for(
            state="visible",
            timeout=10000
        )

        rows = self.page.locator(
            ".oxd-table-body .oxd-table-row"
        ).count()

        logger.info(f"Rows found: {rows}")

        if rows == 0:
            logger.error(
                f"Employee '{employee_name}' not found."
            )
            raise AssertionError(
                f"Employee '{employee_name}' not found."
            )

        logger.info("Employee search completed successfully")

    # =========================
    # Update Employee
    # =========================

    def click_first_edit(self):
        logger.info("Opening first employee for editing")

        edit_button = self.page.locator(
            "button:has(i.bi-pencil-fill)"
        ).first

        edit_button.wait_for(
            state="visible",
            timeout=10000
        )

        edit_button.click()
        self.page.wait_for_load_state("domcontentloaded")

        logger.info("Edit page opened successfully")

    def update_first_name(self, new_name):
        logger.info(
            f"Updating first name to: {new_name}"
        )

        first_name = self.page.locator(
            'input[name="firstName"]'
        )

        first_name.click()
        first_name.press("Control+A")
        first_name.fill(new_name)

        self.page.get_by_role(
            "button",
            name="Save"
        ).first.click()

        self.page.wait_for_load_state(
            "domcontentloaded"
        )

        logger.info(
            "Employee updated successfully"
        )

    # =========================
    # Delete Employee
    # =========================

    def delete_first_employee(self):
        logger.info("Deleting first employee")

        self.page.locator(
            "i.bi-trash"
        ).first.click(force=True)

        self.page.get_by_role(
            "button",
            name="Yes, Delete"
        ).click()

        self.page.wait_for_load_state(
            "domcontentloaded"
        )

        logger.info(
            "Employee deleted successfully"
        )
