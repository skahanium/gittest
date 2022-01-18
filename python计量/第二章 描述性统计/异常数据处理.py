#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 10:45:16 2022

@author: skahanium
"""

import pandas as pd
import numpy as np
from scipy.stats.mstats import winsorize

data = pd.read_excel(r'/Users/skahanium/编程训练/python计量/第二章 描述性统计/rsr补全后的数据.xlsx')

#%% 描述性统计

result = data.describe()

#%% 绘制直方图

data['jf_rsr2'].hist(bins=100)

#%% 异常值处理(缩尾)
obj1 = data['人口密度'].copy()
obj1 = winsorize(obj1,(0.01, 0.01))
obj1 = pd.Series(obj1)
obj1.hist(bins=100)

#%% 异常值处理(固定比例法)
obj2 = data['人口密度'].copy()
obj2[obj2 >= obj2.quantile(0.99)] = obj2.quantile(0.99)
obj2[obj2 <= obj2.quantile(0.01)] = obj2.quantile(0.01)
obj2.hist(bins=100)

#%% 异常值处理(均值标准差法)

# 注：把三倍标准差之外的值都视为异常值

obj3 = data['人口密度'].copy()
obj3[obj3 >= obj3.mean() + 3*obj3.std()] = obj3.mean() + 3*obj3.std()
obj3[obj3 <= obj3.mean() - 3*obj3.std()] = obj3.mean() - 3*obj3.std()
obj3.hist(bins=100)

#%% 异常值处理(MAD法)
obj4 = data['jf_rsr2'].copy()
med = obj4.median()
MAD = np.abs(obj4 - med).median()
obj4[obj4 >= med + 3*MAD] = med + 3*MAD
obj4[obj4 <= med - 3*MAD] = med - 3*MAD
obj4.hist(bins=100)

