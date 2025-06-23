import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By
class Test:
    def test_login(self,setup):
        login_page = LoginPage(setup)
        login_page.login("Admin", "admin123")
        time.sleep(3)
