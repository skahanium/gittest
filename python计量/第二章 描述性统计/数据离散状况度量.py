#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 16:41:18 2022

@author: skahanium
"""

import numpy as np
np.random.seed(125)

X = np.random.randint(100, size=20)
X = np.sort(X)
print('x：%s' %(X))
mu = X.mean()
print('x的平均值：', mu)
#%% 区间长度
print("Range of x：%s" %(np.ptp(X))) # 注：ptp()函数是计算最大最小值差值的函数，即Peak to Peak

#%% 平均绝对偏差(MAD)
abs_dispersion = [np.abs(mu-x) for x in X]
MAD = np.sum(abs_dispersion) / len(abs_dispersion)
print('X的平均绝对偏差为：', MAD)

#%% 方差、标准差
print(X.var())
print(X.std())

#%% 下偏方差、下偏标准差
lowers = [e for e in X if e <= mu]
semivar = np.sum(np.square(lowers-mu)) / len(lowers)
print("X的下偏方差为：", semivar)
print("X的下偏标准差为：", np.sqrt(semivar))
#%% 目标下偏方差、目标下偏标准差
B = np.array(50.02154)
lowers2 = [e for e in X if e <= B]
semivar2 = np.sum(np.square(lowers2-B)) / len(lowers)
print("X的目标下偏方差为：", semivar2)
print("X的目标下偏标准差为：", np.sqrt(semivar2))