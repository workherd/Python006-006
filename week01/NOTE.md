

# 正则的使用

```python
常用组合：
.*  匹配任意字符出现任意多此，如.*@.* 匹配电子邮箱


import re
import re

content = "13231143991"
a = re.match(".{11}",content).group()
a1 = re.match(".{11}",content).span()
print(a)
print(a1)

a2 = re.match("@","123@123.com")
a3 = re.match(".*@.*","123@123.com")
print(a2)
print(a3)
a4 = re.match(".*@.*","123@123.com").group()
print(a4)

a5 = re.match("(.*)@(.*)","abc@123.com").group(2)
print(a5)

a6 = re.search("@",'abc@123.com')
print(a6)

a7 = re.findall("123","123@123.com")
print(a7)

a8 = re.sub("123","abc","123@123.com")
a9 = re.sub("\d","xyz","123@123.com")
a10 = re.sub("\d+","xyz","123@123.com")
# a11 = re.sub("\d.","xyz","123@123.com")
print(a8)
print(a9)
print(a10)
# print(a11)

a12 = re.split("@","123@123.com")
a13 = re.split("(@)","123@123.com")
print(a12)
print(a13)
```

# 时间操作的联系

```python

import time
from datetime import datetime,timedelta

a = time.time()
print('时间戳')
print(a)
print(time.localtime())
print('时间的格式化')
aa = time.strftime('%Y-%m-%d %X',time.localtime())
print(aa)
print('字符转换为时间对象')
print(time.strptime('2020-12-22 16:43:01','%Y-%m-%d %X'))

print('*'*11,'datatime 时间偏移的处理','*'*11)
print('now()')
print(datetime.now())
print('today()')
print(datetime.today())
print('时间偏移')
print("day+1")
print(datetime.today() - timedelta(days=1))
print(datetime.today() + timedelta(days=-1))

```

