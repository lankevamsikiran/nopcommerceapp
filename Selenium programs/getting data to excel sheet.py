
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.headless=True

driver=webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("https://www.dibbs.bsm.dla.mil//awards/awddates.aspx?category=awddt")
driver.find_element_by_xpath("//*[@id='butAgree']").click()

a=driver.find_elements_by_xpath("//*[@id='ctl00_cph1_dtlDateList']/tbody/tr")



for i in range(1,len(a)):
    print(a[i].text)
    elements = driver.find_elements_by_xpath("//*[@id='ctl00_cph1_dtlDateList']/tbody/tr["+str(i+1)+"]/td")

    for j in range(1,len(elements)):
        pages=driver.find_element_by_xpath("//*[@id='ctl00_cph1_dtlDateList']/tbody/tr["+str(i+1)+"]/td["+str(j)+"]")
        pages.click()

        table=driver.find_elements_by_xpath("// *[ @ id = 'ctl00_cph1_grdAwardSearch'] / tbody / tr")
        print(len(table))
        driver.implicitly_wait(10)
        driver.back()
        #driver.get("https://www.dibbs.bsm.dla.mil//awards/awddates.aspx?category=awddt")



