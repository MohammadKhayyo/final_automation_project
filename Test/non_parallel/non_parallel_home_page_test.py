import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.Home_page import HomePage


class NonParallelHomePageTests(unittest.TestCase):
    VALID_USERS = users.valid_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'firefox'  # Specify your default browser here
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.home_page = HomePage(self.driver)

    def test_switch_between_environments(self):
        print("test_switch_between_environments")
        name = self.home_page.switch_to_environment(environment_name="sales CRM")
        self.assertEqual(name, "sales CRM", "You are not in a sales CRM environment")
        name = self.home_page.switch_to_environment(environment_name="dev")
        self.assertEqual(name, "dev", "You are not in a dev environment")

    def test_sign_out(self):
        print("test_sign_out")
        status = self.home_page.sign_out()
        self.assertTrue(status, "test_sign_out filed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
        # self.browser_wrapper.close_browser(self.driver)
