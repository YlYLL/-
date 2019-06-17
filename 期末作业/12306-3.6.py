import re
import time
import base64
import requests
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request



class Login(object):
    #初始化函数
    def __init__(self):
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.totalFlush = 0
        self.startTime = time.time()
        # self.driver = '' #驱动chrome浏览器进行操作
        driver = webdriver.Chrome()
        self.driver = driver #驱动chrome浏览器进行操作

    
    def login_input(self):
        self.driver.get(self.login_url)
        time.sleep(0.2)
        account = self.driver.find_element_by_class_name("login-hd-account")
        account.click()
        userName = self.driver.find_element_by_id("J-userName")
        userName.send_keys("13750988183")  # 12306账号
        password = self.driver.find_element_by_id("J-password")
        password.send_keys("mxl15258088950")  # 12306密码


    




if __name__ == '__main__':
    spider = Login()
    spider.login_input()
