from playwright.sync_api import Page  # Импортируем класс Page


class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page  # Присваиваем объект page атрибуту класса

    # Метод для перехода на страницу
    def visit(self, url: str):
        self.page.goto(url)
        # self.page.wait_for_timeout(10000)
        # Закомментирована строка, тк мешает выполнению теста на личной машине

    # Метод для перезагрузки страницы
    def reload(self):
        self.page.reload(wait_until="domcontentloaded")
