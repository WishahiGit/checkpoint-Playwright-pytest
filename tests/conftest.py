# conftest.py

import pytest
import allure
import os
from playwright.sync_api import sync_playwright

from pages.Home_Page import HomePage
from pages.Inbox_Page import InboxPage
from pages.Login_Page import LoginPage

# Set custom browser installation path to avoid default Playwright location
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"

# Global constants
URL = "https://gmail.com/"
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# -----------------------------
#  Fixture: Browser Setup
# -----------------------------
# This fixture runs automatically before each test.
# It launches a Chromium browser, opens Gmail, and initializes all page objects (Home, Login, Inbox).
# The browser context and page are injected into the test class instance for reuse.
@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    print(f"[DEBUG] setup_browser called for {request.node.cls}")

    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=800)
    context = browser.new_context()
    page = context.new_page()
    page.goto(URL)

    # Initialize Page Object Model instances
    home_page = HomePage(page)
    login_page = LoginPage(page)
    inbox_page = InboxPage(page)

    # Inject instances into the test class
    request.cls.playwright = playwright
    request.cls.browser = browser
    request.cls.context = context
    request.cls.page = page
    request.cls.login_page = login_page
    request.cls.home_page = home_page
    request.cls.inbox_page = inbox_page

    yield  # Run the test

    # Clean up after the test
    context.close()
    browser.close()
    playwright.stop()

# ---------------------------------------
#  Hook: Capture Screenshot on Failure
# ---------------------------------------
# This pytest hook captures a full-page screenshot when a test fails.
# It also attaches the current URL and screenshot to the Allure report for easier debugging.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        test_instance = getattr(item, "instance", None)
        page = getattr(test_instance, "page", None)

        if page:
            screenshot_path = os.path.join(SCREENSHOT_DIR, f"{item.name}.png")
            try:
                page.screenshot(path=screenshot_path, full_page=True)
                allure.attach.file(
                    screenshot_path,
                    name="Screenshot on Failure",
                    attachment_type=allure.attachment_type.PNG
                )
                allure.attach(
                    page.url,
                    name="Current URL",
                    attachment_type=allure.attachment_type.TEXT
                )
            except Exception as e:
                print(f"[⚠️ Screenshot failed] {e}")
