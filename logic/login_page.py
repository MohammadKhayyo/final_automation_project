from infra.page_base import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    URL_BOARD = "https://mohammadkhayyo12account.monday.com"
    LOGIN = (By.XPATH, '//*[@id="login-monday-container"]/div/div[2]/div/div[1]/div/div[4]/div/button')
    EMAIL = (By.XPATH, '//*[@id="user_email"]')
    PASSWORD = (By.XPATH, '//*[@id="user_password"]')
    ENTER = LOGIN
    switcher_button = (By.XPATH, '//*[@id="product-switcher-button-id"]')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        """Login method to enter credentials and navigate to the board."""
        try:
            self.navigation(self.URL_BOARD)
            self.wait_for_element_and_click(self.LOGIN)
            self.type_text(self.EMAIL, email)
            self.type_text(self.PASSWORD, password)
            self.wait_for_element_and_click(self.ENTER)
            self.wait_for_url(self.URL_BOARD)
            self.wait_for_click_able_element(self.switcher_button)
            return True
        except Exception as E:
            print(E)
            return False
