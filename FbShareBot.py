from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time

username=' ur Fb username'
password='Ur Fb password'
url="https://www.facebook.com/"
driver=webdriver.Chrome("C:/Users/HAFEEZ P P/Documents/NewProject/Downloads/chromedriver.exe")
driver.get(url)
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()
time.sleep(5)
driver.find_element_by_xpath("//textarea[@name='xhpc_message']").send_keys('PYthon Bot is typing....')
time.sleep(5)
buttons = driver.find_elements_by_tag_name('button')
for button in buttons:
    if button.text=='Share':
        button.click()


print('share clicked..')
driver.close()

