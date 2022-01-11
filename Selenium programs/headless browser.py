
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless=True
driver=webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


driver.get("https://www.facebook.com/")

driver.find_element_by_xpath("//button[@name='login']").click()
driver.save_screenshot("Head.png")

print(driver.title)
driver.close()
