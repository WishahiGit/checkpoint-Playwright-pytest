from playwright.sync_api import Page

class BasePage:


    def __init__(self, page: Page):
        self.page = page

    # Click on an element
    def click(self, locator) -> None:
        self.page.locator(locator).click()

    # Fill text into an input field
    def fill_text(self, locator, txt: str) -> None:
        self.page.locator(locator).fill(txt)

    # Get the visible inner text of an element
    def get_text(self, locator) -> str:
        return self.page.locator(locator).inner_text()

    # Select a value from a dropdown menu
    def select(self, locator, value: str) -> None:
        self.page.locator(locator).select_option(value=value)

    # Get a specific attribute value of an element
    def get_attribute(self, locator, attribute: str) -> str:
        return self.page.locator(locator).get_attribute(attribute)

    # Check if an element is visible on the page
    def is_visible(self, locator) -> bool:
        return self.page.locator(locator).is_visible()

    # Check if an element is enabled (not disabled)
    def is_enabled(self, locator) -> bool:
        return self.page.locator(locator).is_enabled()

    # Check if a checkbox or radio button is checked
    def is_checked(self, locator) -> bool:
        return self.page.locator(locator).is_checked()

    # Press a keyboard key on a specific element
    def press_key(self, locator, key: str) -> None:
        self.page.locator(locator).press(key)

    # Hover the mouse over an element (simulate user mouse hover)
    def hover(self, locator) -> None:
        self.page.locator(locator).hover()

    # Get the current value of an input field
    def input_value(self, locator) -> str:
        return self.page.locator(locator).input_value()

    # Wait until an element becomes visible
    def wait_for_visibility(self, locator, timeout=5000) -> None:
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)

    # Wait until an element becomes hidden
    def wait_for_hidden(self, locator, timeout=5000) -> None:
        self.page.locator(locator).wait_for(state="hidden", timeout=timeout)

    # Get the current page URL
    def get_current_url(self) -> str:
        return self.page.url

    # Get a Frame object by locating an iframe element
    def get_frame_by_locator(self, iframe_locator):
        return self.page.frame_locator(iframe_locator).frame()
