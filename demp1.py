import re
import driver as driver
import selenium.webdriver.firefox.webelement
import self as self
from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/")
from selenium.webdriver.support.wait import WebDriverWait

driver.minimize_window()
sleep(2)
driver.maximize_window()
sleep(2)
driver.close()

d=driver.find_element_by_link_text("Register").click()
sleep(1)
d=driver.find_element_by_id("gender-male").click()
sleep(1)
d=driver.find_element_by_id("FirstName").send_keys('hello')
sleep(1)
d=driver.find_element_by_id("LastName").send_keys('hai')
sleep(1)
d=driver.find_element_by_id("Email").send_keys('zzzzzzzz999999@gmail.com')
sleep(1)
d=driver.find_element_by_id("Password").send_keys('123456')
sleep(1)
d=driver.find_element_by_id("ConfirmPassword").send_keys('123456')
sleep(1)
d=driver.find_element_by_id("register-button").click()
sleep(1)

#driver.get("file:///C:/Users/pc/Downloads/xpath.html")

###Absulute X path###
# driver.get("file:///D:/selineium/demo-html/xpath.html")
# driver.find_element_by_xpath("/html/body/div[1]/input[1]").send_keys('banu')
#
# driver.find_element_by_xpath("/html/body/div[1]/input[2]").send_keys('prathap')
#
# driver.find_element_by_xpath("/html/body/div[2]/input[1]").send_keys('TYSSS')
# driver.find_element_by_xpath("/html/body/div[2]/input[2]").send_keys('BLR')

###Related X path###

'''driver.find_element_by_xpath('//a[@class="ico-register"]').click()
sleep(1)
driver.find_element_by_xpath('//input[@id="gender-male"]').click()
sleep(1)
driver.find_element_by_xpath('//input[@id="FirstName"]').send_keys('banu')
driver.find_element_by_xpath('//input[@id="LastName"]').send_keys('prathap')
driver.find_element_by_xpath('//input[@id="Email"]').send_keys('dddddd@gmail.com')
driver.find_element_by_xpath('//input[@id="Password"]').send_keys('fgfgfgf')
driver.find_element_by_xpath('//input[@id="ConfirmPassword"]').send_keys('fgfgfgf')
driver.find_element_by_xpath('//input[@id="register-button"]').click()'''

#driver.find_element_by_xpath("//a[text()='Register']").click()
#driver.find_element_by_xpath("//a[text()='Log in']").click()
#driver.find_element_by_xpath("//a[text()='Shopping cart']").click()
#driver.find_element_by_xpath("//a[text()='Wishlist']").click()




# driver.find_element_by_xpath("//a[text()='Health Book']/../..//input[@value='Add to cart']")
# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.get("http://demowebshop.tricentis.com")
# driver.find_element_by_xpath1("//a[text()='Health Book']/../..//input[@value='Add to cart']").click()


#
# x = ("//div[@class='block block-category-navigation']//a")
# link=driver.find_elements_by_xpath(x)
# for i in link:
#     print(i.text)

# x = ("//div[@class='footer']//a")
# link=driver.find_elements_by_xpath(x)
# for i in link:
#     print(i.text)
# driver.get


# driver.get("https://www.monsterindia.com").send_keys('python')
# driver.find_element_by_xpath().click()
##single select##
# from selenium.webdriver.support.select import Select
# driver.get("file:///D:/selineium/demo-html/demo.html")
# cars = driver.find_element_by_id('standard_cars')
# s = Select(cars)
# s.deselect_by_index(4)
# s.select_by_visible_text("Mercedes")
# s.select_by_visible_text("Audi")
# s.select_by_visible_text("BMW")

# all_options = s.options
# text_options = [item.text for item in all_options]

# type(all_options)
# for item in all_options:
#print(text_options)

