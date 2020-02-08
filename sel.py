from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get('http://jha.iums.ac.ir/')
# driver.implicitly_wait(20)
driver.maximize_window()
# driver.find_element_by_link_text('آرشیو مجله و مقالات').click()
menu = driver.find_element_by_link_text('آرشیو مجله و مقالات')
ActionChains(driver).move_to_element(menu).perform()
driver.find_element_by_link_text('کلیه شماره‌های مجله').click()



