import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.Tasks_page import TasksPage
from logic.Home_page import HomePage


class SerialTasksTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'chrome'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.tasks_Page = TasksPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.switch_to_environment(environment_name="dev")

    def test_delete_all_tasks_that_have_same_name(self):
        status = self.tasks_Page.delete_tasks("New task", "all")
        self.assertTrue(status, "test_delete_all_tasks_that_have_same_name did not succeed")

    def test_delete_all_task_and_undo(self):
        status = self.tasks_Page.undo_delete_all_tasks()
        self.assertTrue(status, "test_delete_all_task_and_undo did not succeed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