##multiple  selct###
# from selenium.webdriver.support.select import Select
# driver.get("file:///D:/selineium/demo-html/demo.html")
# cars = driver.find_element_by_id('multiple_cars')
# s = Select(cars)
# items=['Audi','BMW','Honda']
# for item in items:
#     s.select_by_visible_text(item)
# s.deselect_by_index(4)
# s.select_by_visible_text("Mercedes")
# s.select_by_visible_text("Audi")
# s.select_by_visible_text("BMW")

# all_options = s.options
# text_options = [item.text for item in all_options]

# type(all_options)
# for item in all_options:
# print(item)


# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.get("http://demowebshop.tricentis.com/books")
# driver.find_element_by_xpath("//a[text()='Fiction']/../..//input[@value='Add to cart']").click()
#
#
#
# #
# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/sunglasses")
# sleep(1)
# # driver.find_element_by_xpath().click()
# sun_glasses = {'Sunglasses Aero':139.00,'ORIGINAL COLLECTION':149.00,'Custom Sunglasses':179.00}
# for glass,expected_price in sun_glasses.items():
#     _xpath = f"//span[text()='{glass}']/../../..//span[@class='art-price']"
#     actual_price = driver.find_element_by_xpath(_xpath).text
#     actual_price = re.findall(r"[\d.]", actual_price)
#     _temp = float("".join(actual_price))
#     if _temp == expected_price:
#         print("pass")
#     else:
#         print("fail")
#     sleep(1)
# driver.close()


# monster#
# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.get("https://www.monsterindia.com")
# sleep(3)
# driver.find_element_by_xpath("//input[@id='SE_home_autocomplete']").send_keys('python')
# sleep(3)
# driver.find_element_by_xpath("//button[@class='No thanks']").click()
# sleep(1)
# driver.find_element_by_xpath("//input[@value='Search']").click()
# job_title=driver.find_elements_by_xpath("//div[@class='job-tittle']/h3/a")
# for job_titles in job_title:
#     print(job_titles.text)
#     # sleep(0.5)
# driver.close()
#

#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.remote.webelement import WebElement
# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.get("file:///D:/selineium/demo-html/loading.html")
# # sleep(10)
# wait = WebDriverWait(driver, 30)
# txt_fname=driver.find_element_by_name('fname')
# #edit firstname
# txt_fname.send_keys('hello')
# #
# # driver.find_element_by_xpath("//a[text()='Health Book']/../..//input[@value='Add to cart']")
# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://demowebshop.tricentis.com")
# sleep(2)
# driver.find_element_by_link_text("Google+").click()
# #get the window id's all the windows that the selenium has opened
# window_ids = driver.window_handles
# driver.switch_to.window(window_ids[1])
# sleep(10)
# driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("hello")
# sleep(5)
# driver.switch_to.window(window_ids[0])
# sleep(5)
# driver.find_element_by_xpath("//a[text()='Log in']").click()
# sleep(2)
# print(window_ids)




#
# from selenium.common.exceptions import NoSuchElementException
# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://www.goibibo.com")
# sleep(5)
# driver.find_element_by_xpath("//span[text()='Departure']").click()
# sleep(2)
# _month = 'November 2022'
# _day = int(25)
# for _ in range(12):
#     try:
#         driver.find_element_by_xpath(f"//div[text()='{_month}']")
#         break
#     except NoSuchElementException:
#         driver.find_element_by_xpath("//span[@aria-label='Next Month']").click()
#         sleep(1)
#         continue
# try:
#     driver.find_element_by_xpath("f//div[text()={_day}]").click()
# except NoSuchElementException:
#     print("invalid date")

# driver.close()



