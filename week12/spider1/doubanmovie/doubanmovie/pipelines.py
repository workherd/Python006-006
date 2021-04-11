# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanmoviePipeline:  # 注册到settings.py文件的item）piplines中激活组件
    # def process_item(self, item, spider):
    #     return item

    # 每一个item管道都调用该方法，必须返回一个item对象或raise dropitem异常
    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        # content = item['content']
        output = f'|{title}|\t|{link}|\n\n'
        # output = f'|{title}|\t|{link}|\t|{content}|\n\n'
        with open('./doubanmovie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item