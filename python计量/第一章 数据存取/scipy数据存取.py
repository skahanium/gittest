#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 14:42:01 2022

@author: skahanium
"""
#%% 数据设置
import numpy as np
from scipy import io

a = np.mat('1, 2, 3; 4, 5, 6')
b = np.array([[1, 2, 3], [4, 5, 6]])
#%% 数据储存
io.savemat('/Users/skahanium/编程训练/python计量/第一章 数据存取/a.mat', {'matrix' : a})
io.savemat('/Users/skahanium/编程训练/python计量/第一章 数据存取/b.mat', {'array' : b})
#%% 数据读取
data1 = io.loadmat('/Users/skahanium/编程训练/python计量/第一章 数据存取/a.mat')
data1_1 = io.loadmat('/Users/skahanium/编程训练/python计量/第一章 数据存取/a.mat')['matrix']
data2 = io.loadmat('/Users/skahanium/编程训练/python计量/第一章 数据存取/b.mat')
data2_2 = io.loadmat('/Users/skahanium/编程训练/python计量/第一章 数据存取/b.mat')['array']
