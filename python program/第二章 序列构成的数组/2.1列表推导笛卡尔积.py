# 笛卡儿积是一个列表，列表里的元素是由输入的可迭代类型的元素对构成的元组，因此笛卡儿积列表的长度等于输入变量长度的乘积

colors = ['black', 'white']
sizes = ['s', 'm', 'l']

tshirt = [(color, size) for color in colors for size in sizes]
print(tshirt)

for color in colors:
    for size in sizes:
        print(color, size)
