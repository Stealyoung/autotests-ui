import pytest
from playwright.sync_api import Page, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):  # Создаем тестовую функцию

    # Переходим на страницу курсов
    chromium_page_with_state.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )

    # Проверяем, что есть заголовок Courses
    courses_title = chromium_page_with_state.get_by_test_id(
        "courses-list-toolbar-title-text"
    )
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    # Проверяем, что есть иконка пустого блока
    empty_block_icon = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-icon"
    )
    expect(empty_block_icon).to_be_visible()

    # Проверяем, что появился текст об отсутствии результатов
    no_results_block = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-title-text"
    )
    expect(no_results_block).to_be_visible()
    expect(no_results_block).to_have_text("There is no results")

    # Проверяем, что появился текстовый блок под заголовком
    text_description_block = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-description-text"
    )
    expect(text_description_block).to_be_visible()
    expect(text_description_block).to_have_text(
        "Results from the load test pipeline will be displayed here"
    )
