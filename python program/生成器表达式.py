symbols = 'k#*(dsfds#'
tuple_1 = list(ord(symbol) for symbol in symbols)  # 将生成器转化为了列表
tuple_2 = tuple(ord(symbol) for symbol in symbols)  # 将生成器转化为了元组
tuple_3 = (ord(symbol) for symbol in symbols)  # 生成器本身

print(tuple_1)
print(tuple_2)
print(tuple_3)

# 生成器表达式计算笛卡尔积
colors = ['black', 'white']
sizes = ['s', 'm', 'l']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
