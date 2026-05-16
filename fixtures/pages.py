import pytest
from playwright.sync_api import Page

from pages.Authentication.registration_page import RegistrationPage
from pages.Dashboard.dashboard_page import DashboardPage
from pages.Courses.courses_list_page import CoursesListPage
from pages.Courses.create_course_page import CreateCoursePage
from pages.Authentication.login_page import LoginPage


@pytest.fixture
def registration_page(browser_page: Page) -> RegistrationPage:
    return RegistrationPage(page=browser_page)


@pytest.fixture
def dashboard_page(browser_page: Page) -> DashboardPage:
    return DashboardPage(page=browser_page)


@pytest.fixture
def dashboard_page_with_state(browser_page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=browser_page_with_state)


@pytest.fixture
def courses_list_page(browser_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=browser_page_with_state)


@pytest.fixture
def create_course_page(browser_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=browser_page_with_state)


@pytest.fixture
def login_page(browser_page: Page) -> LoginPage:
    return LoginPage(page=browser_page)
