from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome(executable_path='./chromedriver.exe')

web_url = "http://www.ijgeophysics.ir/issue_12544_13525.html"

driver.get(web_url)
driver.maximize_window()
links_total = len(driver.find_elements_by_xpath("//a[contains(@onclick, 'loadIssues')]"))
print("all links in this web page = ", str(links_total))
i = 1
for plus in driver.find_elements_by_xpath(
        "//a[contains(@onclick, 'loadIssues')]"):  # browser.find_elements_by_class_name("dv_archive_vol"):

    print("link found ")
    print(plus)
    plus.click()
    time.sleep(10)# plus.find_element_by_tag_name("a").click()
# driver.implicitly_wait(time_to_wait=5)
