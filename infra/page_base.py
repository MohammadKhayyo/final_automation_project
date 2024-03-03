from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class BasePage():
    NUTRITIONAL_TARGET_NAVIGATION = (By.XPATH, "//a[@type='button']/span[text()='Nutrition Targets']")
    MENU = (By.XPATH, "//button[@title='Open Menu']")
    DIET_NUTRITION_NAVIGATION = (By.XPATH, "//button/svg[text()='Diet & Nutrition']")
    Main_table = (By.XPATH, "//button[.//span[contains(text(), 'Main Table')]]")
    Main_table_Tasks = (By.XPATH, '//*[@id="board-header"]/div/div/div[2]/div[2]/div[4]/button')
    board = (
        By.XPATH,
        "//*[starts-with(@id, 'row-header-currentBoard-') and contains(@id, '-notfloating-focus-name-')]/div[3]")
    button_filter_in_search = (
        By.XPATH, '//*[@id="board-header-view-bar"]/div/div[3]/div[1]/div/div[2]/div/div/span/button')
    name_after_click_in_item_with_filter = (By.XPATH,
                                            "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div")
    CHECK_BOX = (
        By.XPATH, "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[2]")
    page_choose_columns = (By.XPATH, '//*[@id="main"]/span/div/div/div')
    text_how_many_columns = (By.XPATH, '//*[@id="main"]/span/div/div/div/div[3]/div[1]/label[2]')
    all_columns_button = (By.XPATH, '//*[@id="main"]/span/div/div/div/div[3]/div[1]/label[1]')
    name_columns_button = (By.XPATH, '//*[@id="main"]/span/div/div/div/div[3]/div[2]/label')
    DELETE_BUTTON = (By.XPATH, '//*[@id="board-wrapper-first-level-content"]/div[4]/div/div/div/div[7]')
    DELETE_ANYWAY_BUTTON = (By.XPATH, '//*[@id="main"]/*/div/div/div/div/div/span/button[2]')
    SEARCH_WITHOUT_CLICK = (By.XPATH, '//*[@id="board-header-view-bar"]/div[1]/div[3]/div[1]')
    SEARCH_WITH_CLICK = (By.XPATH, '//*[@id="board-header-view-bar"]/div[1]/div[3]/div[1]/div/div[1]/input')
    X_SEARCH = (By.XPATH, '//*[@id="board-header-view-bar"]/div[1]/div[3]/div[1]/div/div[2]/span/button')
    ALL_CHECK_BOX_ = (By.XPATH,
                      "//*[starts-with(@id, 'row-header-currentBoard-') and contains(@id, '-notfloating-focus-name-')]/div[2]")
    UNDO = (By.XPATH, '//*[@id="main"]/div[24]/div[1]/div/div[2]/button')

    DELETE_ANYWAY_BUTTON_fire_fox = DELETE_ANYWAY_BUTTON
    description = (By.XPATH, '//*[@id="board-header"]/div/div/div[1]/div/div[1]/div/div[2]/span/button')

    MY_TEAM_SEARCH = (By.XPATH, '//*[@id="boards-list-search-input"]')

    def __init__(self, driver):
        self._driver = driver

    def wait_for_element_and_click(self, locator):
        """Wait for an element to be clickable and then click."""
        WebDriverWait(self._driver, 30).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self._driver, 30).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def wait_presence_of_element_located(self, locator):
        return WebDriverWait(self._driver, 30).until(EC.presence_of_element_located(locator))

    def type_text(self, locator, text):
        """Type text into a field located by a specific locator."""
        field = self.wait_presence_of_element_located(locator)
        field.clear()
        field.send_keys(text)

    def navigation(self, url):
        self._driver.get(url)

    def wait_for_url(self, url):
        WebDriverWait(self._driver, 30).until(lambda driver: url in driver.current_url)

    def wait_for_text(self, url):
        WebDriverWait(self._driver, 30).until(lambda driver: url in driver.current_url)

    def wait_for_click_able_element(self, locator):
        """Wait for an element to be clickable and then click."""
        self.wait_presence_of_element_located(locator)
        element = WebDriverWait(self._driver, 30).until(EC.element_to_be_clickable(locator))
        return element

    def switch_to_element(self, ELEMENT, tab):
        try:
            self.wait_for_click_able_element(self.MY_TEAM_SEARCH)
            self.wait_for_click_able_element(ELEMENT)
            self.wait_for_element_and_click(ELEMENT)
            self.wait_for_click_able_element(tab)
            self.wait_for_element_and_click(tab)
        except:
            self.wait_for_click_able_element(ELEMENT)
            self.wait_for_element_and_click(ELEMENT)
            self.wait_for_click_able_element(tab)
            self.wait_for_element_and_click(tab)

    def add_new(self, name, ELEMENT, NEW_ELEMENT, TEXT_NEW, NAME_NEW, name_new, Task=False):
        self.switch_to_element(ELEMENT, self.Main_table)
        # if Task:
        #     self.wait_for_click_able_element(self.Main_table_Tasks)
        #     self.wait_for_element_and_click(self.Main_table_Tasks)
            # self.switch_to_element(ELEMENT, self.Main_table_Tasks)
        self.wait_for_element_and_click(NEW_ELEMENT)
        try:
            name_field = self.wait_for_click_able_element(TEXT_NEW)
        except:
            names = self._driver.find_elements(*NAME_NEW)
            for element in names:
                if element.text.lower() == name_new.lower():
                    element.click()
                    break
            try:
                name_field = self.wait_for_click_able_element(TEXT_NEW)
            except:
                return False
        name_field.send_keys(Keys.CONTROL + "a")
        name_field.send_keys(Keys.DELETE)
        name_field.send_keys(name)
        name_field.send_keys(Keys.ENTER)
        return True

    def select(self, select_Type, names, check_boxes, name):
        count = 0
        list_EM = list()
        actions = ActionChains(self._driver)
        board = self._driver.find_elements(*self.board)
        board[0].click()
        for index, _name in enumerate(names):
            if _name.text.lower() == name.lower():
                count += 1
                list_EM.append(_name)
                not_click = True
                while not_click:
                    try:
                        check_boxes[index].click()
                        not_click = False
                    except:
                        actions.send_keys(Keys.ARROW_DOWN * 3).perform()
                if select_Type == 'first':
                    break
        return list_EM, count

    def search(self, ELEMENT, name, Task=False):
        self.switch_to_element(ELEMENT, self.Main_table)
        # if Task:
        #     self.wait_for_click_able_element(self.Main_table_Tasks)
        #     self.wait_for_element_and_click(self.Main_table_Tasks)
        self.wait_for_element_and_click(self.SEARCH_WITHOUT_CLICK)
        _input = self.wait_presence_of_element_located(self.SEARCH_WITH_CLICK)
        _input.send_keys(Keys.CONTROL + "a")
        _input.send_keys(Keys.DELETE)
        _input.send_keys(name)
        _input.send_keys(Keys.ENTER)
        WebDriverWait(self._driver, 30).until(lambda driver: _input.get_attribute("value") == name)
        self.filter_in_search_By_column_only(self.name_columns_button)
        self.wait_for_click_able_element(self.X_SEARCH)
        self.wait_for_click_able_element(self.button_filter_in_search)
        try:
            self.wait_for_click_able_element(self.name_after_click_in_item_with_filter)
            names = self._driver.find_elements(*self.name_after_click_in_item_with_filter)
            check_boxes = self._driver.find_elements(*self.CHECK_BOX)
            return names, check_boxes
        except:
            return None, None

    def filter_in_search_By_column_only(self, column_name):
        self.wait_for_element_and_click(self.button_filter_in_search)
        WebDriverWait(self._driver, 30).until(EC.presence_of_element_located(self.page_choose_columns))
        _text = WebDriverWait(self._driver, 30).until(EC.presence_of_element_located(self.text_how_many_columns))
        _text = _text.text
        if _text != "0 selected":
            self.wait_for_element_and_click(self.all_columns_button)
        _text = WebDriverWait(self._driver, 30).until(EC.presence_of_element_located(self.text_how_many_columns))
        _text = _text.text
        self.wait_for_element_and_click(column_name)
        self.wait_for_element_and_click(self.button_filter_in_search)

    def check_search(self, ELEMENT, name="New task", Task=False):
        names, check_boxes = self.search(ELEMENT=ELEMENT, name=name, Task=Task)
        try:
            EM_names = self._driver.find_elements(*self.name_after_click_in_item_with_filter)
        except:
            if names is None:
                return True
            else:
                return False
        board = self._driver.find_elements(*self.board)
        board[0].click()
        count = 0
        actions = ActionChains(self._driver)
        for _name in EM_names:
            count += 1
            actions.send_keys(Keys.ARROW_DOWN).perform()
        if count == len(names):
            return True
        else:
            return False

    def delete_equal(self, name, ELEMENT, select_Type="first", Task=False):
        try:
            names, check_boxes = self.search(ELEMENT=ELEMENT, name=name, Task=Task)
            if names is None or len(names) == 0:
                return True
            list_EM, count = self.select(select_Type=select_Type, name=name, names=names, check_boxes=check_boxes)
            if (len(list_EM) != 0 and count == 0) or (count != 0 and len(list_EM) == 0):
                return False
            if count == 0:
                return True
            self.wait_for_click_able_element(self.DELETE_BUTTON)
            self.wait_for_element_and_click(self.DELETE_BUTTON)
            self.wait_for_click_able_element(self.DELETE_ANYWAY_BUTTON)
            self.wait_for_element_and_click(self.DELETE_ANYWAY_BUTTON)

            return True
        except:
            return False

    def delete_all(self, ELEMENT, NAME_NEW, Task=False):
        # self.switch_to_element(ELEMENT, self.Main_table)
        # if Task:
        #     self.wait_for_click_able_element(self.Main_table_Tasks)
        #     self.wait_for_element_and_click(self.Main_table_Tasks)
        try:
            self.switch_to_element(ELEMENT, self.Main_table)
            # self.wait_for_click_able_element(NAME_NEW)
            # self.wait_for_click_able_element(NAME_NEW)
        except:
            return list()
        self.wait_for_click_able_element(ELEMENT)
        self.wait_for_click_able_element(self.board)
        self.wait_for_element_and_click(self.board)
        # WebDriverWait(self._driver, 30).until(EC.presence_of_all_elements_located(NAME_NEW))
        try:
            names = self._driver.find_elements(*NAME_NEW)
        except:
            WebDriverWait(self._driver, 30).until(EC.presence_of_all_elements_located(NAME_NEW))
            names = self._driver.find_elements(*NAME_NEW)
        if names is None or len(names) == 0:
            return list()
        list_all_element = list()
        for name in names:
            list_all_element.append(name.text)
        self.wait_for_click_able_element(ELEMENT)
        # self.wait_for_element_and_click(ELEMENT)
        count = 0
        try:
            # WebDriverWait(self._driver, 30).until(EC.presence_of_all_elements_located(self.ALL_CHECK_BOX_))
            elements = self._driver.find_elements(*self.ALL_CHECK_BOX_)
        except:
            return None
        for element in elements:
            try:
                element.click()
                count += 1
            except:
                pass
        if count == 0:
            return list_all_element
        self.wait_for_click_able_element(self.DELETE_BUTTON)
        self.wait_for_element_and_click(self.DELETE_BUTTON)
        self.wait_for_click_able_element(self.DELETE_ANYWAY_BUTTON)
        self.wait_for_element_and_click(self.DELETE_ANYWAY_BUTTON)

        # for element in elements:
        #     try:
        #         element.click()
        #     except:
        #         pass
        return list_all_element

    def UNDO_DELETE(self, list_all_element, NAME_NEW):
        if not list_all_element or len(list_all_element) == 0:
            return True
        self.wait_for_element_and_click(self.UNDO)
        self.wait_for_click_able_element(NAME_NEW)
        names = self._driver.find_elements(*NAME_NEW)
        if len(list_all_element) != len(names):
            return False
        sorted_names = list()
        for name in names:
            sorted_names.append(name.text)
        sorted_names = sorted(sorted_names)
        sorted_list_all_element = sorted(list_all_element)
        for i in range(len(sorted_names)):
            if sorted_names[i] != sorted_list_all_element[i]:
                return False
        return True

    def get_xpath(self, element):
        """
        Generates an XPath selector for the given Selenium element.
        """
        components = []
        child = element
        while child is not None:
            # Use the updated method to find the parent element
            parent = child.find_element(By.XPATH, '..')
            siblings = parent.find_elements(By.XPATH, child.tag_name)
            if len(siblings) == 1:
                components.append(child.tag_name)
            else:
                index = 1 + siblings.index(child)
                components.append(f"{child.tag_name}[{index}]")
            child = parent if parent.tag_name != "html" else None

        components.reverse()
        return '/' + '/'.join(components)
