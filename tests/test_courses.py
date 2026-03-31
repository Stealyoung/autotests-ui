import pytest
from playwright.sync_api import Page, expect

from pages.courses_list_page import CoursesListPage, CheckVisibleCourseCardParams
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):

    # Переходим на страницу курсов
    courses_list_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )

    # Проверяем, что есть Navbar
    courses_list_page.navbar.check_visible("username")

    # Проверяем, что есть Sidebar
    courses_list_page.sidebar.check_visible()

    # Проверяем, что есть заголовок и кнопка
    courses_list_page.toolbar_view.check_visible()

    # Проверяем, что есть иконка пустого блока с текстом
    # об отсутствии результатов
    courses_list_page.check_visible_empty_view()


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
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    create_course_page.check_visible_create_course_form(
        title="", estimated_time="", description="", min_score="0", max_score="0"
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.image_upload_widget.upload_preview_image(
        file="./testdata/files/image.png"
    )
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10",
    )
    create_course_page.click_create_course_button()
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks",
    )
