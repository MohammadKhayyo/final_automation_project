from selenium.webdriver.common.by import By
from infra.page_base import BasePage
from selenium.webdriver.support.ui import WebDriverWait


class HomePage(BasePage):
    switcher_button = (By.XPATH, '//*[@id="product-switcher-button-id"]')
    DIV_BUTTON = (By.XPATH, '//*[@id="main"]/span/div/div/div/div[1]/div[2]/div[1]/div/clickable')
    SALES_CRM = (By.XPATH, '//*[@id="main"]/span/div/div/div/div[1]/div[2]/div[2]/div/clickable')
    environment_name = (By.XPATH, '//*[@id="mf-topbar"]/div/div/div[1]/div[2]/h1/span[2]')
    DROP_DOWN_LIST = (By.XPATH, '//*[@id="surface-avatar-menu-component"]/div/div/div/img')
    SIGN_OUT = (
        By.XPATH, "//div[contains(@class, 'monday-deprecated-menu-item') and .//span[contains(text(), 'Log out')]]")
    LOGIN = (By.XPATH, '//*[@id="login-monday-container"]/div/div[2]/div/div[1]/div/div[4]/div/button')

    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_environment(self, environment_name='dev'):
        try:
            self.wait_for_element_and_click(self.switcher_button)
            if environment_name == 'dev':
                self.wait_for_element_and_click(self.DIV_BUTTON)
            elif environment_name == "sales CRM":
                self.wait_for_element_and_click(self.SALES_CRM)
            count = 0
            environment_span = None
            while count <= 10:
                environment_span = self.wait_presence_of_element_located(self.environment_name)
                try:
                    WebDriverWait(self._driver, 3).until(lambda driver: environment_name == environment_span.text)
                    break
                except:
                    environment_span = self.wait_presence_of_element_located(self.environment_name)
                    count += 1
            environment_span = self.wait_presence_of_element_located(self.environment_name)
            name = environment_span.text
            return name
        except Exception as E:
            print(E)
            return "ERROR 404"

    def sign_out(self):
        """Sign out method to log out from the application."""
        try:
            self.wait_for_element_and_click(self.DROP_DOWN_LIST)
            self.wait_for_element_and_click(self.SIGN_OUT)
            self.wait_for_element_and_click(self.LOGIN)
            return True
        except Exception as E:
            print(E)
            return False
