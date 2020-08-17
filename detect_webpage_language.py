from langdetect import detect

from selenium import webdriver


def get_webpage_lang(body_text):

    # url = "http://jh-per.halal.ac.ir/"
    # print(el.text)
    print("the lang of this page is : ", detect(body_text))
    if detect(body_text) == 'fa':
        return True
    return False