#
# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://demowebshop.tricentis.com")
# sleep(2)
# driver.find_element_by_link_text("Facebook").click()
# # get the window id's all the windows that the selenium has opened
# window_ids = driver.window_handles
# driver.switch_to.window(window_ids[1])
# sleep(2)
# driver.find_element_by_name('email').send_keys('bprathapreddy6@gmail.com')
# sleep(5)
# driver.find_element_by_name("pass").send_keys('Amma@101')
# driver.close()
# sleep(2)
# driver.find_element_by_name('Log In').click()
# sleep(1)
# driver.switch_to.window(window_ids[0])9902567101)# sleep(5)
# driver.find_element_by_xpath("//a[text()='Log in']").click()
# sleep(2)
# print(window_ids)



# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://mail.google.com/mail/?tab=rm&authuser=0&ogbl")
# sleep(2)
# driver.find_element_by_link_text("Gmail").click()
# get the window id's all the windows that the selenium has opened
# window_ids = driver.window_handles
# driver.switch_to.window(window_ids[1])
# sleep(2)
# driver.find_element_by_xpath("//input[@type='email']").send_keys('bpreddy101@gmail.com')
# sleep(5)
# driver.find_element_by_xpath("//span[text()='Next']").click()
# driver.find_element_by_name("pass").send_keys('Amma@101')
# driver.close()
# sleep(2)
# driver.find_element_by_name('Log In').click()
# sleep(1)

'''naukari  resume login'''

# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
# driver.implicitly_wait(30)
# driver.find_element_by_id('name').send_keys('Banuprathap PV')
# sleep(2)
# driver.find_element_by_id('email').send_keys('bpreddy101@sjcit.ac.in')
# sleep(2)
# driver.find_element_by_id('password').send_keys('Amma@101')
# sleep(3)
# driver.find_element_by_id('mobile').send_keys('9902567101')
# driver.implicitly_wait(30)
# driver.find_element_by_id('resumeUpload').send_keys(r'C:\Users\pc\PycharmProjects\_selenium\BANUPRATHAP PV resume Mtech.txt.doc')
# sleep(2)


'''mouse actions'''
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
# sleep(1)
# actions = ActionChains(driver)

'''Gmail getting error due to chrome problem'''
# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://accounts.google.com")
# driver.implicitly_wait(20)
# driver.find_element_by_xpath("//input[@type='email']").send_keys('bpreddy101@gmail.com')
# sleep(5)
# driver.find_element_by_xpath("//span [text()='Next']").click()



'''whatapp'''
#
# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://web.whatsapp.com")
# driver.implicitly_wait(20)
# # driver.find_element_by_xpath.send_keys('bpreddy101@gmail.com')
# # sleep(5)
# # driver.find_element_by_xpath("//span [text()='Next']").click()


# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://demowebshop.tricentis.com")
# #driver.get("file:///D:/selineium/demo-html/demo.html")
# driver.implicitly_wait(20)
# driver.find_element_by_link_text("Register").click()
# sleep(5)
# print(b)
# driver.find_element_by_id("small-searchterms").send_keys('hello','world')
# sleep(5)
# driver.find_element_by_id("small-searchterms").clear()
# v=driver.find_element_by_link_text("Log in").tag_name
# print(v)

# print(driver.find_element_by_id("gender-male").is_selected())
# sleep(5)


# c=driver.find_element_by_id("gender-female").is_selected()
# sleep(10)
# print(c)

# a=driver.find_element_by_name("q").size
# b=driver.find_element_by_name("q").location
# c=driver.find_element_by_name('q').rect
# print(a)

#a = driver.find_element_by_xpath("//label[text()='Apple']").is_selected()
# sleep(4)
#print(a)






# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://demowebshop.tricentis.com")
# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self,driver):
#         result = super().__call__(driver)
#         if isinstance(result,WebElement):
#             return result.is_enabled()
#         else:
#             return False
#
# def wait(func):
#     def wrapper(*args,**kwargs):
#         locator = args[0]
#         wait = WebDriverWait(driver,20)
#         v = _visibility_of_element_located(locator)
#         wait.until(v)
#         return func(*args,**kwargs)
#     return wrapper
#
# @wait
# def click_element(locator):
#     driver.find_element(*locator).click()
#
# @wait
# def enter_text(locator,value):
#     driver.find_element(*locator).clear()
#     driver.find_element(*locator).send_keys(value)

