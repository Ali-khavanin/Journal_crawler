from bs4 import BeautifulSoup
from urllib2 import urlopen as uReq
from selenium import webdriver
from urllib import quote
import time
from urlparse import urlparse
from urlparse import  urljoin
from get_xml import Get_xml
import os
import errno
from selenium.webdriver.common.by import By

class Sina_Web(Get_xml):
    def __init__(self):
        pass

    def crawl_sinaweb(self,url,filename,save_dir):
        
        if not os.path.exists(save_dir):
            try:
                os.makedirs(save_dir)
                print "Directory " + save_dir + " is created."
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        
        executable_path = 'C:\\Users\\Sabzalian\\Desktop\\software\\phantom\\phantomjs-2.1.1-windows\\bin\\phantomjs'
        #driver = webdriver.Chrome(executable_path=r"C:\Users\Sabzalian\Desktop\software\chromdriver\chromedriver.exe")
        """ webdriver.PhantomJS(executable_path=executable_path,
                    desired_capabilities=dict(webdriver.DesiredCapabilities.PHANTOMJS),
                    service_args=['--web-security=no', '--ssl-protocol=any', '--ignore-ssl-errors=yes']) """  
        browser =  webdriver.PhantomJS(executable_path=executable_path, service_args=['--ignore-ssl-errors=true', '--ssl-certificates-path=C:\Users\Sabzalian\Documents\papers_list\my_trust_store.pem']) #webdriver.PhantomJS(executable_path=executable_path)
        browser.get(url)
        # called Ajax
        message = "Waiting for Ajax links ..."
        print message
        links_total = len(browser.find_elements_by_xpath("//a[contains(@onclick, 'loadIssues')]"))
        print str(links_total)
        for plus in browser.find_elements_by_xpath("//a[contains(@onclick, 'loadIssues')]"): # browser.find_elements_by_class_name("dv_archive_vol"):
            
            plus.click()  #plus.find_element_by_tag_name("a").click()
            time.sleep(4)
            
        soup = BeautifulSoup(browser.page_source,'html.parser')
        c = 0
        link_len = len(soup.findAll('div', {"class" : "issue_dv"}))

        for ana in soup.findAll('div', {"class" : "issue_dv"}):
            c = c+1
            link = ana.findAll("a",href=True)

            #
            print(c)
            #fullurl = quote(link[0].get('href'), safe="%/:=&?~#+!$,;'@()*[]")
            correct_url = urljoin(url,link[0].get('href'))
            #print correct_url
            #links = links.append(link[0].get('href'))

            fname = filename+ "{:02d}".format(c) + ".xml"
            print "All Link number = " + str(link_len) + "          ####################"
            w = Get_xml(correct_url,fname,save_dir)
            w.save_xml(correct_url,fname,save_dir)
            #s = getxml.save_dir(url,filename,save_dir)
            #print("Save File: " + fname +" is Done")




""" url = 'http://gps.gu.ac.ir/'
executable_path = 'C:\\Users\\Sabzalian\\Desktop\\software\\phantom\\phantomjs-2.1.1-windows\\bin\\phantomjs'
#driver = webdriver.Chrome(executable_path=r"C:\Users\Sabzalian\Desktop\software\chromdriver\chromedriver.exe")
browser = webdriver.PhantomJS(executable_path=executable_path)
 
browser.get(url)

for plus in browser.find_elements_by_class_name("dv_archive_vol"):
    plus.find_element_by_tag_name("a").click()
    time.sleep(2)

soup = BeautifulSoup(browser.page_source,'html.parser')
c = 0
for ana in soup.findAll('div', {"class" : "issue_dv"}):
    c = c+1
    link = ana.findAll("a",href=True)
    print(c)
    print(link) """

