import sqlite3

def insert(new_data: dict):
    con = sqlite3.connect('grades.db')
    cur = con.cursor()

    sql = 'insert into 语文 (学号, 姓名, 分数, 排名)' \
        'values(?, ?, ?, ?)'
    data = (new_data['学号'], new_data['姓名'], new_data['分数'], new_data['排名'])
    try:
        cur.execute(sql, data)
    except sqlite3.IntegrityError:
        print('学生信息已存在，不要重复插入！！！')

    con.commit()
    cur.close()
    con.close()


# def insert_all(all_data: list):
#     for i in all_data:
#         insert(i)


def insert_all(all_data: list):
    con = sqlite3.connect('grades.db')
    cur = con.cursor()

    sql = 'insert into 语文 (学号, 姓名, 分数, 排名)' \
        'values(?, ?, ?, ?)'
    data_list = []
    for data in all_data:
        data_list.append(tuple(data.values()))
    try:
        cur.executemany(sql, data_list)
    except sqlite3.IntegrityError:
        print('学生信息已存在，不要重复插入！！！')
    con.commit()
    cur.close()
    con.close()
    return cur.rowcount


order1 = {'学号':16, '姓名':'冉正仕', '分数':19, '排名':25}
order2 = {'学号':18, '姓名':'冉昊', '分数':21, '排名':20}
order3 = {'学号':14, '姓名':'冉博', '分数':15, '排名':26}


orders = [order1, order2, order3]
insert_all(orders)


