import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.Bugs_Queue_page import BugsQueuePage
from logic.Home_page import HomePage


class BugsQueueTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'firefox'  # Specify your default browser here
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.bugs_queue_page = BugsQueuePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.switch_to_environment(environment_name="dev")

    def test_delete_all_retrospectives_that_have_same_name(self):
        status = self.bugs_queue_page.delete_bugs_queue("New bug", "all")
        self.assertTrue(status, "test_delete_all_retrospectives_that_have_same_name did not succeed")

    def test_delete_all_retrospectives_and_undo(self):
        status = self.bugs_queue_page.undo_delete_all_bugs_queue()
        self.assertTrue(status, "test_delete_all_retrospectives_and_undo did not succeed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
