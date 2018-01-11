# coding=utf-8  
import time  
from selenium import webdriver  
  
  
driver = webdriver.Chrome()  
driver.implicitly_wait(6)  
driver.get("https://www.baidu.com")  
time.sleep(1)  
  
for link in driver.find_elements_by_xpath("//*[@href]"):  
    print (link.get_attribute('href'))  
driver.quit()
