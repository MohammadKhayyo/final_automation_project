import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.Sprints_page import SprintsPage
from logic.Home_page import HomePage


class SerialSprintsTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'chrome'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.sprints_Page = SprintsPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.switch_to_environment(environment_name="dev")

    def test_delete_all_sprints_that_have_same_name(self):
        status = self.sprints_Page.delete_sprint("New sprint", "all")
        self.assertTrue(status, "Delete all sprints that have the name did not succeed")

    def test_delete_all_sprint_and_undo(self):
        status = self.sprints_Page.undo_delete_all_sprints()
        self.assertTrue(status, "test_delete_all_sprint_and_undo did not succeed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
