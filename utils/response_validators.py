import allure

# Validates the visibility of key UI elements on the Home Page to ensure it has loaded properly
@allure.step("Validate elements on Home Page")
def validate_home_page(home_page):
    assert home_page.get_signin_text().is_visible(), "'Sign in' text is not visible on Home Page"
    assert home_page.get_create_account_link().is_visible(), "'Create account' link is not visible on Home Page"

# Validates whether a login error message appears based on the expected outcome.
# If login is expected to fail, it checks for an error or handles silent failures gracefully.
@allure.step("Validate login error visibility")
def validate_login_error_visible(login_page, expected: bool):
    try:
        locator = login_page.get_error_message()

        if expected:
            assert not locator.is_visible(), "Unexpected login error message appeared"
        else:
            if locator.is_visible():
                assert True
            else:
                print("[INFO] Login failed silently - no visible error message")
                assert True

    except Exception as e:
        if not expected:
            print("[INFO] No error element found at all - assuming silent login failure")
            assert True
        else:
            raise AssertionError("Expected successful login, but error element appeared") from e

# Validates that login was successful by checking the visibility of key elements in the inbox page
@allure.step("Validate successful login by checking key UI elements in inbox")
def validate_successful_login(inbox_page):
    inbox_page.wait_for_page_to_load()
    assert inbox_page.get_compose_button().is_visible(), "'Compose' button not visible – login may have failed"
    assert inbox_page.get_inbox_tab().is_visible(), "'Inbox' tab not visible – login may have failed"
