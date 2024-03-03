import time
from os.path import dirname, join
from selenium import webdriver
from infra.config_loader import ConfigLoader


class BrowserWrapper:

    def __init__(self):
        self.driver = None
        configloader = ConfigLoader()
        self.config = configloader.load_config()

    def get_driver(self, browser):
        browser_type = self.config["browser"]
        if self.config["grid"]:
            options = self.set_up_capabilities(browser)
            self.driver = webdriver.Remote(command_executor=self.config["hub"], options=options)
        else:
            if browser.lower() == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser.lower() == 'edge':
                self.driver = webdriver.Edge()
        url = self.config["url"]
        self.driver.get(url)
        # time.sleep(5)
        self.driver.maximize_window()
        return self.driver

    def close_browser(self, driver):
        if driver:
            driver.close()

    def set_up_capabilities(self, browser_type):
        options = None
        if browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser_type.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
        elif browser_type.lower() == 'edge':
            options = webdriver.EdgeOptions()
        if options is not None:
            platform_name = self.config["platform"]
            options.add_argument(f'--platformName={platform_name}')
            print(options)
            return options
        else:
            raise ValueError("Unsupported browser type")

    def is_parallel(self):
        return self.config['parallel']

    def get_browsers(self):
        return self.config["browser_types"]

    def get_filename(self, filename):
        here = dirname(__file__)
        output = join(here, filename)
        return output

    def is_grid(self):
        return self.config['grid']

    def get_browser(self):
        return self.config['browser']
