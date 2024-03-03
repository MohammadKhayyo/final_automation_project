import unittest
from Utils import users
from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.Epics_page import EpicsPage
from logic.Home_page import HomePage
from Utils import generate_string


class ParallelEpicsTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        default_browser = 'firefox'  # Specify your default browser here
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.get_driver(browser=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.epics_Page = EpicsPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.switch_to_environment(environment_name="dev")

    def test_add_epic_and_and_delete_it(self):
        print("test_add_epic_and_and_delete_it")
        task_name = generate_string.create_secure_string()
        status = self.epics_Page.add_new_epic(task_name)  # Use a unique name to ensure the test is reliable
        self.assertTrue(status, "add new task did not succeed")
        status = self.epics_Page.delete_epic(task_name)
        self.assertTrue(status, "Delete The epic did not succeed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
