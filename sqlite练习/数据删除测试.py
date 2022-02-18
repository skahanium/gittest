import sqlite3

path = '成绩.db'

def del1(sid: int):
    con = sqlite3.connect(path)
    cur = con.cursor()

    sql = 'delete from 语文 where 学号=?'
    学号 = (sid, )
    cur.execute(sql, 学号)

    con.commit()
    cur.close()
    con.close()


def del2(name: str):
    con = sqlite3.connect(path)
    cur = con.cursor()

    sql = 'delete from 语文 where 姓名=?'
    姓名 = (name, )
    cur.execute(sql, 姓名)
    con.commit()
    cur.close()
    con.close()


def delete_data(inf):
    if type(inf) == int:
        del1(inf)
    elif type(inf) == str:
        del2(inf)
    else:
        print('输入正确的数据类型')


def delete_all(infs: list):
    for inf in infs:
        delete_data(inf)


bad_students = ['冉正仕', '冉昊', '冉博']
delete_all(bad_students)