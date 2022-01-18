#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 15:09:59 2022

@author: skahanium
"""
import scipy.stats as stats
import numpy as np
from collections import Counter

#%% 算数平均值
x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x2 = x1 + [12]

print('x1的算数平均值为：', np.mean(x1))
print('x2的算数平均值为：', np.mean(x2))

#%% 中位数
print('x1的中位数为：', np.median(x1))
print('x2的中位数为：', np.median(x2))

#%% 众数
x3 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 8, 8, 8]

def mode(obj):
    obj = Counter(obj)
    max_time = np.array(list(obj.values())).max()
    result = []
    for k, v in obj.items():
        if v == max_time:
            result.append(k)
    return result

print('x3的众数为：', mode(x3))

#%% 几何平均值（样本数据非负）

print('x1的几何平均值为：', stats.gmean(x1))
print('x2的几何平均值为：', stats.gmean(x2))

#%% 调和平均值

print('x1的调和平均值为：', stats.hmean(x1))
print('x2的调和平均值为：', stats.hmean(x2))
