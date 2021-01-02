#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from pathlib import *
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

"""
https://www.zhihu.com/api/v4/questions/26551475/root_comments?limit=10&offset=30&order=normal&status=open
使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容 (如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件。
https://www.zhihu.com/question/421150601
referer: https://www.zhihu.com/question/421150601
method:post
用户：//div[@class="List-item"]//a[@class="UserLink-link"]/text()
答案://div[@class="List-item"]//div[@class="RichContent-inner"]/span[1]/p/text()
答案的规则： span 标签  类class  =  "RichText ztext CopyrightRichText-richText"
"""

# starter

if __name__ == '__main__':
    driver = webdriver.Chrome()  # 打开浏览器

    driver.get("https://www.zhihu.com/question/421150601")
    time.sleep(5)
    action1 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/button")
    ActionChains(driver).move_to_element(action1).click(action1).perform()

    # driver.find_element_by_id("su").click()
    # 模拟用户操作
    def execute_times(times):

        for i in range(times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            # try:
            #     driver.find_element_by_css_selector('button.QuestionMainAction').click()
            #     print("page" + str(i))
            #     time.sleep(1)
            # except Exception as e:
            #     print(e)
            #     break

    execute_times(10)

    result_raw = driver.page_source
    with open('zhihu_yuanshi.html','w',encoding='utf-8') as f:
        f.write(result_raw)
    # print(result_raw)