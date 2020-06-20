import logging
import sys
import unittest

import HtmlTestRunner
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

sys.path.append("C:/Users/npavankumar/PycharmProjects/SeleniumPythonPOM")
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from utility.configParser_util import parse_data
from utility.jsonParser_util import parse_json, json_length,write_json

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# creds = lambda: (
#     (parse_json("data", 0, 'username'), parse_json("data", 0, 'password')),
#     (parse_json("data", 1, 'username'), parse_json("data", 1, 'password')),
#     (parse_json("data", 2, 'username'), parse_json("data", 2, 'password')),
#     (parse_json("data", 3, 'username'), parse_json("data", 3, 'password'))
# )


@allure.severity(allure.severity_level.NORMAL)
class LoginTest(unittest.TestCase):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def setUpClass(cls):
        cls.driver.get(parse_data('section_a', 'url_val'))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @allure.severity(allure.severity_level.BLOCKER)
    # @data_provider(creds)
    def test_Login(self):
        lp = LoginPage(driver=self.driver)
        for i in range(json_length("data")):
            #  lp.setUserName(parse_data('section_a', 'username_val'))

            lp.setUserName(parse_json("data", i, 'username'))
            # lp.setPassword(parse_data('section_a', 'password_val'))
            lp.setPassword(parse_json("data", i, 'password'))
            lp.clickLoginButton()
            dp = DashboardPage(driver=self.driver)
            try:
                if lp.verifyErrorMsg():
                    allure.attach(self.driver.get_screenshot_as_png(),
                                  name="FailScreenshot",
                                  attachment_type=AttachmentType.PNG)
                    logger.info("Login with ", parse_json("data", i, 'username'), "&",
                                parse_json("data", i, 'password'), "FAILED")
                    write_json("data", i, "status", "FAILED")
            except NoSuchElementException:
                write_json("data", i, "status", "PASSED")
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="PassScreenshot",
                              attachment_type=AttachmentType.PNG)
                logger.info("Login with ", parse_json("data", i, 'username'), "&", parse_json("data", i, 'password'),
                            "PASSED")
                dp.clickOnWelcome()
                dp.clickOnLogout()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    with open("C:/Users/npavankumar/PycharmProjects/SeleniumPythonPOM/allure-report/index.html", "wb") as fp:
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
            output="C:/Users/npavankumar/PycharmProjects/SeleniumPythonPOM/reports",
            add_timestamp=True,
            report_title="AutomationReport",
            report_name="OrangeHRMAutomation",
            open_in_browser=True
        ))
