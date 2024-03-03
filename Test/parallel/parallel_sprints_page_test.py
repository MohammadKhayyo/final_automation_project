import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.Sprints_page import SprintsPage
from logic.Home_page import HomePage
from Utils import generate_string


class ParallelSprintPageTests(unittest.TestCase):
    VALID_USERS = users.valid_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'chrome'  # Specify your default browser here
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.sprints_Page = SprintsPage(self.driver)
        self.home_page = HomePage(self.driver)

    def test_add_sprint_and_and_delete_it(self):
        print("test_add_sprint_and_and_delete_it")
        task_name = generate_string.generate_text()
        status = self.sprints_Page.add_new_sprint(task_name)  # Use a unique name to ensure the test is reliable
        self.assertTrue(status, "add new sprint did not succeed")
        status = self.sprints_Page.delete_sprint(task_name)
        self.assertTrue(status, "Delete the sprint did not succeed")

    # def test_delete_all_sprints_that_have_same_name(self):
    #     status = self.sprints_Page.delete_sprint("New sprint", "all")
    #     self.assertTrue(status, "Delete all tasks that have the name did not succeed")
    #
    # def test_delete_all_sprint_and_undo(self):
    #     status = self.sprints_Page.undo_delete_all_sprints()
    #     self.assertTrue(status, "test_delete_all_task_and_undo did not succeed")

    def tearDown(self):
        # self.home_page.sign_out()
        if self.driver:
            self.driver.quit()
        # self.browser_wrapper.close_browser(self.driver)
