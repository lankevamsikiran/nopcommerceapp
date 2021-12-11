
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

#
# driver=webdriver.Chrome(executable_path="F:\pysel\chromedriver")

driver=webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.facebook.com/")

driver.find_element_by_xpath("//button[@name='login']").click()

print(driver.title)
driver.close()

