l = list(range(10))
l[2:5] = [20, 40] # 对列表第2、3、4个元素赋值，此时切片长度和赋值列表长度不一致也是可以的
print(l)

l[3::2] = [11, 12, 13] # 从列表第3个元素开始，每隔一个元素进行替换，此时切片长度和替换列表长度必须一致
print(l)