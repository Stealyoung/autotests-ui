import pytest
from playwright.sync_api import Page

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)

@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)
