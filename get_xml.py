from bs4 import BeautifulSoup

from urllib.request import urlopen as uReq
from urllib.request import urlopen
import urllib.request
from selenium import webdriver
from urllib.parse import urlparse
from urllib.parse import urljoin
import time
import re
import requests
import io
import os
import ssl


class Get_xml(object):

    def __init__(self, url, filename, save_dir):
        self.url = url
        self.filename = filename
        self.save_dir = save_dir

    def save_xml(self, url, filename, save_dir):
        # grabs the page
        parse_object = urlparse(url)
        base_url = "http://" + parse_object.netloc
        # print base_url

        soup = self.retrying_request(5, url)
        xml_obj = soup.findAll("a", attrs={"title": "XML"}, href=True)
        # print xml_obj[0].get('href')
        href = xml_obj[0].get('href')
        correct_url = urljoin(base_url, href)
        # print correct_url

        url = correct_url

        """ r = requests.get(url)
        r.encoding = r.apparent_encoding  """

        # encodedText = self.encode_xml(r.text) #r.text.encode("utf-8")
        # print encodedText

        """ ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE """
        # context = ssl._create_unverified_context()

        ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        # uReq("https://your-test-server.local", context=ctx)

        if not os.path.exists(os.path.join(save_dir, filename)):
            print("XML Request is sending ... ")
            time.sleep(1)
            get = uReq(url, context=ctx)
            html = get.read()
            soup = BeautifulSoup(html, features="lxml")
            encodedText = soup.encode("utf-8")
            print("Saving File: " + filename + "  ...")
            with open(os.path.join(save_dir, filename), 'w') as file:
                file.write(encodedText)
                file.close()
            print("writing xml file is Done: " + filename)
        else:
            print("xml file does  exist: " + filename)

    def encode_xml(self, string, encoding='utf-8'):
        string = string.encode(encoding)
        # string = string.encode('cp1252').decode('cp1256')
        """ string = string.replace( '&', '&amp;')
        string = string.replace( '<', '&lt;')
        string = string.replace( '>', '&gt;')
        string = string.replace('\\', '&quot;') """
        return string

    def retrying_request(self, retries, url):
        # eventlet.monkey_patch()
        for i in range(retries):
            try:
                print("Retry number " + str(i))
                time.sleep(2)
                client = uReq(url, v)
                soup = BeautifulSoup(client.read(), 'html.parser')  # using the default html parser
                # r.raise_for_status()
                return soup
            except requests.exceptions.HTTPError as errh:
                print("Http Error:", errh)
                continue
            except requests.exceptions.ConnectionError as errc:
                print("Error Connecting:", errc)
                continue
            except requests.exceptions.Timeout as errt:
                print("Timeout Error:", errt)
                continue
            except requests.exceptions.RequestException as err:
                print("OOps: Something Else", err)
                continue
