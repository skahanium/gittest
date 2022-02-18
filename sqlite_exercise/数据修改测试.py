import sqlite3

path = 'grades.db'


def upd1(sid: int, inf: dict):
    con = sqlite3.connect(path)
    cur = con.cursor()

    sql = 'update 语文 set 姓名=?, 分数=?, 排名=? where 学号=?'
    data = (inf['姓名'], inf['分数'], inf['排名'], sid)
    cur.execute(sql, data)

    con.commit()
    cur.close()
    con.close()


def upd2(name: str, inf: dict):
    con = sqlite3.connect(path)
    cur = con.cursor()

    sql = 'update 语文 set 学号=?, 分数=?, 排名=? where 姓名=?'
    data = (inf['学号'], inf['分数'], inf['排名'], name)
    cur.execute(sql, data)

    con.commit()
    cur.close()
    con.close()


def update_data(*inf):
    if type(inf[0]) == int:
        upd1(inf[0], inf[1])
    elif type(inf[0]) == str:
        upd2(inf[0], inf[1])
    else:
        print('请按照规定输入信息')


update_data('成龙', {'学号': 21, '分数': 77, '排名': 2})
