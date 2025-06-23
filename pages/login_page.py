import time

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        time.sleep(5)
        self.name = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_b = (By.XPATH, '//*[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')

    def login(self, username, password):
        self.driver.find_element(*self.name).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_b).click()
