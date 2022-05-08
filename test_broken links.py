from time import sleep

from requests import request
from selenium import webdriver
# request("GET",url=?)

driver = webdriver.Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
driver.get("file:///D:/selineium/demo-html/links.html")
sleep(2)
links = driver.find_elements_by_xpath("//a")
urls = [link.get_attribute("href") for link in links]

for item in urls[:15]:
    response = request("GET", url=item)
    if response.status_code == 200:
        print("got correct response")
    else:
        print(f"something went wrong :: {item}")

