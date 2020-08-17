from langdetect import detect

from selenium import webdriver


def get_webpage_lang(url):
    driver = webdriver.PhantomJS(
        executable_path="C:/Users/khavaninzadeh/Desktop/phantomjs-2.1.1-windows/bin/phantomjs.exe")

    # url = "http://jh-per.halal.ac.ir/"
    driver.get(url)
    el = driver.find_element_by_tag_name('body')
    # print(el.text)
    print("the lang of this page is : ", detect(el.text))
    if detect(el.text) == 'fa':
        return True
    return False
