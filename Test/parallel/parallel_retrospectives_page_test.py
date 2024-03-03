import unittest
from Utils import users
from infra.browser_wrapper import WebDriverManager
from logic.login_page import LoginPage
from logic.Retrospectives_page import RetrospectivesPage
from logic.Home_page import HomePage
from Utils import generate_string


class ParallelRetrospectivesTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = WebDriverManager()
        default_browser = 'chrome'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.retrospectives_page = RetrospectivesPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.changeEnvironment(environment_name="dev")

    def test_create_and_remove_retrospective(self):
        task_name = generate_string.create_secure_string()
        creationStatus = self.retrospectives_page.add_new_retrospective(task_name)
        self.assertTrue(creationStatus, "Creation of a new retrospective failed")
        deletionStatus = self.retrospectives_page.bulkDeleteRetrospectives(task_name)
        self.assertTrue(deletionStatus, "Deletion of the retrospective failed")



    def tearDown(self):
        if self.driver:
            self.driver.quit()
