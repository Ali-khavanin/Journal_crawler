from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
url = "http://www.ijgeophysics.ir/"

driver.get(url)
driver.maximize_window()

all_links = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[1]/a[1]')

all_links.click()
