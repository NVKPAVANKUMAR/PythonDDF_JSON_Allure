from selenium.webdriver.common.by import By


class DashboardPage():
    link_welcome_id = "welcome"
    link_logout_xpath = "//a[.='Logout']"
    img_logo = (By.CSS_SELECTOR, "img[alt='OrangeHRM']")

    def __init__(self, driver):
        self.driver = driver

    def clickOnWelcome(self):
        self.driver.find_element_by_id(self.link_welcome_id).click()

    def clickOnLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()

    def verifyLogo(self):
        return self.driver.find_element(*self.img_logo).is_displayed()
