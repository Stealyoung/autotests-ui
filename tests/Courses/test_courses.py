import pytest
import allure
from allure_commons.types import Severity

from pages.Courses.courses_list_page import CoursesListPage
from pages.Courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
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

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(
        self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage
    ):
        create_course_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"
        )
        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="", estimated_time="", description="", min_score="0", max_score="0"
        )
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image(
            file="./testdata/files/image.png"
        )
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10",
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks",
        )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(
        self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage
    ):
        create_course_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"
        )
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10",
        )
        create_course_page.image_upload_widget.upload_preview_image(
            file="./testdata/files/image.png"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks",
        )
        courses_list_page.course_view.menu.click_edit(0)
        create_course_page.create_course_form.fill(
            title="Automatization QA",
            estimated_time="3 months",
            description="Automatization QA",
            max_score="200",
            min_score="1",
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Automatization QA",
            estimated_time="3 months",
            max_score="200",
            min_score="1",
        )
