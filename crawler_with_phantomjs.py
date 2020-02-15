from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.PhantomJS(
    executable_path="C:/Users/khavaninzadeh/Desktop/phantomjs-2.1.1-windows/bin/phantomjs.exe")

web_url = "http://www.ijgeophysics.ir/issue_12544_13525.html"

driver.get(web_url)
driver.maximize_window()
links_total = len(driver.find_elements_by_xpath("//a[contains(@onclick, 'loadIssues')]"))
print("all links in this web page = ", str(links_total))
i = 1
for plus in driver.find_elements_by_xpath(
        "//a[contains(@onclick, 'loadIssues')]"):  # browser.find_elements_by_class_name("dv_archive_vol"):
    try:
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick, 'loadIssues')]")))
        print("link number  ", i, "is found ")
        # print(plus)
        plus.click()
        print("plus number ", i, " is clicked   ", str(plus.click()))
        time.sleep(10)  # plus.find_element_by_tag_name("a").click()
        i += 1
    except Exception as exc:
        print("something went wrong ! in link number : ", i)
        print(exc)
        i += 1
# driver.implicitly_wait(time_to_wait=5)
