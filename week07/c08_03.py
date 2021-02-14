#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 11:02
# @Author     : john
# @File       : c08_03.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world!</h1>'


if __name__ == '__main__':
    app.run(debug=True)

# 注册
@route('index', method = ['GET', 'POST'])
def static_html():
    return render_template('index.html')

# 等效于
static_html = route('index', method=['GET', 'POST'])(static_html)()


def route(rule, **options):
    def decorator(f):
        endpoint = options.pop("endpoint", None)
        # 使用类似字典结构，以index为key，以method staict_html 其他参数为value存储绑定关系s
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorator


