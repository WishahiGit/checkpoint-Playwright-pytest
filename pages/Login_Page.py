from pages.BasePage import BasePage
from playwright.sync_api import TimeoutError

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__EMAIL_INPUT = self.page.get_by_role("textbox", name="Email or phone")
        self.__EMAIL_NEXT_BTN = self.page.get_by_role("button", name="Next")
        self.__PASSWORD_NEXT_BTN = self.page.get_by_role("button", name="Next")

    def login(self, email, password):
        self.__EMAIL_INPUT.fill(email)
        self.__EMAIL_NEXT_BTN.click()

        try:
            self.page.wait_for_selector('input[type="password"]', timeout=5000)
            self.__PASSWORD_INPUT = self.page.locator('input[type="password"]')
            self.__PASSWORD_INPUT.fill(password)
            self.__PASSWORD_NEXT_BTN.click()
        except TimeoutError:

            pass


    def get_error_message(self):
        return self.page.locator('div[jsname="B34EJ"], div[jsname="uyM38b"]')


