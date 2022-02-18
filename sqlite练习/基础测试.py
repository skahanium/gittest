import sqlite3

# 获取与数据库的连接
path = '成绩.db'
conn = sqlite3.connect(path)

# 编写sql语句
sql = 'select * from 语文'

# 执行sql语句
cur = conn.cursor()
cur.execute(sql)

# 打印结果
print(cur.fetchall())

# 关闭连接
cur.close()
conn.close()
