
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="F:\pysel\chromedriver")
driver.get("https://www.facebook.com/")
links=driver.find_elements(By.TAG_NAME, "a")

print(len(links))
#
# for link in links:
#     print(link.text)
#
driver.find_element(By.LINK_TEXT, "Create New Account").click()
assert driver.title=="Facebook – log in or sign up"
print("succes")

driver.save_screenshot("F:/pycharm practice/nopcommerceApp/screenshots/fb.png")

driver.close()