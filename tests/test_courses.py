import pytest
from playwright.sync_api import Page, expect

from pages.courses_list_page import CoursesListPage, CheckVisibleCourseCardParams
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(
        create_course_page: CreateCoursePage, courses_list_page: CoursesListPage
):
    create_course_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"
    )
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_create_course_form(
        title="", estimated_time="", description="", min_score="0", max_score="0"
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image(file="./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10",
    )
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        CheckVisibleCourseCardParams(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks",
        )
    )

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
