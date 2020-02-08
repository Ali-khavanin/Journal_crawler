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
driver.find_element_by_xpath('//*[@id="top_box_b"]/div[2]/div[2]/div[2]/a[3]').click()
options = webdriver.ChromeOptions()

# options.add_argument("--headless")
# options.add_argument("--window-size=1920x1080")
# options.add_argument("--disable-notifications")
# options.add_argument('--no-sandbox')
# options.add_argument('--verbose')
#
# options.add_experimental_option("prefs", {
#         "download.default_directory": "./journals",
#         "download.prompt_for_download": False,
#         "download.directory_upgrade": True,
#         "safebrowsing_for_trusted_sources_enabled": False,
#         "safebrowsing.enabled": False
# })


print("starting to download the xml file !")
driver.find_element_by_xpath('//*[@id="top_box_b"]/div[2]/div[2]/a[2]').click()
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="top_box_b"]/div[2]/div/div[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/a').click()
driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="top_box_b"]/div[2]/div/div[3]/table/tbody/tr[3]/td/div/p[1]/a').click()
driver.implicitly_wait(15)

print("the xml file downloaded !")
driver.__exit__()
