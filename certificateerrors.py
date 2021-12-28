
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options

options=webdriver.ChromeOptions()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')

# prefs={"download.default_directory":"F:\pysel"}
# options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://aptransport.org/")
driver.find_element_by_xpath("//*[@id='rightbar']/ul/li[5]/a/span").click()

