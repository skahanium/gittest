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
io.savemat('a.mat', {'matrix' : a})
io.savemat('b.mat', {'array' : b})
#%% 数据读取
data1 = io.loadmat('a.mat')
data1_1 = io.loadmat('a.mat')['matrix']
data2 = io.loadmat('b.mat')
data2_2 = io.loadmat('b.mat')['array']