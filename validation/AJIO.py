
from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
driver = Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
driver.get("https://www.ajio.com/s/men-winterwear-4137-78751")
ele_jacket = driver.find_elements_by_xpath("//div[@class='nameCls']")
ele_expected_price =driver.find_elements_by_xpath("//span[@class='price  ']")

jacket_names=[i.text for i in ele_jacket]
jacket_price = [i.text for i in ele_expected_price]

prices = []
import re
for price in jacket_price:
    res = re.findall(r'\d',price)
    prices.append(int("".join(res)))
print(prices)

pair = []
for _jacket,_price in zip(jacket_names,prices):
    pair.append({'name':_jacket,'price':_price})
print(pair[:])

# max = sorted(pair, key=lambda item:item['price'])[-1]
# min = sorted(pair, key=lambda item:item['price'])[0]
# print(max)
# print(min)

# between_1000_2000 =[i for i in pair if i['price']>1000 and i['price']<2000]
# print(between_1000_2000)









