import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage  # Импортируем LoginPage


@pytest.mark.authorization
@pytest.mark.regression
@pytest.mark.parametrize(
    "email, password",
    [
        {"user.name@gmail.com", "password"},
        {"user.name@gmail.com", "  "},
        {"  ", "password"},
    ],
)
def test_wrong_email_or_password_authorization(
    chromium_page: Page, email: str, password: str
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