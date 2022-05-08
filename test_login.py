#
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from time import sleep
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# from config import Config
#
# from demp1 import driver
#
# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://demowebshop.tricentis.com")
# #
# '''class automation'''
#
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         else:
#             return False
#
# def wait(func):
#     def wrapper(*args,**kwargs):
#         instance = args[0]
#         locator = args[1]
#         wait = WebDriverWait(instance.driver,40)
#         v = _visibility_of_element_located(locator)
#         wait.until(v)
#         return func(*args,**kwargs)
#     return wrapper
#
# class Selenium_Wrapper:
#     def __init__(self,driver):
#         self.driver = driver
#
#
#     @wait
#     def test_click_element(self,locator):
#         self.driver.find_element(*locator).click()
#
#     @wait
#     def test_enter_text(self, locator, *, value):
#         self.driver.find_element(*locator).clear()
#         self.driver.find_element(*locator).send_keys(value)
#
#
#     @wait
#     def test_select_item(self, locator, *, item):
#         element = self.driver.find_element(*locator)
#         s = Select(element)
#         if isinstance(item,str):
#             s.select_by_visible_text(item)
#         elif isinstance(item,int):
#             s.select_by_index(item)
#         else:
#             raise TypeError
#
#
# # # '''register'''
# s = Selenium_Wrapper(driver)
# sleep(2)
# s.test_click_element(("link text", "Log in"))
# sleep(2)
# s.test_enter_text(("name","Email"),value='jhdhjhjhjh@gmail.com')
# sleep(2)
# s.test_enter_text(("id","Password"),value='kkkk')
# sleep(5)
# s.test_click_element(('xpath', "//input[@value='Log in']"))
# sleep(2)
# print('pass')