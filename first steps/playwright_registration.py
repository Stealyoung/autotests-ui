from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )

    # Заполняем поле email
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input = page.get_by_test_id("registration-form-username-input").locator(
        "input"
    )
    username_input.fill("username")

    # Заполняем поле password
    password_input = page.get_by_test_id("registration-form-password-input").locator(
        "input"
    )
    password_input.fill("password")

    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    # Проверяем, что есть заголовок Dashboard
    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_be_visible()
