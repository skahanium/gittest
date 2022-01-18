#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 14:21:41 2022

@author: skahanium
"""
#%% 数据设置
import numpy as np

a = np.mat('1, 2, 3; 4, 5, 6')
b = np.array([[1, 2, 3], [4, 5, 6]])
#%% 数据储存
np.save('/Users/skahanium/编程训练/python计量/第一章 数据存取/a.npy', a)
np.save('/Users/skahanium/编程训练/python计量/第一章 数据存取/b.npy', b)
#%% 数据读取
data_a = np.load('/Users/skahanium/编程训练/python计量/第一章 数据存取/a.npy')
data_b = np.load('/Users/skahanium/编程训练/python计量/第一章 数据存取/b.npy')