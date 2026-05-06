from playwright.sync_api import Page


from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.create_course_exercise_form_component import (
    CreateCourseExerciseFormComponent,
)
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import (
    CreateCourseToolbarViewComponent,
)
from components.courses.create_course_exercises_toolbar_view_component import (
    CreateCourseExercisesToolbarViewComponent,
)
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)

        # Замена локаторов на компонент
        self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)

        self.image_upload_widget = ImageUploadWidgetComponent(
            page, "create-course-preview"
        )
        self.exercises_empty_view = EmptyViewComponent(page, "create-course-exercises")

        # Замена локаторов на компонент
        self.create_course_form = CreateCourseFormComponent(page)

        # Замена локаторов на компонент
        self.create_course_exercises_toolbar_view = (
            CreateCourseExercisesToolbarViewComponent(page)
        )

        # Блок, который отображается, когда в курсе нет заданий
        self.create_exercises_form = CreateCourseExerciseFormComponent

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title="There is no exercises",
            description='Click on "Create exercise" button to create new exercise',
        )
