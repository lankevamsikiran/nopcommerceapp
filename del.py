
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
options=webdriver.ChromeOptions()
prefs={"download.default_directory":"F:\pysel"}
options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm")
driver.find_element_by_xpath("//*[@id='searchterm']").send_keys("211188")
driver.find_element_by_xpath("//*[@id='DrugNameform']/div[2]/button[1]").click()
driver.find_element_by_xpath("//*[@id='exampleProd_wrapper']/div[1]/a[1]/span").click()
time.sleep(10)
driver.quit()
