import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
def test_login_valid(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(
        By.ID,
        "password",
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID,
        "login-button",
    ).click()

    wait.until(EC.url_contains("inventory.html"))

    title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    ).text

    assert title == "Products"