#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:58:05 2021

@author: new
"""

def miss_num_func(iter):
    return [x for x in range(iter[0], iter[-1]+1) 
                               if x not in iter]

iter = [0,1,2,4,5,6,7]

miss= miss_num_func(iter)
print(miss) 
