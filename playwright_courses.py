from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создание контекста
    page = context.new_page()  # Создание страницы

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

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        storage_state="browser-state.json"
    )  # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )

    # Проверяем, что есть заголовок Courses
    courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    # Проверяем, что есть иконка пустого блока
    empty_block_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(empty_block_icon).to_be_visible()

    # Проверяем, что появился текст об отсутствии результатов
    no_results_block = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(no_results_block).to_be_visible()
    expect(no_results_block).to_have_text("There is no results")

    # Проверяем, что появился текстовый блок под заголовком
    text_description_block = page.get_by_test_id(
        "courses-list-empty-view-description-text"
    )
    expect(text_description_block).to_be_visible()
    expect(text_description_block).to_have_text(
        "Results from the load test pipeline will be displayed here"
    )
