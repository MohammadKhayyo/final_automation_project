import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.Sprints_page import SprintsPage
from logic.Home_page import HomePage


class NonParallelSprintPageTests(unittest.TestCase):
    VALID_USERS = users.valid_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'firefox'  # Specify your default browser here
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.sprints_Page = SprintsPage(self.driver)
        self.home_page = HomePage(self.driver)

    # def test_add_sprint_and_and_delete_it(self):
    #     status = self.sprints_Page.add_new_sprint(
    #         "Sprint Example 1")  # Use a unique name to ensure the test is reliable
    #     self.assertTrue(status, "add new task did not succeed")
    #     status = self.sprints_Page.delete_sprint("Sprint Example 1")
    #     self.assertTrue(status, "Delete all tasks that have the name did not succeed")

    def test_delete_all_sprints_that_have_same_name(self):
        print("test_delete_all_sprints_that_have_same_name")
        status = self.sprints_Page.delete_sprint("New sprint", "all", browser=self.browser)
        self.assertTrue(status, "Delete all sprints that have the name did not succeed")

    def test_delete_all_sprint_and_undo(self):
        print("test_delete_all_sprint_and_undo")
        status = self.sprints_Page.undo_delete_all_sprints(browser=self.browser)
        self.assertTrue(status, "test_delete_all_sprint_and_undo did not succeed")

    def tearDown(self):
        # self.home_page.sign_out()
        if self.driver:
            self.driver.quit()
        # self.browser_wrapper.close_browser(self.driver)
