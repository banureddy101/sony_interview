
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from pytest import fixture
from config import Config

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from config import Config

from demp1 import driver
from selenium_wrapper import Selenium_Wrapper
from pytest import mark


def test_registration(_driver):
    s = Selenium_Wrapper(_driver)
    sleep(2)
    s.test_click_element(("link text", "Register"))
    sleep(2)
    s.test_click_element(("id","gender-male"))
    sleep(2)
    s.test_enter_text(("id","FirstName"),value='kkkk')
    sleep(2)
    s.test_enter_text(("id","LastName"),value='fhfh')
    sleep(2)
    s.test_enter_text(("name","Email"),value='jhdhjhjhjh@gmail.com')
    sleep(2)
    s.test_enter_text(("name","Password"),value = '12324242')
    sleep(2)
    s.test_enter_text(("name","ConfirmPassword"),value='12324242')
    sleep(2)
    s.test_click_element(("id","register-button"))
    print("pass")