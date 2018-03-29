# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:02:38 2017

@author: ramals2
"""
import numpy
import matplotlib



s = 'azcbobobegghakl'



count = 0
itr = 0
for l in s:
    if l == 'b':
        if s[count:count+3] == 'bob':
            itr +=1
    count+=1

print(itr)
