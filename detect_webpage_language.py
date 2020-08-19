from langdetect import detect

from selenium import webdriver


def get_webpage_lang(body_text):
    # url = "http://jh-per.halal.ac.ir/"
    # print(el.text)

    try:
        if detect(body_text) == 'fa':
            print("the lang of this page is : ", detect(body_text))
            return True
    except Exception as exp:
        print("there was as problem : ", exp)
        return False


def is_persian(txt):
    try:
        if detect(txt) == 'fa':
            return True
        return False
    except Exception as exp:
        return False
