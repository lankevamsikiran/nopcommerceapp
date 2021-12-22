


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://datatables.net/")



rows=len(driver.find_elements_by_xpath("//*[@id='example']/tbody/tr"))
cols=len(driver.find_elements_by_xpath("//*[@id='example']/tbody/tr[1]/td"))

print(rows)
print(cols)

def allitems():
    rows = len(driver.find_elements_by_xpath("//*[@id='example']/tbody/tr"))
    cols = len(driver.find_elements_by_xpath("//*[@id='example']/tbody/tr[1]/td"))

    for r in range(2, rows + 1):
        for c in range(1, cols + 1):
            value = driver.find_element_by_xpath("//*[@id='example']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
            print(value, end="      ")

        print()





elements=len(driver.find_elements_by_xpath("//*[@id='example_paginate']/span/a"))
print(elements)

for i in range(1,elements+1):
    allitems()
    driver.find_element_by_xpath("//*[@id='example_next']").click()

x=driver.find_element_by_xpath("//*[@id='example_next']").is_enabled()


driver.quit()

