from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--incognito')
# chrome_options.add_argument('--headless')
options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='./chromedriver.exe')

web_url = "http://www.ijgeophysics.ir/issue_12544_13525.html"

driver.get(web_url)
driver.maximize_window()
links_total = len(driver.find_elements_by_xpath("//a[contains(@onclick, 'loadIssues')]"))
print("all links in this web page = ", str(links_total))
i = 1
for plus in driver.find_elements_by_xpath(
        "//a[contains(@onclick, 'loadIssues')]"):  # browser.find_elements_by_class_name("dv_archive_vol"):
    try:
        if i == 1:
            print("link number  ", i, "is found ")
            print("plus number ", i, " is NOT clicked cause it is a minus !  ")
            i += 1
            time.sleep(5)
        else:
            print(' i = ', i)
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

soup = BeautifulSoup(driver.page_source, 'html.parser')

with open('Chr_out.txt', 'w', encoding='utf8') as out:
    for line in soup.prettify():
        out.write(line)
print("the page source is now in the file !")
print(soup.prettify())
# driver.implicitly_wait(time_to_wait=5)
