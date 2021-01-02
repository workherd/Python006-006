#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import re
#
# str1 = ' </a> 华为在 1 月 1 日凌晨发布公告宣布下架腾讯手游。腾讯按市值是世界最大的游戏公司。华为给出的理由是“腾讯游戏于 2020 年 12 月 31 日 17 点 57 分单方面就双方合作做出重大变更，导致双方的继续合作产生重大障碍。经过我司法务的谨慎评估，我们不得不依照腾讯单方面要求暂停相关合作，将腾讯游戏从华为平台下架。对此我们深表遗憾。”业内人士称<a href="https://news.stcn.com/sd/202101/t20210101_2693963.html">腾讯与华为之间的分歧是平台抽成比例</a>。苹果和 Google 应用商店的抽成比例是 30%，这一比例被认为过高而引发了很多争议，Epic Games 为此与苹果在打官司。但与中国的平台相比，30% 已经是很低了。国产 Android 机官方应用商店一直跟游戏厂商 5:5 分成，这还是在扣除支付通道费之后算的，所以游戏厂商实际只能拿到不足 50% 的分成。也就是说，开发商辛辛苦苦做一个游戏，大部分的收入都会被渠道赚走。   '
# print(f'str1:{str1}')
# str2 = re.sub("<a href=.*\">", '', str1)
# str3 = re.sub("\S</a>", '', str2)
# print(f'str3:{str3}')
# str3 = ""
# for i in t:
#     str3 += i
#
# print(f'str1:{str3}')


import re

htmlString = '''<ul id="TopNav"><li><a href="/EditPosts.aspx" id="TabPosts">随笔</a></li>
        <li><a href="/EditArticles.aspx" id="TabArticles">文章</a></li>
        <li><a href="/EditDiary.aspx" id="TabDiary">日记</a></li>
        <li><a href="/Feedback.aspx" id="TabFeedback">评论</a></li>
        <li><a href="/EditLinks.aspx" id="TabLinks">链接</a></li>
        <li id="GalleryTab"><a href="/EditGalleries.aspx" id="TabGalleries">相册</a></li>
        <li id="FilesTab"><a href="Files.aspx" id="TabFiles">文件</a></li>
        <li><a href="/Configure.aspx" id="TabConfigure">设置</a></li>
        <li><a href="/Preferences.aspx" id="TabPreferences">选项</a></li></ul>'''

# 方法 1
pre = re.compile('>(.*?)<')
s1 = ''.join(pre.findall(htmlString))
print(s1)  # '随笔文章日记评论链接相册文件设置选项'
# 方法2
s2 = re.sub(r'<.*?>','',htmlString)
print(s2)
s2 = s2.replace('\n','')
print(s2)