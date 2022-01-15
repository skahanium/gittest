#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 15:09:59 2022

@author: skahanium
"""
#%%
import scipy.stats as stats
import numpy as np

#%% 算数平均值
x1 = [1, 2, 3, 4, 5, 6, 4, 8, 9]
x2 = x1 + [12]

print(np.mean(x1))
print(np.mean(x2))

#%% 加权算数平均值
