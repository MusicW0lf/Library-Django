from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

VALID_USERNAME = "thehourofcode4@gmail.com"
VALID_PASSWORD = "qwerty"
INVALID_USERNAME = "aa@123com"
INVALID_PASSWORD = "aaaaa"

BASE_URL = "http://127.0.0.1:8000/authentication/"

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

def navigate_to_login():
    driver.get(BASE_URL)
    print("Navigated to the login page.")
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
    login_link.click()
    print("Clicked the 'Login' button.")

def login(email, password):
    email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_field = driver.find_element(By.NAME, "password")
    email_field.clear()
    password_field.clear()
    email_field.send_keys(email)
    password_field.send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    print(f"Attempted login with email: {email} and password: {password}")

def assert_error_message(expected_message):
    error_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-message")))
    assert expected_message in error_message.text
    print("Error message displayed as expected.")

def logout():
    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Logout']")))
    logout_button.click()
    print("Clicked the 'Logout' button.")

try:
    navigate_to_login()

    # Invalid Email Test
    login(INVALID_USERNAME, VALID_PASSWORD)
    assert_error_message("Invalid email or password")

    # Invalid Password Test
    login(VALID_USERNAME, INVALID_PASSWORD)
    assert_error_message("Invalid email or password")

    # Both Invalid Email and Password Test
    login(INVALID_USERNAME, INVALID_PASSWORD)
    assert_error_message("Invalid email or password")

    # Valid Credentials Test
    login(VALID_USERNAME, VALID_PASSWORD)
    user_status = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'You are logged in as:')]")))
    assert VALID_USERNAME in user_status.text
    print("Successfully logged in with valid credentials.")
    logout()

except TimeoutException as e:
    print(f"Test failed due to timeout: {e}")
except AssertionError as e:
    print(f"Test failed due to assertion error: {e}")
finally:
    driver.quit()
    print("Browser closed.")
