import pytest
from pages.login import Login

@pytest.mark.parametrize("username, password, expected_message", [
    ("standard_user", "secret_sauce", None),
    ("standard_user", "bad_password", "Epic sadface: Username and password do not match any user in this service"),
    ("user_not_registered", "secret_sauce", "Epic sadface: Username or password do not match any user in this service"),
])
def test_login(driver, username, password, expected_message):
    driver.get("https://www.saucedemo.com/")
    login = Login(driver)
    login.login(username, password)

    if expected_message:
        actual_message = login.get_error_message()
        assert actual_message == expected_message
    else:
        assert "inventory.html" in driver.current_url