import allure
import pytest
from tests.BaseTest import BaseTest
from utils.response_validators import validate_home_page

@allure.epic("Gmail UI")
@allure.feature("Home Page")
class TestHomePage(BaseTest):

    @allure.story("Homepage loaded successfully")
    @allure.description("Validate Gmail home page screen has 'Sign in' and 'Create account'")
    def test_home_page_loaded(self):
        validate_home_page(self.home_page)
