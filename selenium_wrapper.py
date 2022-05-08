from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#from time import sleep
from demp1 import wait


class Selenium_Wrapper:
    def __init__(self,driver):
        self.driver = driver


    @wait
    def test_click_element(self,locator):
        self.driver.find_element(*locator).click()

    @wait
    def test_enter_text(self, locator, *, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)


    @wait
    def test_select_item(self, locator, *, item):
        element = self.driver.find_element(*locator)
        s = Select(element)
        if isinstance(item,str):
            s.select_by_visible_text(item)
        elif isinstance(item,int):
            s.select_by_index(item)
        else:
            raise TypeError
