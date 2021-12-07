# from selenium import webdriver

#from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import requests
#
#driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://github.com/naveens33/python_tutorials")
#
# links=driver.find_elements(By.TAG_NAME,"a")
# #print(len(links))
# #print(links)
# #
# for link in links:
#     print(link)
#     l=requests.get(link)
#     if l.status_code==200:
#         print("working fine: ", link.text)
#
# driver.quit()
#


import requests
import urllib3
import pytest
from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# capabilities = {
#     "build": "[Python] Finding broken links on a webpage using Selenium",
#     "name": "[Python] Finding broken links on a webpage using Selenium",
#     "platform": "Windows 10",
#     "browserName": "Chrome",
#     "version": "85.0"
# }
#
# user_name = "user-name"
# app_key = "access-key"
broken_links = 0
valid_links = 0

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument('disable-infobars')
# driver=webdriver.Chrome(options=options)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#remote_url = "http://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"
#driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=capabilities)

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
#driver.get('https://www.lambdatest.com/blog/')
driver.get("https://github.com/naveens33/python_tutorials")
# links = driver.find_elements_by_css_selector("a")
links = driver.find_elements(By.CSS_SELECTOR, "a")

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '88.0',
 'os': 'Windows',
 'os_version': '10',
 'name': 'BStack-[Python] Sample Test', # test name
 'build': 'BStack Build Number 1' # CI/CD job or build name
}
driver = webdriver.Remote(
    command_executor='https://vamsikiran_le5ojK:y9cPyrj95jj9jfkJknxS@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)


for link in links:
    try:
        request = requests.head(link.get_attribute('href'), data={'key': 'value'})
        print("Status of " + link.get_attribute('href') + " is " + str(request.status_code))
        if (request.status_code == 404):
            broken_links = (broken_links + 1)
        else:
            valid_links = (valid_links + 1)
    except requests.exceptions.MissingSchema:
        print("Encountered MissingSchema Exception")
    except requests.exceptions.InvalidSchema:
        print("Encountered InvalidSchema Exception")
    except:
        print("Encountered Some other execption")

print("Detection of broken links completed with " + str(broken_links) + " broken links and " + str(
    valid_links) + " valid links")

driver.quit()