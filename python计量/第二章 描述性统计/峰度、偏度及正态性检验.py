#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 17:41:23 2022

@author: skahanium
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from statsmodels.stats.stattools import jarque_bera

xs = np.linspace(-6, 6, 100)
normal = stats.norm.pdf(xs)
plt.plot(xs, normal)
#%% 偏度

# 先绘制两个正偏度与负偏度的分布看看形状

xs2 = np.linspace(stats.lognorm.ppf(0.01, .7, loc=-.1), stats.lognorm.ppf(0.99, .7, loc=-.1), 1500)
lognorm = stats.lognorm.pdf(xs2, .7)

plt.plot(xs2, lognorm, label='skew > 0')
plt.plot(xs2, lognorm[::-1], label='skew < 0')
plt.legend()

# 得到偏度
print("偏度为：", stats.skew(lognorm))

#%% 峰度

plt.plot(xs, stats.laplace.pdf(xs), label='Leptokurtic')
print('尖峰的超额峰度：', (stats.laplace.stats(moments='k')))
plt.plot(xs, normal, label='Mesokertic')
print('正态分布的超额峰度：', (stats.norm.stats(moments='k')))
plt.plot(xs, stats.cosine.pdf(xs), label='Platykurtic')
print('平峰的超额峰度：', (stats.cosine.stats(moments='k')))
plt.legend()

#%% 使用Jarque-Bera的正太检验

_, pvalue, _, _ = jarque_bera(xs2)

if pvalue > 0.05:
    print('服从正态分布')
else:
    print('不服从正态分布')