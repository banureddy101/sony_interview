
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


def test_login(_driver):

    s = Selenium_Wrapper(_driver)
    sleep(2)
    s.test_click_element(("link text", "Log in"))
    sleep(2)
    s.test_enter_text(("name","Email"),value='jhdhjhjhjh@gmail.com')
    sleep(2)
    s.test_enter_text(("id","Password"),value='kkkk')
    sleep(5)
    s.test_click_element(('xpath', "//input[@value='Log in']"))
    sleep(2)
    print('pass')