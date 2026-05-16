import allure
from playwright.sync_api import Page, Playwright
from config import settings, Browser


def initialize_playwright_page(
    playwright: Playwright, test_name: str, browser_type:Browser,  storage_state: str | None = None
) -> Page:
    browser = playwright[browser_type].launch(
        headless=settings.headless
    )  # Запускаем браузер
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state,
        record_video_dir=settings.videos_dir,
    )  # Создаем контекст вместе с сохраненным состоянием бразуера
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page  # Открываем новую страницу и передаем ее в тест
    context.tracing.stop(path=settings.tracing_dir.joinpath(f"{test_name}.zip"))

    browser.close()  # После выполнения теста закрываем браузер

    allure.attach.file(
        source=settings.tracing_dir.joinpath(f"{test_name}.zip"),
        name="trace",
        extension="zip",
    )
    allure.attach.file(
        page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM
    )
