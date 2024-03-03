from selenium.webdriver.common.by import By
from infra.page_base import BasePage


class EpicsPage(BasePage):
    EPIC_ELEMENT = (By.XPATH,
                    '/html/body/div[1]/div[4]/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[5]/div/div/div/div/div')

    NEW_EPIC_ELEMENT = (By.XPATH,
                        '/html/body/div[1]/div[4]/div[3]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div[1]/button')

    TEXT_NEW_EPIC = (By.XPATH,
                     "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/input")
    NAME_NEW_EPIC = (By.XPATH,
                     "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def add_new_epic(self, epic_name="New epic"):
        return self.add_new(name=epic_name, ELEMENT=self.EPIC_ELEMENT, NEW_ELEMENT=self.NEW_EPIC_ELEMENT,
                            TEXT_NEW=self.TEXT_NEW_EPIC, NAME_NEW=self.NAME_NEW_EPIC, name_new="New epic")

    def delete_epic(self, epic_name="New epic", select_Type="first", browser="chrome"):
        return self.delete_equal(name=epic_name, ELEMENT=self.EPIC_ELEMENT, select_Type=select_Type, browser=browser)

    def delete_all_epic(self, browser="chrome"):
        return self.delete_all(self.EPIC_ELEMENT, NAME_NEW=self.NAME_NEW_EPIC, browser=browser)

    def undo_delete_all_epics(self, browser="chrome"):
        _elements = self.delete_all_epic(browser=browser)
        return self.UNDO_DELETE(list_all_element=_elements, NAME_NEW=self.NAME_NEW_EPIC)
