import pytest
from playwright.sync_api import Page

from pages.Authentication.login_page import LoginPage  # Импортируем LoginPage
from pages.Dashboard.dashboard_page import DashboardPage
from pages.Authentication.registration_page import RegistrationPage


@pytest.mark.authorization
@pytest.mark.regression
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password",
        [
            {"user.name@gmail.com", "password"},
            {"user.name@gmail.com", "  "},
            {"  ", "password"},
        ],
    )
    def test_wrong_email_or_password_authorization(
        self, chromium_page: Page, email: str, password: str
    ):
        login_page = LoginPage(page=chromium_page)

        # Переходим на страницу входа
        login_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
        )

        # Заполняем поле email и password
        login_page.login_form.fill_login_form(email, password)

        # Нажимаем на кнопку Login
        login_page.click_login_button()

        # Проверяем, что появилось сообщение об ошибке
        login_page.check_visible_wrong_email_or_password_alert()

    def test_successful_authorization(
        self,
        login_page: LoginPage,
        dashboard_page: DashboardPage,
        registration_page: RegistrationPage,
    ):
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )
        registration_page.registration_form.fill(
            email="user.name@gmail.com", username="username", password="password"
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill_login_form(
            email="user.name@gmail.com", password="password"
        )
        login_page.click_login_button()

        # Проверка элементов Dashboard после входа
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()

    def test_navigate_from_authorization_to_registration(
        self, login_page: LoginPage, registration_page: RegistrationPage
    ):
        login_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
        )
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(
            email="", username="", password=""
        )
