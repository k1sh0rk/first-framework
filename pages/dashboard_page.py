from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.admin=(By.XPATH,'//*[@class="oxd-main-menu-item" and @href="/web/index.php/admin/viewAdminModule"]')
    def admin(self):
        self.driver.find_element(*self.admin).click()
