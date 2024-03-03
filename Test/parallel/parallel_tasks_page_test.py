import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.Tasks_page import TasksPage
from logic.Home_page import HomePage
from Utils import generate_string


class ParallelTasksPageTests(unittest.TestCase):
    VALID_USERS = users.valid_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'firefox'  # Specify your default browser here
        browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.tasks_Page = TasksPage(self.driver)
        self.home_page = HomePage(self.driver)

    def test_add_Task_and_and_delete_it(self):
        task_name = generate_string.generate_text()
        status = self.tasks_Page.add_new_task(task_name)  # Use a unique name to ensure the test is reliable
        self.assertTrue(status, "add new task did not succeed")
        status = self.tasks_Page.delete_tasks(task_name)
        self.assertTrue(status, "Delete The task did not succeed")

    # def test_delete_all_tasks_that_have_same_name(self):
    #     status = self.tasks_Page.delete_tasks("New task", "all")
    #     self.assertTrue(status, "Delete all tasks that have the name did not succeed")
    #
    # def test_delete_all_task_and_undo(self):
    #     status = self.tasks_Page.undo_delete_all_tasks()
    #     self.assertTrue(status, "test_delete_all_task_and_undo did not succeed")

    def tearDown(self):
        # self.home_page.sign_out()
        if self.driver:
            self.driver.quit()
        # self.browser_wrapper.close_browser(self.driver)
