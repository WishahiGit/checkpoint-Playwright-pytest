import pytest
import allure
from tests.BaseTest import BaseTest
from utils.load_data import load_test_data
from utils.input import parse_bool, extract_login_credentials
from utils.response_validators import  validate_successful_login, validate_login_error_visible




@pytest.mark.ui
@allure.epic("Gmail UI")
@allure.feature("Login Scenarios")
class TestLoginUI(BaseTest):

    @allure.story("Positive and Negative Login Scenarios")
    @allure.description("Login with valid and invalid email/password combinations from Excel and validate expected outcome")
    @pytest.mark.parametrize(*load_test_data(sheet_name="ui", action="login", parametrize=True, excel_file="test_data/test_cases_login.xlsx"))
    def test_login(self, data: dict):
        email, password, expected = extract_login_credentials(data)
        self.login_page.login(email, password)
        if expected:
            validate_successful_login(self.inbox_page)

        else:
            validate_login_error_visible(self.login_page, expected=False)




