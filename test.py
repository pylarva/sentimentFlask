# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

conn = pymysql.connect(host='192.168.2.10', port=3306, user='root', passwd='root', db='flask02')

# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.3'")
effect_row = cursor.execute("show tables")
# print(effect_row)

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# 执行SQL，并返回受影响行数
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])

# 提交，不然无法保存新建或者修改的数据
# conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()