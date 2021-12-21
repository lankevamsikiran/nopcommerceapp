
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver=webdriver.Chrome(ChromeDriverManager().install())
#
# from webdriver_manager.firefox import GeckoDriverManager
# driver=webdriver.Firefox(GeckoDriverManager().install())

from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver=webdriver.Edge(EdgeChromiumDriverManager().install())




driver.maximize_window()
driver.get("https://www.google.com/")
