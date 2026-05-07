from playwright.sync_api import Page

from pages.base_page import BasePage
from components.authentication.registration_form_component import (
    RegistrationFormComponent,
)
from elements.button import Button
from elements.link import Link


class RegistrationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # Замена локаторов на компонент
        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(
            page, "registration-page-registration-button", "Registration"
        )
        self.login_link = Link(page, "registration-page-login-link", "Login")

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
