import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.Sprints_page import SprintsPage
from logic.Home_page import HomePage
from Utils import generate_string


class ParallelSprintsTests(unittest.TestCase):
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

    def test_add_sprint_and_and_delete_it(self):
        print("test_add_retrospectives_and_and_delete_it")
        task_name = generate_string.create_secure_string()
        status = self.sprints_Page.add_new_sprint(task_name)
        self.assertTrue(status, "add new sprint did not succeed")
        status = self.sprints_Page.delete_sprint(task_name)
        self.assertTrue(status, "Delete the sprint did not succeed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
