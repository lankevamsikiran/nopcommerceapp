
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.headless=True

driver=webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("https://www.dibbs.bsm.dla.mil//awards/awddates.aspx?category=awddt")
driver.find_element_by_xpath("//*[@id='butAgree']").click()

a=driver.find_elements_by_xpath("//*[@id='ctl00_cph1_dtlDateList']/tbody/tr")


#elements=driver.find_element_by_xpath("//*[@id='ctl00_cph1_dtlDateList']/tbody/tr[2]/td")

print(len(a))

