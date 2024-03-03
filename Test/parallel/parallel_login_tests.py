import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage


class ParallelLoginTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = "firefox"
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=self.browser)
        self.login_page = LoginPage(self.driver)


    def test_login_with_valid_user(self):
        print("test_login_with_valid_user")
        for user in self.VALID_USERS:
            status = self.login_page.login(user['email'], user['password'])
            self.assertTrue(status)

    def tearDown(self):
        if self.driver:
            self.driver.quit()
