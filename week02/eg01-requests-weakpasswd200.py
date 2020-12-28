#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
from time import sleep

# 定义函数
def get_url_name(myurl):

    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    header = {'user-agent': ua}
    reponse = requests.get(myurl, headers=header)
    print(reponse.status_code)
    # print(reponse.text)
    selector = etree.HTML(reponse.text)
    # weak_passwd
    # weak_pwds = selector.xpath('//div[@class="TopWorstPsw__table-row data inline-block md:flex"]/div/div[2]/div')
    weak_pwds = selector.xpath('//*[@id="Top worst passwords table"]/section/div/div[2]/div[2]/div/div[2]/div')


    print(weak_pwds)
    # for i in weak_passswds:
    #     print(f'电影名称：{i} \t \t 电影链接：{film_info[i]}')


if __name__ == '__main__':
    # 生成包含所有页面的元组
    urls = 'https://nordpass.com/most-common-passwords-list/'
    print(urls)
    get_url_name(urls)
    sleep(1)
    print('end')
