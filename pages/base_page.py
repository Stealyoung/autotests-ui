from re import Pattern

import allure
from playwright.sync_api import Page, expect  # Импортируем класс Page


class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page  # Присваиваем объект page атрибуту класса

    # Метод для перехода на страницу
    def visit(self, url: str):
        with allure.step(f"Opening the url '{url}'"):
            self.page.goto(url)
            # self.page.wait_for_timeout(10000)
            # Закомментирована строка, тк мешает выполнению теста на личной машине

    # Метод для перезагрузки страницы
    def reload(self):
        with allure.step(f"Reloading page with url '{self.page.url}'"):
            self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f"Checking current url matches with '{expected_url.pattern}'"):
            expect(self.page).to_have_url(expected_url)
