# 使用isinstance()来判断某个数据是否广义上的映射类型
from collections import abc

my_dict = {}
print(isinstance(my_dict, abc.Mapping))
