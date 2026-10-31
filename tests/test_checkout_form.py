import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


fake = Faker("ru_RU")
Faker.seed(1)

users = [
    (
        fake.first_name(),
        fake.last_name(),
        fake.postcode(),
    )
    for _ in range(10)
]

@pytest.mark.regression
@pytest.mark.parametrize(
    "first_name,last_name,postal_code",
    users,
)
def test_checkout_form(
    logged_in,
    first_name,
    last_name,
    postal_code,
):
    driver = logged_in
    wait = WebDriverWait(driver, 10)

    driver.get(
        "https://www.saucedemo.com/checkout-step-one.html"
    )

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "first-name")
        )
    ).send_keys(first_name)

    driver.find_element(
        By.ID,
        "last-name",
    ).send_keys(last_name)

    driver.find_element(
        By.ID,
        "postal-code",
    ).send_keys(postal_code)

    wait.until(
        EC.element_to_be_clickable((By.ID, "continue"))
    ).click()

    wait.until(EC.url_contains("checkout-step-two"))

    assert "checkout-step-two" in driver.current_url