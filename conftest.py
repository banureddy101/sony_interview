from _pytest.fixtures import fixture
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

#fixture is function

@fixture                    # it is function
def _driver():
    driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
    driver.maximize_window()
    driver.get(Config.URL)
    sleep(3)
    yield driver                #pass the instance to all the test methods
    driver.quit()
    # driver.close()   # it will close the current tab