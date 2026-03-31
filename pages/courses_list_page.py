from playwright.sync_api import Page, expect
from dataclasses import dataclass

from components.courses.courses_list_toolbar_view_component import (
    CoursesListToolbarViewComponent,
)
from components.courses.course_view_component import CourseViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from pages.base_page import BasePage


@dataclass
class CheckVisibleCourseCardParams:
    index: int
    title: str
    max_score: str
    min_score: str
    estimated_time: str


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)

        # Замена локаторов на компонент
        self.toolbar_view = CoursesListToolbarViewComponent(page)

        # Замена локаторов на компонент
        self.course_view = CourseViewComponent(page)

        self.course_menu_button = page.get_by_test_id("course-view-menu-button")
        self.course_edit_menu_item = page.get_by_test_id("course-view-edit-menu-item")
        self.course_delete_menu_item = page.get_by_test_id(
            "course-view-delete-menu-item"
        )

        # Замена локаторов на компонент
        self.empty_view = EmptyViewComponent(page, "courses-list")

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title="There is no results",
            description="Results from the load test pipeline will be displayed here",
        )
