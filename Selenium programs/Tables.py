
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demo.guru99.com/test/web-table-element.php")


rows=len(driver.find_elements_by_xpath("//*[@id='leftcontainer']/table/tbody/tr"))
cols=len(driver.find_elements_by_xpath("//*[@id='leftcontainer']/table/tbody/tr[1]/td"))

print(rows)
print(cols)

for r in range(2,rows+1):
    for c in range(1,cols+1):
        value=driver.find_element_by_xpath("//*[@id='leftcontainer']/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end="      ")

    print()


driver.quit()