#
# @wait
# def select_item(locator,item):
#     element = driver.find_element(*locator)
#     s = Select(element)
#     if isinstance(item,str):
#         s.select_by_visible_text(item)
#     elif isinstance(item,int):
#         s.select_by_index(item)
#     else:
#         raise TypeError


'''register'''
#
# click_element(("link text","Register"))
# click_element(("id","gender-male"))
# enter_text(("id","FirstName"),value='kkkk')
# enter_text(("id","LastName"),value='fhfh')
# enter_text(("name","Email"),value='jhdhjhjhjh@gmail.com')
# enter_text(("name","Password"),value = '12324242')
# enter_text(("name","ConfirmPassword"),value='12324242')
# click_element(("id","register-button"))

'''add cart'''

# click_element(("link text","Books"))
# sleep(3)
# click_element(("link text","Computing and Internet"))
# sleep(3)
# click_element(("id","add-to-cart-button-13"))
# sleep(1)
# click_element(("link text","Fiction"))
# sleep(3)
# click_element(("id","add-to-cart-button-45"))

#
# ent(("link text","Books"))
# sleep(3)
# click_element(("link text","Computing and Internet"))
# sleep(3)
# click_element(("id","add-to-cart-button-13"))
# sleep(1)
# click_element(("link text","Fiction"))
# gssleep(3)
# click_element(("id","add-to-cart-button-45"))

# @wait
# def enter_element(locator,value):
#     driver.find_element(locator).clear()
#     driver.find_element(locator).send_keys(value)

# @wait
# def select_item(locator,item):
#     element=driver.find_element(locator)
#     s = Select(element)
#     if isinstance(item,str):
#         s.select_by_visible_text(item)
#         if isinstance(item,int):
#             s.select_by_index(item)
#         else:
#             raise TypeError

#text
#
#
#


'''class automation'''
# driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("http://demowebshop.tricentis.com")
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self,driver):
#         result = super().__call__(driver)
#         if isinstance(result,WebElement):
#             return result.is_enabled()
#         else:
#             return False
#
# def wait(func):
#     def wrapper(*args,**kwargs):
#         instance = args[0]
#         locator = args[1]
#         wait = WebDriverWait(instance.driver,10)
#         v = _visibility_of_element_located(locator)
#         wait.until(v)
#         return func(*args,**kwargs)
#     return wrapper
#
# class Selenium_Wrapper:
#     def __init__(self,driver):
#         self.driver = driver

    # def click_element(self, *locator):
    #     pass
    # def click_element(self, *locator):
    #     pass
#     def click_element(self, *locator):
#         pass
#
#
# @wait
# def click_element(self,locator):
#     self.driver.find_element(*locator).click()
#
# @wait
# def enter_text(self, locator, *, value):
#     self.driver.find_element(*locator).clear()
#     self.driver.find_element(*locator).send_keys(value)


# @wait
# def select_item(self, locator, *, item):
#     element = self.driver.find_element(*locator)
#     s = Select(element)
#     if isinstance(item,str):
#         s.select_by_visible_text(item)
#     elif isinstance(item,int):
#         s.select_by_index(item)
#     else:
#         raise TypeError


# # # '''register'''
# s = Selenium_Wrapper(driver)
# s.click_element(("link text", "Register"))
# s.click_element(("id","gender-male"))
# s.enter_text(("id","FirstName"),value='kkkk')
# s.enter_text(("id","LastName"),value='fhfh')
# s.enter_text(("name","Email"),value='jhdhjhjhjh@gmail.com')
# s.enter_text(("name","Password"),value = '12324242')
# s.enter_text(("name","ConfirmPassword"),value='12324242')
# s.click_element(("id","register-button"))

















