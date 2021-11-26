from  selenium import webdriver
from selenium.webdriver.common.keys import  Keys

driver=webdriver.Chrome(executable_path="F:\pysel\chromedriver")

driver.get("https://chromedriver.chromium.org/downloads")

driver.implicitly_wait(500)
driver.close()
