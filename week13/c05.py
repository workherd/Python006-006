#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 15:49
# @Author     : john
# @File       : c05.py

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome dirver 和浏览器的版本要保持一致
    #https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/#
    # 将现在的程序放置在python解析相同的文件夹中

    browser.get('https://www.douban.com')
    time.sleep(1)

    # browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[0])
    btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    # /html/body/div[1]/div[1]/ul[1]/li[2]
    btm1.click()

    browser.find_element_by_xpath('//*[@id="username"]').send_keys('1330430077@qq.com')
    browser.find_element_by_id('password').send_keys('test123@douban')
    time.sleep(1)
    browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)

finally:
    browser.close()





