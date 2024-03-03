import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.Tasks_page import TasksPage
from logic.Home_page import HomePage
from Utils import generate_string


class ParallelTasksTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'firefox'
        browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.tasks_Page = TasksPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.switch_to_environment(environment_name="dev")

    def test_add_Task_and_and_delete_it(self):
        task_name = generate_string.create_secure_string()
        status = self.tasks_Page.add_new_task(task_name)
        self.assertTrue(status, "test_add_Task_and_and_delete_it did not succeed")
        status = self.tasks_Page.delete_tasks(task_name)
        self.assertTrue(status, "test_add_Task_and_and_delete_it did not succeed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
