import pytest
import allure
from allure_commons.types import Severity
from playwright.sync_api import Page

from config import settings
from pages.Authentication.login_page import LoginPage  # Импортируем LoginPage
from pages.Dashboard.dashboard_page import DashboardPage
from pages.Authentication.registration_page import RegistrationPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.routes import AppRoute


@pytest.mark.authorization
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password",
        [
            {"user.name@gmail.com", "password"},
            {"user.name@gmail.com", "  "},
            {"  ", "password"},
        ],
    )
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(
        self, browser_page: Page, email: str, password: str
    ):
        allure.dynamic.title(f"User login with wrong email or password: {email}")
        login_page = LoginPage(page=browser_page)

        # Переходим на страницу входа
        login_page.visit(AppRoute.LOGIN)

        # Заполняем поле email и password
        login_page.login_form.fill_login_form(email, password)

        # Нажимаем на кнопку Login
        login_page.click_login_button()

        # Проверяем, что появилось сообщение об ошибке
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with correct email and password")
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
        self,
        login_page: LoginPage,
        dashboard_page: DashboardPage,
        registration_page: RegistrationPage,
    ):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill_registration_form(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password,
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill_login_form(
            email=settings.test_user.email, password=settings.test_user.password
        )
        login_page.click_login_button()

        # Проверка элементов Dashboard после входа
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()

    @allure.tag(AllureTag.NAVIGATION)
    @allure.title("Navigation from login page to registration page")
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(
        self, login_page: LoginPage, registration_page: RegistrationPage
    ):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(
            email="", username="", password=""
        )
