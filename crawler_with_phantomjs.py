from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib import request

import time
import requests
from twisted.test.test_sslverify import ctx

driver = webdriver.PhantomJS(
    executable_path="C:/Users/khavaninzadeh/Desktop/phantomjs-2.1.1-windows/bin/phantomjs.exe")

web_url = "http://www.ijgeophysics.ir/"

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
            time.sleep(5)  # plus.find_element_by_tag_name("a").click()
            i += 1
    except Exception as exc:
        print("something went wrong ! in link number : ", i)
        print(exc)
        i += 1

soup = BeautifulSoup(driver.page_source, 'html.parser')
# with open('PhJs_out.txt', 'w', encoding='utf8') as out:
#     for line in soup.prettify():
#         out.write(line)
# print("the page source is now in the file !")
# print(soup)
# driver.implicitly_wait(time_to_wait=5)

c = 0
link_len = len(soup.findAll('div', {"class": "issue_dv"}))

for ana in soup.findAll('div', {"class": "issue_dv"}):
    print(ana)
    c = c + 1
    links = ana.findAll("a", href=True)

print("all issues count =  ", c)
print("web url is ... ", web_url)
issue_link = links[0].get('href')
print("issue link is ... ", issue_link)

correct_url = urljoin(web_url, issue_link)
print(correct_url)

# w = Get_xml(correct_url, '1_1', './journals')
# print("going to save the xml file ...")
#
# w.save_xml(correct_url, '1_1.xml', './journals')

name = ""
path_to_save = "./All_sinawebs/"
name = "Sweb_Volume_"
final_save_loc = ""
parse_object = urlparse(web_url)
base_url = "http://" + parse_object.netloc
soup2 = BeautifulSoup(request.urlopen(correct_url), 'html.parser')
issue_xml_objects = soup2.findAll("a", attrs={"title": "XML"}, href=True)
# href = issue_xml_objects[0].get('href')
# get_xml_url = urljoin(base_url, href)
# print(get_xml_url)
# req = requests.get(get_xml_url, allow_redirects=True)  # idk what is context !!!!!! it imported a package to use it
# open('./journals/1_1.xml', 'wb').write(req.content)
volume_number = 0
issue_number = 1
for link in links:
    time.sleep(10)
    volume_number += 1
    issue_number = 1
    print("Going to main page with link = ", link)
    for issue_xml_link in issue_xml_objects:
        time.sleep(5)
        print("going to download xml file with link = ", issue_link)
        href = issue_xml_link.get('href')
        get_xml_url = urljoin(base_url, href)
        print("Going to link => ", get_xml_url)

        # name += str(list.index(links, link, 0, -1) + 1) + "_" + str(
        #     list.index(issue_xml_objects, issue_xml_link, 0, -1)) + ".xml"

        name = name + str(volume_number) + "_" + "Issue_" + str(issue_number) + ".xml"

        print("the name of the xml file would be ", name)
        req = requests.get(get_xml_url, allow_redirects=True)
        print("request is sent ...")
        path_to_save.join(name)
        with open(path_to_save, 'wb') as download_loc:
            download_loc.write(req.content)
        print("File ", name, " is saved !", "\n ______________________________________________________________")
        issue_number += 1
    print("the volume number ", str(volume_number), " is completely downloaded !",
          "\n ************************************************************************************")
