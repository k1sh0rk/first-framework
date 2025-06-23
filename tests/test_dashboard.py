import time

from pages import login_page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By
class Test:
    def test_dashboard(self,setup):
        test_dashboard= DashboardPage(setup)
        login_page.login()
        test_dashboard.admin()
        time.sleep(5)
