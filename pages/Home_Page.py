from pages.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__SIGNIN_TEXT = page.get_by_role("heading", name="Sign in")
        self.__CREATE_ACCOUNT_LINK = page.get_by_text("Create account")
        self.__EMAIL_INPUT = page.get_by_role("textbox", name="Email or phone")

    def get_signin_text(self):
        return self.__SIGNIN_TEXT

    def get_create_account_link(self):
        return self.__CREATE_ACCOUNT_LINK

    def get_email_input(self):
        return self.__EMAIL_INPUT



