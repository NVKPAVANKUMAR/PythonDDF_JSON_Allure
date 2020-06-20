from selenium.webdriver.common.by import By


class LoginPage():
    textbox_username_id = "txtUsername"
    textbox_password_id = "txtPassword"
    button_login = (By.NAME, "Submit")
    errortxt_msg = (By.CSS_SELECTOR, "span#spanMessage")

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, usn):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(usn)

    def setPassword(self, pwd):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(pwd)

    def clickLoginButton(self):
        self.driver.find_element(*self.button_login).click()

    def verifyErrorMsg(self):
        return self.driver.find_element(*self.errortxt_msg).is_displayed()
