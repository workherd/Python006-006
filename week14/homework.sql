作业要求：请将以下的 SQL 语句翻译成 pandas 语句：
1. SELECT * FROM data;
print(df)

2. SELECT * FROM data LIMIT 10;
print(df.head(10))

3. SELECT id FROM data;  //id 是 data 表的特定一列
print(df['id'])

4. SELECT COUNT(id) FROM data;
print(df['id'].count())

5. SELECT * FROM data WHERE id<1000 AND age>30;
print(df[(df['id']<1000) & (df['age']>30)])

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(df.groupby('id').agg({'order_id': pd.Series.nunique}))

7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(table1, table2, on='id', how='inner'))

8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.merge(table1, table2, how='outer'))

9. DELETE FROM table1 WHERE id=10;
print(df.drop(df[df['id']==10].index, axis=0))

10. ALTER TABLE table1 DROP COLUMN column_name;
print(df.drop(['column_name'], axis=1))

11. select a.sex, a.tip
from tips_tb a
where (
	select count(*)
	from tips_tb b
	where b.sex = a.sex and b.tip > a.tip
) < 2
order by a.sex, a.tip desc;

# 1.
df.assign(rn=df.sort_values(['total_bill'], ascending=False)
          .groupby('sex')
          .cumcount()+1)\
    .query('rn < 3')\
    .sort_values(['sex', 'rn'])

# 2.
df.assign(rn=df.groupby('sex')['total_bill']
          .rank(method='first', ascending=False)) \
    .query('rn < 3') \
    .sort_values(['sex', 'rn'])

12.