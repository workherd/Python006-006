#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 23:34
# @Author     : john
# @File       : test.py
import pandas as pd

import pandas as pd
df = pd.DataFrame({"id": [500, 500, 10, 24],
                   "order_id": [4, 2, 4, 2],
                   "age": [40, 22, 88, 55],
                   "D": [20, 4, 2, None]
                   })
print(df)
print('='*88)
# sort_values(by=['A'], ascending=True)
# print(df[['id','order_id']].sort_values(by='id', ascending=True))
# print(df.drop_duplicates(subset=['order_id'], keep='first', inplace=True))
print(df.groupby('id').agg({'order_id': pd.Series.nunique}))
print('='*88)

'6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;'