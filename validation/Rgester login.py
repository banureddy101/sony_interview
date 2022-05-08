from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com")
driver.find_element_by_xpath("//a[text()='Register']").click()
sleep(2)
driver.find_element_by_id("gender-male").click()
driver.find_element_by_id("FirstName").send_keys("nkn")
driver.find_element_by_id("LastName").send_keys("hhb")
driver.find_element_by_id("Email").send_keys("jjjj@gmail.com")
driver.find_element_by_id("Password").send_keys("fffffff")
driver.find_element_by_id("ConfirmPassword").send_keys("fffffff")
driver.find_element_by_id("register-button").click()


'''absulute path'''
# driver.get("file:///D:/selineium/demo-html/xpath.html")
# driver.find_element_by_xpath("/html/body/div[1]/input[1]").send_keys('banu')

# driver =webdriver.Chrome(r"C:\Users\pc\PycharmProjects\_selenium\chromedriver.exe")
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



