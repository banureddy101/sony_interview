import webbrowser
from webbrowser import Chrome

import driver
from selenium import webdriver
from time import sleep


# driver = webdriver.Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://www.ajio.com/s/men-winterwear-4137-78751")
# sleep(2)
# ele_shoesnames = driver.find_elements_by_xpath("//div[@class='nameCls']")
# ele_shoesprice = driver.find_elements_by_xpath("//span[@class='price  ']")
# shoe_names = [i.text for i in ele_shoesnames]
# shoe_price = [i.text for i in ele_shoesprice]
#
# prices = []
# import re
# for i in shoe_price:
#     res = re.findall(r'\d',i)
#     prices.append(int("".join(res)))
# print(prices)
#
# pair = []
# for shoes_,price_ in zip(shoe_names,prices):
#     pair.append({'shoe':shoes_,'price':price_})
# print(pair[:2])
#
# max_price = sorted(pair,key=lambda item:item['price'])[-1]
# print(max_price)


# driver = webbrowser.Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
# # driver.maximize_window()
# driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
# driver.implicitly_wait(30)
# driver.find_element_by_id('resumeUpload').send_keys(r'C:\Users\pc\PycharmProjects\_selenium\BANUPRATHAP PV resume Mtech.txt.doc')
# sleep(2)



