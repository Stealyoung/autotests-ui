from playwright.sync_api import Page

from pages.base_page import BasePage
from components.authentication.registration_form_component import (
    RegistrationFormComponent,
)


class RegistrationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # Замена локаторов на компонент
        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = page.get_by_test_id(
            "registration-page-registration-button"
        )
        self.login_link = page.get_by_test_id("registration-page-login-link")

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
