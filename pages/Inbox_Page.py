# pages/InboxPage.py

from pages.BasePage import BasePage
import time
from playwright.sync_api import expect

class InboxPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__COMPOSE_BUTTON = page.get_by_role("button", name="Compose")
        self.__INBOX_TAB = page.get_by_role("link", name="Inbox")

    def get_compose_button(self):
        return self.__COMPOSE_BUTTON

    def get_inbox_tab(self):
        return self.__INBOX_TAB

    def wait_for_page_to_load(self):
        time.sleep(3)
        expect(self.__COMPOSE_BUTTON).to_be_visible(timeout=10000)
        expect(self.__INBOX_TAB).to_be_visible(timeout=10000)

